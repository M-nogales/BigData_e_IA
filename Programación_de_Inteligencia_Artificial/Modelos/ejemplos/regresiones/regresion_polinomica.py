# REGRESIÓN POLINÓMICA

#PASO 01. IMPORTAR LIBRERIAS
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

#PASO 02. CREAR DATOS DE EJEMPLO
# Generar datos simulados
np.random.seed(42)
X = np.linspace(-5, 5, 100).reshape(-1, 1)
y = 3 * X**2 + 2 * X + np.random.randn(100, 1) * 5  # Relación cuadrática con ruido

# Visualizar los datos
plt.scatter(X, y, color='blue', label='Datos reales')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Datos de ejemplo para regresión polinómica')
plt.legend()
plt.show()

#PASO 03. APLICAR REGRESION LINEAL COMO BASE
# Aplicar regresión lineal para comparar
linear_model = LinearRegression()
linear_model.fit(X, y)
y_pred_linear = linear_model.predict(X)

# Visualizar los resultados de la regresión lineal
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, y_pred_linear, color='red', label='Regresión Lineal')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresión Lineal vs. Datos Reales')
plt.legend()
plt.show()

#NOTA; La regresión lineal no es suficiente para capturar la forma cuadrática de los datos ..... 

#PASO 04. APLICAR REGRESIÓN POLINÓMICA
# Transformar las características a un polinomio de grado 2
poly = PolynomialFeatures(degree=2)  # Cambiar el grado según necesidad
X_poly = poly.fit_transform(X)

# Ajustar el modelo de regresión polinómica
poly_model = LinearRegression()
poly_model.fit(X_poly, y)

# Hacer predicciones
y_pred_poly = poly_model.predict(X_poly)

# Visualización de la regresión polinómica
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, y_pred_poly, color='green', label='Regresión Polinómica (grado 2)')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresión Polinómica vs. Datos Reales')
plt.legend()
plt.show()

#PASO 05. EVALUACIÓN DEL MODELO
# Evaluación de la regresión lineal
print("Evaluación de la Regresión Lineal:")
print(f"MSE: {mean_squared_error(y, y_pred_linear):.2f}")
print(f"R^2: {r2_score(y, y_pred_linear):.2f}")

# Evaluación de la regresión polinómica
print("\nEvaluación de la Regresión Polinómica (grado 2):")
print(f"MSE: {mean_squared_error(y, y_pred_poly):.2f}")
print(f"R^2: {r2_score(y, y_pred_poly):.2f}")

#NOTA; Un menor MSE (Error Cuadrático Medio) indica que el modelo predice con mayor precisión. 
#      Un valor más alto de R^2 (cercano a 1) indica que el modelo explica mejor la variabilidad de los datos.

#PASO 06. PREDICCIÓN DE NUEVOS VALORES
# Predicción para nuevos valores
X_new = np.array([[6]])
X_new_poly = poly.transform(X_new)
prediction = poly_model.predict(X_new_poly)

print(f'Predicción para X=6: {prediction[0][0]:.2f}')

