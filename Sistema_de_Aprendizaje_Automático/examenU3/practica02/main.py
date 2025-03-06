import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

# 1. Carga y exploración de datos
print("Cargando el dataset Boston Housing...")
boston = fetch_openml(name='boston', version=1, as_frame=True)
X = boston.data[['RM', 'LSTAT']]
y = boston.target
print(X.head())

# 2. Preprocesamiento de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Construcción del Modelo de Regresión Lineal
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred_lin = lin_reg.predict(X_test)

# 4. Evaluación del modelo de Regresión Lineal
mse_lin = mean_squared_error(y_test, y_pred_lin)
r2_lin = r2_score(y_test, y_pred_lin)
print(f"Regresión Lineal - MSE: {mse_lin:.4f}, R2: {r2_lin:.4f}")

# 5. Comparación con Regresión Ridge
ridge_reg = Ridge(alpha=1.0)
ridge_reg.fit(X_train, y_train)
y_pred_ridge = ridge_reg.predict(X_test)

mse_ridge = mean_squared_error(y_test, y_pred_ridge)
r2_ridge = r2_score(y_test, y_pred_ridge)
print(f"Regresión Ridge - MSE: {mse_ridge:.4f}, R2: {r2_ridge:.4f}")

# 6. Comparación con Regresión Lasso
lasso_reg = Lasso(alpha=1.0)
lasso_reg.fit(X_train, y_train)
y_pred_lasso = lasso_reg.predict(X_test)

mse_lasso = mean_squared_error(y_test, y_pred_lasso)
r2_lasso = r2_score(y_test, y_pred_lasso)
print(f"Regresión Lasso - MSE: {mse_lasso:.4f}, R2: {r2_lasso:.4f}")
print("Si los valores de las regresiones son muy similares graficamente se pisan unos a otros")

# Visualización de Predicciones vs Valores Reales
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred_lin, label='Regresión Lineal', alpha=0.6)
plt.scatter(y_test, y_pred_ridge, label='Regresión Ridge', alpha=0.6, color='r')
plt.scatter(y_test, y_pred_lasso, label='Regresión Lasso', alpha=0.6, color='g')
## Linea perfecta para visualización
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '--k')
plt.xlabel("Valores Reales")
plt.ylabel("Predicciones")
plt.title("Comparación de Modelos")
plt.legend()
plt.grid()
plt.show()