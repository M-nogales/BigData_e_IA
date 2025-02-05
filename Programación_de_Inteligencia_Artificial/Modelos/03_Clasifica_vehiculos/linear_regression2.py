# REGRESION LINEAL 

#PASO 01. IMPORTAR LIBRERIAS NECESARIAS
from tkinter import Y
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#PASO 02. CREAR DATOS DE EJEMPLO
# Generar datos sintéticos
df = pd.read_csv('Dataset_Vehiculos.csv')

print('df.head(): ', df.head())

print('df.describe(): ', df.describe())
print('df.info(): ', df.info())

# Features
X = df.drop(columns=['ID', 'Price'])
# Target
y = df['Price']

# Visualizar los primeros datos
print(df.head())


#PASO 03. DIVIDIR LOS DATOS EN ENTRENAMIENTO Y PRUEBA
# Dividir en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f'Tamaño del conjunto de entrenamiento: {X_train.shape[0]} muestras')
print(f'Tamaño del conjunto de prueba: {X_test.shape[0]} muestras')


#PASO 04. CREAR Y ENTRENAR EL MODELO DE REGRESIÓN LINEAL
# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Obtener los coeficientes aprendidos
print(f'Intercepto (β0): {model.intercept_:.2f}')
print(f'Pendiente (β1): {model.coef_[0]:.2f}')


#PASO 05. REALIZAR PREDICCIONES
# Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Comparar predicciones con valores reales
resultados = pd.DataFrame({'Real': y_test, 'Predicción': y_pred})
print(resultados.head())


#PASO 06. EVALUAR EL MODELO
# Calcular métricas de rendimiento
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Error cuadrático medio (MSE): {mse:.2f}')
print(f'Raíz del error cuadrático medio (RMSE): {rmse:.2f}')
print(f'Coeficiente de determinación (R^2): {r2:.2f}')


#PASO 07. VISUALIZACIÓN DE RESULTADOS
# Graficar datos reales vs predicciones
plt.scatter(y_test, y_pred, color='blue', label='Datos reales')
plt.plot(X_test, y_pred['Price'], color='red', linewidth=2, label='Predicción (línea de regresión)')
plt.xlabel('Variable Independiente (X)')
plt.ylabel('Variable Dependiente (y)')
plt.title('Regresión Lineal: Datos reales vs Predicción')
plt.legend()
plt.show()

# plt.scatter(y_test, y_pred, color='blue', label='Real vs Predicción')
# plt.xlabel('Valores reales')
# plt.ylabel('Valores predichos')
# plt.title('Comparación entre valores reales y predichos')
# plt.legend()
# plt.show()