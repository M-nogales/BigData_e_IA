from flask import Flask, render_template, request
import json
import joblib
import pandas as pd
import numpy as np
from datetime import datetime

app = Flask(__name__)
modelo = joblib.load("trained_model.pkl")

@app.route("/", methods=["GET", "POST"])
def formulario():
    prediction_result = None

    if request.method == "POST":
        datos_formulario = request.form.to_dict()

        # --- Parsear habilidades técnicas ---
        habilidades_raw = datos_formulario.get("technical_abilities", "{}")
        try:
            habilidades_dict = json.loads(habilidades_raw)
        except json.JSONDecodeError:
            habilidades_dict = {}

        # Expandir las habilidades como columnas
        for k, v in habilidades_dict.items():
            datos_formulario[f"skill_{k.lower().strip()}"] = v

        # Guardar el dict original también
        datos_formulario["technical_abilities_dict"] = habilidades_dict

        # --- Procesar tipos numéricos y fechas ---
        processed = {}
        for key, value in datos_formulario.items():
            if key == "Hire_Date":
                try:
                    processed[key] = pd.to_datetime(value)
                except Exception:
                    processed[key] = pd.NaT
            elif isinstance(value, dict):
                processed[key] = value  # dejar como dict
            else:
                try:
                    processed[key] = float(value)
                except (ValueError, TypeError):
                    processed[key] = value


        df = pd.DataFrame([processed])

        # --- Calcular Tenure_Years ---
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

        # --- Calcular Skill_Match_Score ---
        def get_skill_score(row):
            required = row.get("Skill", "")
            skills = row.get("technical_abilities_dict", {})
            if not isinstance(required, str) or pd.isna(required) or not isinstance(skills, dict):
                return 0.0
            return float(skills.get(required.lower().strip(), 0.0))

        df["Skill_Match_Score"] = df.apply(get_skill_score, axis=1)

        # Eliminar columnas no esperadas por el modelo si hace falta
        df.drop(columns=["Hire_Date", "technical_abilities_dict"], errors="ignore", inplace=True)

        try:
            pred = modelo.predict(df)[0]
            prediction_result = f"Resultado de predicción: {pred}"
        except Exception as e:
            prediction_result = f"Error al predecir: {e}"

    return render_template("index.html", prediction_result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)
