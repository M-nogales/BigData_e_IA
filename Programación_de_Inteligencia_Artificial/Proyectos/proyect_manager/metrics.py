import joblib
import pandas as pd
import numpy as np

# Cargar el modelo
modelo = joblib.load("trained_model.pkl")

# Obtener los nombres de las columnas (si el modelo es parte de un Pipeline)
if hasattr(modelo, "named_steps") and "preprocessor" in modelo.named_steps:
    try:
        preprocessor = modelo.named_steps["preprocessor"]
        columnas = preprocessor.get_feature_names_out()
        logistic = modelo.named_steps["classifier"]  # Ajusta esto si tu step no se llama "classifier"
    except Exception as e:
        print(f"Error obteniendo columnas del preprocessor: {e}")
        columnas = [f"Feature_{i}" for i in range(modelo.named_steps['classifier'].coef_.shape[1])]
        logistic = modelo.named_steps["classifier"]
elif hasattr(modelo, "coef_"):
    logistic = modelo
    columnas = getattr(modelo, "feature_names_in_", [f"Feature_{i}" for i in range(modelo.coef_.shape[1])])
else:
    raise ValueError("El modelo cargado no es una regresión logística válida.")

# Obtener coeficientes
coeficientes = logistic.coef_[0]  # Para binaria
importancia_df = pd.DataFrame({
    "Feature": columnas,
    "Coefficient": coeficientes,
    "Abs_Coefficient": np.abs(coeficientes)
}).sort_values(by="Abs_Coefficient", ascending=False)

print("\n=== IMPORTANCIA DE VARIABLES (REGRESIÓN LOGÍSTICA) ===")
print(importancia_df[["Feature", "Coefficient"]].to_string(index=False))
