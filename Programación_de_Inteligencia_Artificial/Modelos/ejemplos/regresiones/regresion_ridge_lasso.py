# REGRESIÖN RIDGE Y LASSO

#PASO 01. IMPORTAR LIBRERIAS
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


#PASO 02. CREAR DATOS DE EJEMPLO
# Datos sintéticos
np.random.seed(42)
X = np.random.rand(100, 5)  # 100 muestras, 5 características
y = 3 * X[:, 0] + 2 * X[:, 1] - 1.5 * X[:, 2] + np.random.randn(100) * 0.5  # Relación lineal con ruido

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#PASO 03. APLICAR REGRESIÓN LINEAL (BASE)
# Modelo de regresión lineal sin regularización
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
y_pred_lin = lin_model.predict(X_test)

# Evaluación de la regresión lineal
print("Regresión Lineal (sin regularización):")
print(f"Coeficientes: {lin_model.coef_}")
print(f"MSE: {mean_squared_error(y_test, y_pred_lin):.2f}")
print(f"R²: {r2_score(y_test, y_pred_lin):.2f}")

#PASO 04. APLICAR REGRESION RIDGE
# Modelo de regresión Ridge con regularización (alpha=1)
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train, y_train)
y_pred_ridge = ridge_model.predict(X_test)

# Evaluación de la regresión Ridge
print("\nRegresión Ridge:")
print(f"Coeficientes: {ridge_model.coef_}")
print(f"MSE: {mean_squared_error(y_test, y_pred_ridge):.2f}")
print(f"R²: {r2_score(y_test, y_pred_ridge):.2f}")


#PASO 05. APLICAR REGRESION LASSO
# Modelo de regresión Lasso con regularización (alpha=0.1)
lasso_model = Lasso(alpha=0.1)
lasso_model.fit(X_train, y_train)
y_pred_lasso = lasso_model.predict(X_test)

# Evaluación de la regresión Lasso
print("\nRegresión Lasso:")
print(f"Coeficientes: {lasso_model.coef_}")
print(f"MSE: {mean_squared_error(y_test, y_pred_lasso):.2f}")
print(f"R²: {r2_score(y_test, y_pred_lasso):.2f}")

#PASO 06. COMPARAR COEFICIENTES
plt.plot(lin_model.coef_, label='Regresión Lineal', marker='o')
plt.plot(ridge_model.coef_, label='Regresión Ridge', marker='s')
plt.plot(lasso_model.coef_, label='Regresión Lasso', marker='x')
plt.xlabel("Coeficiente de la característica")
plt.ylabel("Valor del coeficiente")
plt.title("Comparación de Coeficientes")
plt.legend()
plt.show()

# Resultados: 
# -- Regresión Lineal: Puede dar coeficientes muy grandes, lo que puede indicar sobreajuste. 
# -- Regresión Ridge: Reduce los coeficientes, pero ninguno es exactamente cero.
# -- Regresión Lasso: Algunos coeficientes pueden reducirse a exactamente cero, eliminando características innecesarias.

