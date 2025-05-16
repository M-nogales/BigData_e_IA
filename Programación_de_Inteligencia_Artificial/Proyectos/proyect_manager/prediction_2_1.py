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
import numpy as np
import json
import joblib # For saving the model

def run_prediction_pipeline():
    """
    Runs the full pipeline: Load data, simulate assignments, create artificial
    target based on features, preprocess, train a model, and predict probabilities.
    """
    # --- load and inicial processing ---
    try:
        # --- Load json tasks (task_generator.py) ---
        json_file_path = "generated_tasks copy.json"
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                 task_data = json.load(f)
            task_df = pd.DataFrame(task_data)
            print(f"Successfully loaded task data from {json_file_path}")
        except FileNotFoundError:
            print(f"Error: JSON task file not found at {json_file_path}.")
            return
        except json.JSONDecodeError:
             print(f"Error: Could not decode JSON from {json_file_path}. Check file format.")
             return
        except Exception as e:
             print(f"Error loading JSON task data: {e}")
             return

        # --- load RRHH ---
        try:
            rrhh_df = pd.read_csv("datasets/RRHH.csv")
        except FileNotFoundError:
            print("Warning: 'datasets/RRHH.csv' not found. Trying 'RRHH.csv' in the current directory.")

        print("--- Task Categories Info (from JSON) ---")
        task_df.info() 

        # --- Clear RRHH dataset ---

        # Ensure column names from JSON match expected names and handle potential variations
        # Based on provided JSON, column names are correct: "Task Description", "Category", "Skill"
        task_df.rename(columns={
            "Task Description": "Task Description",
            "Category": "Category",
            "Skill": "Skill",
            "Difficulty Level": "Difficulty Level",
            "Estimated Time (hrs)": "Estimated Time (hrs)",
            "Area": "Area"
        }, inplace=True)

        if 'Skill' in task_df.columns:
            task_df['Skill'] = task_df['Skill'].str.lower().str.strip()
        else:
            print("Warning: 'Skill' column not found in task data after loading JSON.")

        print("\n\n--- RRHH Info ---")
        rrhh_df.info()

        def parse_tech_abilities(abilities_str):
            if pd.isna(abilities_str): return {}
            try:
                # Attempt to clean the string before evaluating
                if isinstance(abilities_str, str):
                    # Remove potential surrounding quotes if present
                    if abilities_str.startswith("'") and abilities_str.endswith("'"):
                        abilities_str = abilities_str[1:-1]
                    elif abilities_str.startswith('"') and abilities_str.endswith('"'):
                         abilities_str = abilities_str[1:-1]
                    # Replace common string representations of None/NaN with actual None just in case
                    abilities_str = abilities_str.replace("None", "None").replace("nan", "None")

                evaluated = ast.literal_eval(abilities_str)
                if isinstance(evaluated, dict):
                    # Ensure keys are strings, lowercased, and stripped
                    return {str(k).lower().strip(): v for k, v in evaluated.items() if k is not None}
                else:
                     # If not a dict after eval, return empty
                     return {}
            except (ValueError, SyntaxError, TypeError) as e:
                # print(f"Could not parse string '{abilities_str[:50]}...': {e}") # Optional: for debugging parsing errors
                return {} # Return empty dict on error

        rrhh_df['technical_abilities_dict'] = rrhh_df['technical_abilities'].apply(parse_tech_abilities)

        if 'Hire_Date' in rrhh_df.columns:
            rrhh_df['Hire_Date'] = pd.to_datetime(rrhh_df['Hire_Date'], errors='coerce')
        else:
            print("\nWarning: 'Hire_Date' column not found in RRHH.csv")

    except FileNotFoundError as e:
        print(f"Error: file do not found - {e}. Make sure the file is in the correct place.")
        return
    except Exception as e:
        print(f"Error: while loading/inicial processing: {e}")
        return

    # --- rule controlled assignments ---
    num_employees = len(rrhh_df)
    num_task_types = len(task_df)
    # ensure we have a reasonable number of assignments for training
    if num_employees > 0 and num_task_types > 0:
        # simulate the lower number of employees * 5 or 100
        total_assignments = min(num_employees * 5, 100)
        valid_employee_ids = rrhh_df['Employee_ID'].unique()
        # Ensure task descriptions in task_df are strings and not empty before sampling
        task_df_cleaned = task_df.dropna(subset=['Task Description'])
        task_df_cleaned = task_df_cleaned[task_df_cleaned['Task Description'] != '']

        valid_task_descriptions = task_df_cleaned['Task Description'].unique()


        if len(valid_employee_ids) == 0 or len(valid_task_descriptions) == 0:
             print("Error: there's no valid employee Ids or tasks descriptions for simulations.")
             return

        # Create assignations WITHOUT the Finish_On_Time column 
        assignment_data = {
            'Assignment_ID': range(1, total_assignments + 1),
            'Employee_ID': np.random.choice(valid_employee_ids, total_assignments),
            'Task Description': np.random.choice(valid_task_descriptions, total_assignments)
        }
        assignments_df = pd.DataFrame(assignment_data)
        print("\n\n--- Inicial Simulated Assignment Data ---")
        print(assignments_df.head())

        # --- 1. Combine DataFrames ---
        merged_df = pd.merge(assignments_df, rrhh_df, on='Employee_ID', how='left')

        # Ensure 'Task Description' is string type and strip whitespace before merge
        task_df['Task Description'] = task_df['Task Description'].astype(str).str.strip()
        merged_df['Task Description'] = merged_df['Task Description'].astype(str).str.strip()

        # Perform the merge with task_df
        merged_df = pd.merge(merged_df, task_df, on='Task Description', how='left')

        initial_rows = len(merged_df)
        # Keep only rows where task details (Category and Skill) were successfully merged
        merged_df.dropna(subset=['Category', 'Skill'], inplace=True)

        if len(merged_df) < initial_rows:
            print(f"\nWarning: Removed {initial_rows - len(merged_df)} assignments due to missing task details after merge.")
        if merged_df.empty:
            print("Error: There's no data to combine and clear, is not possible to continues.")
            return

        # --- 2. New columns for training ---
        # a) Tenure
        current_date = pd.to_datetime(datetime.now())
        if 'Hire_Date' in merged_df.columns and pd.api.types.is_datetime64_any_dtype(merged_df['Hire_Date']):
            # Calculate tenure only for valid dates
            valid_dates_mask = merged_df['Hire_Date'].notna()
            merged_df.loc[valid_dates_mask, 'Tenure_Years'] = (current_date - merged_df.loc[valid_dates_mask, 'Hire_Date']).dt.days / 365.25
            # Fill NaN tenure for invalid dates, maybe with median or 0
            if merged_df['Hire_Date'].isnull().any():
                 merged_df['Tenure_Years'].fillna(merged_df['Tenure_Years'].median() if merged_df['Tenure_Years'].median() is not np.nan else 0.0, inplace=True)

        elif 'Years_At_Company' in merged_df.columns:
             merged_df['Tenure_Years'] = merged_df['Years_At_Company']
        else:
             merged_df['Tenure_Years'] = 0.0
             print("Warning: Could not calculate or find 'Tenure_Years'. Setting to 0.")

        # b) For the assignment, get the skill match score
        def get_skill_score(row):
            required_skill = row['Skill']
            abilities_dict = row['technical_abilities_dict']
            # Ensure required_skill is a string and abilities_dict is a dict for safe lookup
            if not isinstance(required_skill, str) or pd.isna(required_skill) or not isinstance(abilities_dict, dict):
                 return 0.0
            return float(abilities_dict.get(required_skill.lower().strip(), 0.0))


        merged_df['Skill_Match_Score'] = merged_df.apply(get_skill_score, axis=1)

        # c) Manage tasks with various Skills (if any assignment merged with multiple skill rows)
        # This block prevents the same assignment from being assigned to more than one worker,
        #  which would be redundant or conflicting in a random or merit-based assignment.
        #  It also correctly handles cases where a task may have multiple potential matches, choosing only the best.

        if 'Assignment_ID' in merged_df.columns:
             merged_df = merged_df.sort_values('Skill_Match_Score', ascending=False)
             merged_df = merged_df.drop_duplicates(subset=['Assignment_ID'], keep='first')

        # --- 3. ARTIFICIAL CREATION OF THE TARGET 'Finished_On_Time' ---
        print("\n--- Creating Artificial Target 'Finished_On_Time' based on Features ---")

        def create_artificial_target(row):
            """
            Create a True/False value for Finished_On_Time based on features.
            """
            # Ensure the columns exist; otherwise, use neutral value (already imputed/defaulted)
            skill_match = row['Skill_Match_Score']
            perf_score = row['Performance_Score']
            # Use Tenure_Years, which comes from Hire_Date, Years_At_Company, or default
            experience_years = row['Tenure_Years']  # Use Tenure_Years instead of Years_At_Company directly
            overtime = row['Overtime_Hours']

            # Calculate a base probability and adjust it
            # Normalizing/scaling helps, but here we simplify with expected ranges
            prob = 0.5  # Base probability

            # Adjustment for Skill Match (more skill -> more likely to finish on time)
            # Assuming scale 0–10. A value of 5 is neutral.
            prob += (skill_match - 5.0) * 0.04  # Moderate adjustment

            # Adjustment for Performance Score (higher performance -> more likely)
            # Assuming scale 1–5. A value of 3 is neutral.
            prob += (perf_score - 3.0) * 0.06  # Slightly stronger adjustment

            # Adjustment for Experience (more experience -> more likely)
            # Using Tenure_Years. A value of 3 years is neutral.
            prob += (experience_years - 3.0) * 0.01  # Small adjustment

            # Adjustment for Overtime Hours (more overtime -> less likely to finish *this* task on time?)
            # Might indicate overload or difficulty. A value of 8 is neutral.
            prob -= (overtime - 8.0) * 0.01  # Small negative adjustment

            # Ensure the probability stays within reasonable limits (e.g., 0.05 to 0.95)
            prob = np.clip(prob, 0.05, 0.95)

            # Decide True/False based on this probability
            return np.random.rand() < prob

        # Apply the function to create the target column
        merged_df['Finished_On_Time'] = merged_df.apply(create_artificial_target, axis=1)

        print("Artificial target created. Distribution:")
        print(merged_df['Finished_On_Time'].value_counts(normalize=True))

        print("\n--- Merged DataFrame After Feature Engineering & Artificial Target ---")
        print(merged_df[['Assignment_ID', 'Skill_Match_Score','Performance_Score','Tenure_Years','Overtime_Hours','Finished_On_Time']].head())


        # --- 4. Features selection and objective ---
        potential_features = [
             'Age', 'Years_At_Company', 'Performance_Score', 'Monthly_Salary',
             'Work_Hours_Per_Week', 'Projects_Handled', 'Overtime_Hours',
             'Sick_Days', 'Remote_Work_Frequency', 'Team_Size', 'Training_Hours',
             'Promotions', 'Employee_Satisfaction_Score', 'Tenure_Years', 'Skill_Match_Score',
             'Department', 'Gender', 'Job_Title', 'Education_Level', 'Category'
        ]
        # Filter features to include only those present in the merged_df
        features = [f for f in potential_features if f in merged_df.columns]
        target = 'Finished_On_Time' 

        if target not in merged_df.columns: print(f"Error: target '{target}' not found ."); return
        if len(merged_df) == 0: print("Error: There's no data before processing."); return

        X = merged_df[features].copy()
        y = merged_df[target].astype(int)

        # Final clear of nan and null values in numerical and categorical features
        numerical_features = X.select_dtypes(include=np.number).columns.tolist()
        categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()

        for col in numerical_features:
            if X[col].isnull().any():
                 median_val = X[col].median()
                 if pd.isna(median_val):
                     X[col].fillna(0.0, inplace=True)
                 else:
                     X[col].fillna(median_val, inplace=True)

        for col in categorical_features:
            if X[col].isnull().any():
                 X[col].fillna('Missing', inplace=True)


        print("\n--- Features Selected for Model Training ---")
        print("Numerical:", numerical_features)
        print("Categorical:", categorical_features)

        if len(X) < 20 or len(y.value_counts()) < 2:
            print(f"Error: Not enought data ({len(X)} filas) or only a singel value in the target for train ({y.value_counts().to_dict()}).")
            return

        # --- 5. Preprocessing (Pipeline) ---
        # Check if there are numerical or categorical features to process
        transformers_list = []
        if numerical_features:
            transformers_list.append(('num', StandardScaler(), numerical_features))
        if categorical_features:
            transformers_list.append(('cat', OneHotEncoder(handle_unknown='ignore', drop='first', sparse_output=False), categorical_features))

        if not transformers_list:
             print("Error: Not enought numerical or categorical features for preprocessing.")
             return

        preprocessor = ColumnTransformer(
             transformers=transformers_list,
             remainder='drop'
        )


        # --- 6. Split the data and create the model pipelines ---
        # Stratification: ensuring that the class distribution of the target variable (y) is preserved when splitting the datase
        try:
             # Check if stratification is possible (at least two classes and minimum samples in each)
             if len(y.value_counts()) >= 2 and min(y.value_counts()) >= 2: # Ensure at least 2 samples per class for stratification
                 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
                 print("Data split with stratification.")
             else:
                 print("\nWarning: Stratification not possible (not enough classes or samples). Splitting without stratification.")
                 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        except ValueError as e:
             print(f"\nWarning: Error during stratification ({e}). Splitting without stratification.")
             X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        model_pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', LogisticRegression(random_state=42, solver='liblinear', class_weight='balanced'))
        ])

        # --- 7. Entrenar el Modelo ---
        print("\n--- Training Model ---")
        try:
            model_pipeline.fit(X_train, y_train)
            print("Model training complete.")
        except Exception as e:
            print(f"Error: during training {e}")
            return
        # Guardar el modelo entrenado
        try:
            joblib.dump(model_pipeline, 'trained_model.pkl')
            print("Model saved as 'trained_model.pkl'.")
        except Exception as e:
            print(f"Error saving model: {e}")

        # --- 8. Evaluar el Modelo ---
        print("\n--- Model Evaluation ---")
        try:
            if X_test.empty:
                 print("No test data available for evaluation.")
            else:
                 y_pred = model_pipeline.predict(X_test)
                 y_pred_proba = model_pipeline.predict_proba(X_test)[:, 1]

                 print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
                 if len(np.unique(y_test)) > 1:
                     print(f"ROC AUC: {roc_auc_score(y_test, y_pred_proba):.4f}")
                 else: print("ROC AUC: Cannot calculate (only one class in test set)")

                 if len(y_test) > 0 and len(np.unique(y_test)) > 1:
                      print(f"Log Loss: {log_loss(y_test, y_pred_proba):.4f}")
                      print("\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=0))
                 elif len(y_test) > 0:
                      print("Log Loss: Cannot calculate (only one class in test set)")
                      print("\nClassification Report: Cannot calculate (only one class in test set)")
                 else:
                      print("No test samples to calculate metrics.")

        except Exception as e:
            print(f"Error during evaluation: {e}")

        # --- 9. Predicting Probabilities for Test Data ---
        print("\n--- Predicting Probabilities for Test Data (Sample) ---")
        try:
            if not X_test.empty:
                 y_test = y_test.loc[X_test.index]
                 results_df = pd.DataFrame({
                     'Actual_Finished_On_Time': y_test.values,
                     'Predicted_Finished_On_Time': y_pred,
                     'Probability_Finish_On_Time': y_pred_proba.round(4)
                 }, index=X_test.index)
                 print(results_df.head())

                 try:
                     # Get feature names out of the preprocessor
                     if hasattr(model_pipeline.named_steps['preprocessor'], 'get_feature_names_out'):
                          feature_names_out = model_pipeline.named_steps['preprocessor'].get_feature_names_out()
                          print(f"\nNumber of features after transformation: {len(feature_names_out)}")
                     else:
                          print("\nCould not get feature names (get_feature_names_out not available).")
                 except Exception as fe: print(f"Could not get feature names: {fe}")
            else:
                 print("No test data to predict probabilities.")


        except Exception as e:
            print(f"Error during probabilities prediction: {e}")

    else:
        print("\nError: It couldn't be load the employees or the task for the simulation.")

# --- execute pipeline ---
if __name__ == "__main__":
    run_prediction_pipeline()