from flask import Flask, render_template, request
import json
import joblib
import pandas as pd
import numpy as np
from datetime import datetime

app = Flask(__name__)
model = joblib.load("trained_model.pkl")

@app.route("/", methods=["GET", "POST"])
def formulario():
    prediction_result = None

    if request.method == "POST":
        form_data = request.form.to_dict()

        # --- Parse technical abilities ---
        raw_skills = form_data.get("technical_abilities", "{}")
        try:
            skills_dict = json.loads(raw_skills)
        except json.JSONDecodeError:
            skills_dict = {}

        # Expand skills as columns
        for k, v in skills_dict.items():
            form_data[f"skill_{k.lower().strip()}"] = v

        # Keep original dict as well
        form_data["technical_abilities_dict"] = skills_dict
        

        # --- Process numeric types and dates ---
        processed = {}
        for key, value in form_data.items():
            if key == "Hire_Date":
                try:
                    processed[key] = pd.to_datetime(value)
                except Exception:
                    processed[key] = pd.NaT
            elif isinstance(value, dict):
                processed[key] = value  # keep as dict
            else:
                try:
                    processed[key] = float(value)
                except (ValueError, TypeError):
                    processed[key] = value


        df = pd.DataFrame([processed])

        # --- Calculate Tenure_Years ---
        current_date = pd.to_datetime(datetime.now())
        if "Hire_Date" in df.columns and pd.api.types.is_datetime64_any_dtype(df["Hire_Date"]):
            valid_mask = df["Hire_Date"].notna()
            df.loc[valid_mask, "Tenure_Years"] = (current_date - df.loc[valid_mask, "Hire_Date"]).dt.days / 365.25
            if df["Hire_Date"].isnull().any():
                df["Tenure_Years"].fillna(df["Tenure_Years"].median() if df["Tenure_Years"].median() is not np.nan else 0.0, inplace=True)
        elif "Years_At_Company" in df.columns:
            df["Tenure_Years"] = df["Years_At_Company"]
        else:
            df["Tenure_Years"] = 0.0

        # --- Calculate  Skill_Match_Score ---
        def get_skill_score(row):
            required = row.get("Skill", "")
            skills = row.get("technical_abilities_dict", {})
            if not isinstance(required, str) or pd.isna(required) or not isinstance(skills, dict):
                return 0.0
            return float(skills.get(required.lower().strip(), 0.0))

        df["Skill_Match_Score"] = df.apply(get_skill_score, axis=1)

        # --- Drop columns not needed by the model ---
        df.drop(columns=["Hire_Date", "technical_abilities_dict", "Skill"], errors="ignore", inplace=True)

        # Drop columns starting with "skill_", except "Skill_Match_Score"
        skill_cols = [col for col in df.columns if col.startswith("skill_") and col != "Skill_Match_Score"]
        df.drop(columns=skill_cols, errors="ignore", inplace=True)
        
        try:
            # print(df.columns.tolist())  # Debug: Check dataframe columns send to model
            # print(df)
            pred = model.predict(df)[0]
            prediction_result = f"Prediction result:: {pred}"
        except Exception as e:
            prediction_result = f"Prediction error: {e}"

    return render_template("index.html", prediction_result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)
