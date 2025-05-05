import pandas as pd
import io
import ast
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, log_loss
import numpy as np # For handling potential missing values during skill lookup

def run_prediction_pipeline():
    """
    Runs the full pipeline: Load data, simulate assignments, create artificial
    target based on features, preprocess, train a model, and predict probabilities.
    """
    # --- Carga y Procesamiento Inicial ---
    try:
        task_df = pd.read_csv("task_categories_copy.csv")
        try:
            rrhh_df = pd.read_csv("datasets/RRHH.csv")
        except FileNotFoundError:
            print("Warning: 'datasets/RRHH.csv' not found. Trying 'RRHH.csv' in the current directory.")
            rrhh_df = pd.read_csv("RRHH.csv")

        print("--- Task Categories Info ---")
        # task_df.info() # Comentado para brevedad
        task_df['Skill'] = task_df['Skill'].str.lower().str.strip()
        # print("\nUnique Skills Required (lowercase, stripped):")
        # print(task_df['Skill'].unique())

        print("\n\n--- RRHH Info ---")
        # rrhh_df.info() # Comentado para brevedad

        def parse_tech_abilities(abilities_str):
            if pd.isna(abilities_str): return {}
            try:
                if isinstance(abilities_str, str):
                    if abilities_str.startswith("'") and abilities_str.endswith("'"): abilities_str = abilities_str[1:-1]
                    elif abilities_str.startswith('"') and abilities_str.endswith('"'): abilities_str = abilities_str[1:-1]
                evaluated = ast.literal_eval(abilities_str)
                if isinstance(evaluated, dict):
                    return {str(k).lower().strip(): v for k, v in evaluated.items()}
                else: return {}
            except: return {}

        rrhh_df['technical_abilities_dict'] = rrhh_df['technical_abilities'].apply(parse_tech_abilities)

        if 'Hire_Date' in rrhh_df.columns:
            rrhh_df['Hire_Date'] = pd.to_datetime(rrhh_df['Hire_Date'], errors='coerce')
        else:
            print("\nWarning: 'Hire_Date' column not found in RRHH.csv")

    except FileNotFoundError as e:
        print(f"Error crítico: Archivo no encontrado - {e}. Asegúrate de que los archivos CSV estén accesibles.")
        return
    except Exception as e:
        print(f"Error crítico durante la carga/procesamiento inicial: {e}")
        return

    # --- !! SIMULACIÓN DE ASIGNACIONES (SIN TARGET INICIAL) !! ---
    num_employees = len(rrhh_df)
    num_task_types = len(task_df)

    if num_employees > 0 and num_task_types > 0:
        total_assignments = min(num_employees * 5, 100)
        valid_employee_ids = rrhh_df['Employee_ID'].unique()
        valid_task_descriptions = task_df['Task Description'].unique()

        if len(valid_employee_ids) == 0 or len(valid_task_descriptions) == 0:
             print("Error: No hay IDs de empleado válidos o descripciones de tarea válidas para simular asignaciones.")
             return

        # Crear asignaciones SIN la columna Finished_On_Time todavía
        assignment_data = {
            'Assignment_ID': range(1, total_assignments + 1),
            'Employee_ID': np.random.choice(valid_employee_ids, total_assignments),
            'Task Description': np.random.choice(valid_task_descriptions, total_assignments)
        }
        assignments_df = pd.DataFrame(assignment_data)
        print("\n\n--- Simulated Assignment Data (Initial - NO TARGET YET) ---")
        print(assignments_df.head())

        # --- 1. Combinar DataFrames ---
        merged_df = pd.merge(assignments_df, rrhh_df, on='Employee_ID', how='left')
        task_df['Task Description'] = task_df['Task Description'].str.strip()
        merged_df['Task Description'] = merged_df['Task Description'].str.strip()
        merged_df = pd.merge(merged_df, task_df, on='Task Description', how='left')

        initial_rows = len(merged_df)
        merged_df.dropna(subset=['Category', 'Skill'], inplace=True)
        if len(merged_df) < initial_rows:
            print(f"\nWarning: Removed {initial_rows - len(merged_df)} assignments due to missing task details after merge.")

        if merged_df.empty:
            print("Error crítico: No quedan datos después de combinar y limpiar. No se puede continuar.")
            return

        # --- 2. Ingeniería de Características ---
        # a) Antigüedad (Tenure)
        current_date = pd.to_datetime(datetime.now())
        if 'Hire_Date' in merged_df.columns and pd.api.types.is_datetime64_any_dtype(merged_df['Hire_Date']):
            merged_df['Tenure_Years'] = (current_date - merged_df['Hire_Date']).dt.days / 365.25
        elif 'Years_At_Company' in merged_df.columns:
             merged_df['Tenure_Years'] = merged_df['Years_At_Company'] # Usar directamente si existe
        else:
             merged_df['Tenure_Years'] = 0.0 # Default si no hay fecha ni años

        # b) Puntuación de Coincidencia de Habilidad (Skill Match)
        def get_skill_score(row):
            required_skill = row['Skill']
            abilities_dict = row['technical_abilities_dict']
            if pd.isna(required_skill) or not isinstance(abilities_dict, dict): return 0.0
            return float(abilities_dict.get(required_skill, 0.0))

        merged_df['Skill_Match_Score'] = merged_df.apply(get_skill_score, axis=1)

        # c) Manejar Tareas con Múltiples Skills
        if 'Assignment_ID' in merged_df.columns:
             # print(f"\nDataFrame size before handling multi-skill tasks: {len(merged_df)}")
             merged_df = merged_df.sort_values('Skill_Match_Score', ascending=False)
             merged_df = merged_df.drop_duplicates(subset=['Assignment_ID'], keep='first')
             # print(f"DataFrame size after handling multi-skill tasks: {len(merged_df)}")


        # --- 3. IMPUTACIÓN PREVIA para las características usadas en la regla ---
        # Imputar NaNs ANTES de crear la regla artificial
        # Usaremos estas columnas en la regla, así que deben tener valores
        cols_for_rule = ['Skill_Match_Score', 'Performance_Score', 'Years_At_Company', 'Overtime_Hours', 'Tenure_Years']
        for col in cols_for_rule:
            if col in merged_df.columns:
                if merged_df[col].isnull().any():
                    median_val = merged_df[col].median()
                    merged_df[col].fillna(median_val, inplace=True)
                    print(f"Imputed NaNs in '{col}' with median {median_val:.2f} before creating target.")
            else:
                 print(f"Warning: Column '{col}' needed for artificial target rule not found. Target generation might be less accurate.")
                 # Podrías añadir una columna dummy si falta, ej: merged_df[col] = 0


        # --- 4. CREACIÓN ARTIFICIAL DEL TARGET 'Finished_On_Time' ---
        print("\n--- Creating Artificial Target 'Finished_On_Time' based on Features ---")
        def crear_target_artificial(row):
            """
            Crea un valor True/False para Finished_On_Time basado en características.
            Esta lógica es *arbitraria* y solo para demostración.
            """
            # Asegurarse que las columnas existen, si no, usar valor neutral (ej: mediana o 0)
            skill_match = row.get('Skill_Match_Score', 0.0) # Default 0 si no existe
            perf_score = row.get('Performance_Score', 3.0) # Default 3 si no existe
            years_at_co = row.get('Years_At_Company', 1.0) # Default 1 si no existe
            overtime = row.get('Overtime_Hours', 10.0)     # Default 10 si no existe

            # Calcular una probabilidad base y ajustarla
            # Normalizar/escalar los valores ayuda, pero para simplificar usamos rangos esperados
            prob = 0.5  # Probabilidad base

            # Ajuste por Skill Match (más habilidad -> más probable terminar a tiempo)
            # Asumiendo escala 0-10. Un valor de 5 es neutral.
            prob += (skill_match - 5.0) * 0.04 # Ajuste moderado

            # Ajuste por Performance Score (más performance -> más probable)
            # Asumiendo escala 1-5. Un valor de 3 es neutral.
            prob += (perf_score - 3.0) * 0.06 # Ajuste un poco mayor

            # Ajuste por Años en Compañía (más experiencia -> más probable)
            # Un valor de 3 años es neutral.
            prob += (years_at_co - 3.0) * 0.01 # Ajuste pequeño

            # Ajuste por Horas Extra (más horas extra -> menos probable terminar *esta* a tiempo?)
            # Podría indicar sobrecarga o dificultad. Un valor de 8 es neutral.
            prob -= (overtime - 8.0) * 0.01 # Ajuste pequeño negativo

            # Asegurar que la probabilidad esté entre límites razonables (ej. 0.05 y 0.95)
            prob = np.clip(prob, 0.05, 0.95)

            # Decidir True/False basado en esta probabilidad
            return np.random.rand() < prob

        # Aplicar la función para crear la columna objetivo
        merged_df['Finished_On_Time'] = merged_df.apply(crear_target_artificial, axis=1)

        print("Artificial target created. Distribution:")
        print(merged_df['Finished_On_Time'].value_counts(normalize=True))
        print("\n--- Merged DataFrame After Feature Engineering & Artificial Target (Sample) ---")
        print(merged_df[['Assignment_ID', 'Skill_Match_Score','Performance_Score','Years_At_Company','Overtime_Hours','Finished_On_Time']].head())


        # --- 5. Selección Final de Características y Objetivo + Imputación Final ---
        potential_features = [
            'Age', 'Years_At_Company', 'Performance_Score', 'Monthly_Salary',
            'Work_Hours_Per_Week', 'Projects_Handled', 'Overtime_Hours',
            'Sick_Days', 'Remote_Work_Frequency', 'Team_Size', 'Training_Hours',
            'Promotions', 'Employee_Satisfaction_Score', 'Tenure_Years', 'Skill_Match_Score',
            'Department', 'Gender', 'Job_Title', 'Education_Level', 'Category'
        ]
        features = [f for f in potential_features if f in merged_df.columns]
        target = 'Finished_On_Time' # Ya creado

        if target not in merged_df.columns: print(f"Error crítico: Variable objetivo '{target}' no encontrada."); return
        if len(merged_df) == 0: print("Error crítico: No hay datos tras procesar."); return

        X = merged_df[features].copy()
        y = merged_df[target].astype(int)

        # Imputación final para CUALQUIER NaN restante en X antes del pipeline
        numerical_features = X.select_dtypes(include=np.number).columns.tolist()
        categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()

        for col in numerical_features:
            if X[col].isnull().any(): X[col].fillna(X[col].median(), inplace=True)
        for col in categorical_features:
            if X[col].isnull().any(): X[col].fillna('Missing', inplace=True)

        print("\n--- Features Selected for Model Training ---")
        print("Numerical:", numerical_features)
        print("Categorical:", categorical_features)

        if len(X) < 20 or len(y.value_counts()) < 2:
            print(f"\nError crítico: Datos insuficientes ({len(X)} filas) o solo una clase presente ({y.value_counts().to_dict()}) para entrenar.")
            return

        # --- 6. Preprocesamiento (Pipeline) ---
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_features),
                ('cat', OneHotEncoder(handle_unknown='ignore', drop='first', sparse_output=False), categorical_features)
            ],
            remainder='drop'
        )

        # --- 7. Dividir Datos y Crear Pipeline del Modelo ---
        try:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
        except ValueError:
            print("\nWarning: No se pudo estratificar. Dividiendo sin estratificación.")
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        model_pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', LogisticRegression(random_state=42, solver='liblinear', class_weight='balanced'))
        ])

        # --- 8. Entrenar el Modelo ---
        print("\n--- Training Model ---")
        try:
            model_pipeline.fit(X_train, y_train)
            print("Model training complete.")
        except Exception as e:
            print(f"Error crítico durante el entrenamiento: {e}")
            return

        # --- 9. Evaluar el Modelo ---
        print("\n--- Model Evaluation ---")
        try:
            y_pred = model_pipeline.predict(X_test)
            y_pred_proba = model_pipeline.predict_proba(X_test)[:, 1]

            print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
            if len(np.unique(y_test)) > 1:
                print(f"ROC AUC: {roc_auc_score(y_test, y_pred_proba):.4f}")
            else: print("ROC AUC: Cannot calculate (only one class in test set)")
            print(f"Log Loss: {log_loss(y_test, y_pred_proba):.4f}")
            print("\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=0))
        except Exception as e:
            print(f"Error durante la evaluación: {e}")

        # --- 10. Predecir Probabilidades para Datos de Prueba ---
        print("\n--- Predicting Probabilities for Test Data (Sample) ---")
        try:
            y_test = y_test.loc[X_test.index] # Alinear índice
            results_df = pd.DataFrame({
                'Actual_Finished_On_Time': y_test.values,
                'Predicted_Finished_On_Time': y_pred,
                'Probability_Finish_On_Time': y_pred_proba.round(4)
            }, index=X_test.index)
            print(results_df.head())

            try:
                feature_names_out = model_pipeline.named_steps['preprocessor'].get_feature_names_out()
                print(f"\nNumber of features after transformation: {len(feature_names_out)}")
            except Exception as fe: print(f"Could not get feature names: {fe}")

        except Exception as e:
            print(f"Error durante la predicción de probabilidades: {e}")

    else:
        print("\nError crítico: No se pudieron cargar datos de empleados o tareas para la simulación.")

    print("\n--- Pipeline Function Finished ---")

# --- Ejecutar el Pipeline ---
if __name__ == "__main__":
    run_prediction_pipeline()