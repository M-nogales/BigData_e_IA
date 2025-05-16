from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Cargar el modelo al iniciar la app
model = joblib.load('model_pipeline.pkl')

# Definir las columnas de entrada en el mismo orden que X_train
# Asegúrate de listar aquí todas tus columnas de características:
FEATURE_COLUMNS = [
    'Age', 'Years_At_Company', 'Performance_Score', 'Monthly_Salary',
    'Work_Hours_Per_Week', 'Projects_Handled', 'Overtime_Hours',
    'Sick_Days', 'Remote_Work_Frequency', 'Team_Size', 'Training_Hours',
    'Promotions', 'Employee_Satisfaction_Score', 'Tenure_Years', 'Skill_Match_Score',
    'Department', 'Gender', 'Job_Title', 'Education_Level', 'Category'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # data debe ser un dict con keys = FEATURE_COLUMNS y valores escalares
        df = pd.DataFrame([data], columns=FEATURE_COLUMNS)

        # Predecir probabilidad y clase
        proba = model.predict_proba(df)[0, 1]
        pred = int(model.predict(df)[0])

        return jsonify({
            'prediction': pred,
            'probability': float(proba)
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)