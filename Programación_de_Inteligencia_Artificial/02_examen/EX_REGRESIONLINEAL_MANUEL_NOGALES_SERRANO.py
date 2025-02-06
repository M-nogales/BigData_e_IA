import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)

# Features:
X = np.random.rand(100, 1) * 10  # 100 muestras, valores entre 0 y 10
# Target:
y = 3 * X + 7 + np.random.randn(100, 1) * 2  # y = 3x + 7 + ruido

# Convertir a DataFrame para mejor manipulación
df = pd.DataFrame(np.hstack((X, y)), columns=['X', 'y'])

# Visualizar los primeros datos
print(df.head())


# Dividir en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(df[['X']], df['y'], test_size=0.2, random_state=42)

print(f'Tamaño del conjunto de entrenamiento: {X_train.shape[0]} muestras')
print(f'Tamaño del conjunto de prueba: {X_test.shape[0]} muestras')


# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)


# Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Comparar predicciones con valores reales
resultados = pd.DataFrame({'Real': y_test, 'Predicción': y_pred})
print(resultados.head())


# Calcular métricas de rendimiento
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Error cuadrático medio (MSE): {mse:.2f}')
print(f'Raíz del error cuadrático medio (RMSE): {rmse:.2f}')
print(f'Coeficiente de determinación (R^2): {r2:.2f}')


# Graficar datos reales vs predicciones
plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicción (línea de regresión)')
plt.xlabel('Variable Independiente (X)')
plt.ylabel('Variable Dependiente (y)')
plt.title('Regresión Lineal: Datos reales vs Predicción')
plt.legend()
plt.show()

