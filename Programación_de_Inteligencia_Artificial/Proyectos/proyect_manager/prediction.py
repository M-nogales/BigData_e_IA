import pandas as pd
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
    Runs the full pipeline: Load data, simulate assignments, preprocess,
    train a model, and predict probabilities for finishing tasks on time.
    """
    # --- Carga y Procesamiento Inicial ---
    try:
        # Cargar datasets
        task_df = pd.read_csv("task_categories_copy.csv")
        # Intentar cargar RRHH.csv desde 'datasets/' o el directorio actual
        try:
            rrhh_df = pd.read_csv("datasets/RRHH.csv")
        except FileNotFoundError:
            print("Warning: 'datasets/RRHH.csv' not found. Trying 'RRHH.csv' in the current directory.")
            rrhh_df = pd.read_csv("RRHH.csv")

        print("--- Task Categories Info ---")
        task_df.info()
        # Estandarizar 'Skill' a minúsculas y sin espacios extra
        task_df['Skill'] = task_df['Skill'].str.lower().str.strip()
        print("\nUnique Skills Required (lowercase, stripped):")
        print(task_df['Skill'].unique())

        print("\n\n--- RRHH Info ---")
        rrhh_df.info()

        # --- Procesar 'technical_abilities' ---
        def parse_tech_abilities(abilities_str):
            """Parsea de forma segura un string que representa un diccionario de habilidades."""
            if pd.isna(abilities_str): return {}
            try:
                # Limpiar comillas externas si existen
                if isinstance(abilities_str, str):
                    if abilities_str.startswith("'") and abilities_str.endswith("'"): abilities_str = abilities_str[1:-1]
                    elif abilities_str.startswith('"') and abilities_str.endswith('"'): abilities_str = abilities_str[1:-1]
                evaluated = ast.literal_eval(abilities_str)
                if isinstance(evaluated, dict):
                    # Estandarizar claves a minúsculas y sin espacios
                    return {str(k).lower().strip(): v for k, v in evaluated.items()}
                else: return {}
            except: return {} # Captura cualquier error de parseo

        rrhh_df['technical_abilities_dict'] = rrhh_df['technical_abilities'].apply(parse_tech_abilities)

        # --- Convertir 'Hire_Date' ---
        if 'Hire_Date' in rrhh_df.columns:
            rrhh_df['Hire_Date'] = pd.to_datetime(rrhh_df['Hire_Date'], errors='coerce')
        else:
            print("\nWarning: 'Hire_Date' column not found in RRHH.csv")

    # --- Manejo de Errores de Archivo ---
    except FileNotFoundError as e:
        print(f"Error crítico: Archivo no encontrado - {e}. Asegúrate de que los archivos CSV estén accesibles.")
        return # Salir de la función si falla la carga
    except Exception as e:
        print(f"Error crítico durante la carga/procesamiento inicial: {e}")
        return # Salir de la función

    # --- !! SIMULACIÓN DE DATOS DE ASIGNACIONES (REEMPLAZAR CON DATOS REALES) !! ---
    num_employees = len(rrhh_df)
    num_task_types = len(task_df)

    if num_employees > 0 and num_task_types > 0:
        total_assignments = min(num_employees * 5, 100) # Crear más datos simulados si es posible
        valid_employee_ids = rrhh_df['Employee_ID'].unique()
        valid_task_descriptions = task_df['Task Description'].unique()

        if len(valid_employee_ids) == 0 or len(valid_task_descriptions) == 0:
             print("Error: No hay IDs de empleado válidos o descripciones de tarea válidas para simular asignaciones.")
             return # Salir de la función

        assignment_data = {
            'Assignment_ID': range(1, total_assignments + 1),
            'Employee_ID': np.random.choice(valid_employee_ids, total_assignments),
            'Task Description': np.random.choice(valid_task_descriptions, total_assignments),
            # Variable objetivo ARTIFICIAL: True si termina a tiempo, False si no
            'Finished_On_Time': np.random.choice([True, False], total_assignments, p=[0.65, 0.35]) # Ponderado ligeramente hacia True
        }
        assignments_df = pd.DataFrame(assignment_data)
        print("\n\n--- Simulated Assignment Data (DEMO ONLY) ---")
        print(assignments_df.head())

        # --- 1. Combinar DataFrames ---
        #!warning
        merged_df = pd.merge(assignments_df, rrhh_df, on='Employee_ID', how='left')
        # Limpiar 'Task Description' antes del merge
        task_df['Task Description'] = task_df['Task Description'].str.strip()
        merged_df['Task Description'] = merged_df['Task Description'].str.strip()
        merged_df = pd.merge(merged_df, task_df, on='Task Description', how='left')

        # Eliminar filas donde el merge falló (faltan detalles de la tarea)
        initial_rows = len(merged_df)
        merged_df.dropna(subset=['Category', 'Skill'], inplace=True)
        if len(merged_df) < initial_rows:
            print(f"\nWarning: Removed {initial_rows - len(merged_df)} assignments due to missing task details after merge.")

        if merged_df.empty:
            print("Error crítico: No quedan datos después de combinar y limpiar. No se puede continuar.")
            return

        print("\n\n--- Merged DataFrame Head ---")
        print(merged_df.head())

        # --- 2. Ingeniería de Características ---
        # a) Antigüedad (Tenure)
        #warning, years_at_company
        current_date = pd.to_datetime(datetime.now())
        if 'Hire_Date' in merged_df.columns and pd.api.types.is_datetime64_any_dtype(merged_df['Hire_Date']):
            merged_df['Tenure_Years'] = (current_date - merged_df['Hire_Date']).dt.days / 365.25
            merged_df['Tenure_Years'] = merged_df['Tenure_Years'].fillna(merged_df['Tenure_Years'].median())
        elif 'Years_At_Company' in merged_df.columns:
             merged_df['Tenure_Years'] = merged_df['Years_At_Company'].fillna(merged_df['Years_At_Company'].median())
        else:
             merged_df['Tenure_Years'] = 0.0

        # b) Puntuación de Coincidencia de Habilidad (Skill Match)
        def get_skill_score(row):
            required_skill = row['Skill']
            abilities_dict = row['technical_abilities_dict']
            if pd.isna(required_skill) or not isinstance(abilities_dict, dict): return 0.0
            return float(abilities_dict.get(required_skill, 0.0))

        merged_df['Skill_Match_Score'] = merged_df.apply(get_skill_score, axis=1)

        # c) Manejar Tareas con Múltiples Skills (si aplica tras merge)
        if 'Assignment_ID' in merged_df.columns:
             print(f"\nDataFrame size before handling multi-skill tasks: {len(merged_df)}")
             merged_df = merged_df.sort_values('Skill_Match_Score', ascending=False)
             merged_df = merged_df.drop_duplicates(subset=['Assignment_ID'], keep='first')
             print(f"DataFrame size after handling multi-skill tasks: {len(merged_df)}")

        print("\n\n--- Merged DataFrame After Feature Engineering (Sample) ---")
        print(merged_df[['Assignment_ID', 'Employee_ID', 'Task Description', 'Skill', 'Skill_Match_Score', 'Tenure_Years', 'Finished_On_Time']].head())

        # --- 3. Selección de Características y Objetivo + Imputación ---
        potential_features = [
            'Age', 'Years_At_Company', 'Performance_Score', 'Monthly_Salary',
            'Work_Hours_Per_Week', 'Projects_Handled', 'Overtime_Hours',
            'Sick_Days', 'Remote_Work_Frequency', 'Team_Size', 'Training_Hours',
            'Promotions', 'Employee_Satisfaction_Score', 'Tenure_Years', 'Skill_Match_Score',
            'Department', 'Gender', 'Job_Title', 'Education_Level', 'Category'
        ]
        features = [f for f in potential_features if f in merged_df.columns]
        target = 'Finished_On_Time'

        if target not in merged_df.columns: print(f"Error crítico: Variable objetivo '{target}' no encontrada."); return
        if len(merged_df) == 0: print("Error crítico: No hay datos tras procesar."); return

        X = merged_df[features].copy() # Usar copia para evitar SettingWithCopyWarning
        y = merged_df[target].astype(int)

        # Identificar tipos e Imputar NaNs restantes en X
        numerical_features = X.select_dtypes(include=np.number).columns.tolist()
        categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()

        for col in numerical_features:
            if X[col].isnull().any(): X[col].fillna(X[col].median(), inplace=True)
        for col in categorical_features:
            if X[col].isnull().any(): X[col].fillna('Missing', inplace=True)

        print("\n--- Features Selected ---")
        print("Numerical:", numerical_features)
        print("Categorical:", categorical_features)

        # Verificar si hay suficientes datos y clases
        if len(X) < 20 or len(y.value_counts()) < 2:
            print(f"\nError crítico: Datos insuficientes ({len(X)} filas) o solo una clase presente ({y.value_counts().to_dict()}) para entrenar.")
            return

        # --- 4. Preprocesamiento (Pipeline) ---
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_features),
                ('cat', OneHotEncoder(handle_unknown='ignore', drop='first', sparse_output=False), categorical_features)
            ],
            remainder='drop'
        )

        # --- 5. Dividir Datos y Crear Pipeline del Modelo ---
        try:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        except ValueError:
            print("\nWarning: No se pudo estratificar (pocas muestras en una clase). Dividiendo sin estratificación.")
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model_pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', LogisticRegression(random_state=42, solver='liblinear', class_weight='balanced'))
        ])

        # --- 6. Entrenar el Modelo ---
        print("\n--- Training Model ---")
        try:
            model_pipeline.fit(X_train, y_train)
            print("Model training complete.")
        except Exception as e:
            print(f"Error crítico durante el entrenamiento: {e}")
            try:
                X_train_transformed = model_pipeline.named_steps['preprocessor'].fit_transform(X_train)
                print(f"Shape of transformed training data: {X_train_transformed.shape}")
                if np.isnan(X_train_transformed).any(): print("NaNs found in transformed training data.")
                if not np.isfinite(X_train_transformed).all(): print("Infinities or values too large found.")
            except Exception as pe: print(f"Error during preprocessing check: {pe}")
            return

        # --- 7. Evaluar el Modelo ---
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

        # --- 8. Predecir Probabilidades para Datos de Prueba ---
        print("\n--- Predicting Probabilities for Test Data (Sample) ---")
        try:
            # Alinear y_test con X_test si los índices se desordenaron
            y_test = y_test.loc[X_test.index] # Re-align index just in case
            results_df = pd.DataFrame({
                'Actual_Finished_On_Time': y_test.values,
                'Predicted_Finished_On_Time': y_pred,
                'Probability_Finish_On_Time': y_pred_proba.round(4)
            }, index=X_test.index) # Usar índice de X_test
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