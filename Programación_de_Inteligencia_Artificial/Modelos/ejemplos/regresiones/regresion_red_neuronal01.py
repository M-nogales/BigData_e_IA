# REGRESION RED NEURONAL (necesario tensorflow)
## pip install tensorflow numpy pandas matplotlib scikit-learn

# PASO 01. IMPORTAR LIBRERIAS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error


# PASO 02. CREACION DATOS DE EJEMPLO
# Generación de datos sintéticos para regresión
np.random.seed(42)
X = np.linspace(0, 10, 200).reshape(-1, 1)  # Característica independiente
y = 3 * X[:, 0]**2 + 2 * X[:, 0] + np.random.randn(200) * 10  # Relación cuadrática con ruido

# Convertir a DataFrame para manipulación
df = pd.DataFrame({'X': X.flatten(), 'y': y})
plt.scatter(df['X'], df['y'], color='blue', label='Datos reales')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Datos de ejemplo para regresión con redes neuronales')
plt.legend()
plt.show()


# PASO 03. PREPROCESAMIENTO DE LOS DATOS
# División en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalización de los datos para mejorar el entrenamiento
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# PASO 04. CONSTRUIR MODELO DE RED NEURONAL
# Definir la arquitectura del modelo
model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),  # Capa oculta con 64 neuronas y activación ReLU
    Dense(32, activation='relu'),  # Capa oculta adicional
    Dense(1, activation='linear')  # Capa de salida para regresión
])

# Compilar el modelo con función de pérdida MSE y optimizador Adam
model.compile(optimizer=Adam(learning_rate=0.01), loss='mse', metrics=['mae'])

# Resumen del modelo
model.summary()



# PASO 05. ENTRENAR MODELO
# Entrenamiento del modelo con los datos de entrenamiento
history = model.fit(X_train_scaled, y_train, validation_data=(X_test_scaled, y_test), 
                    epochs=200, batch_size=16, verbose=1)

# Graficar la pérdida durante el entrenamiento
plt.plot(history.history['loss'], label='Pérdida en entrenamiento')
plt.plot(history.history['val_loss'], label='Pérdida en validación')
plt.xlabel('Épocas')
plt.ylabel('Pérdida (MSE)')
plt.title('Evolución de la pérdida durante el entrenamiento')
plt.legend()
plt.show()



# PASO 06. EVALUAR MODELO
# Evaluación del modelo en el conjunto de prueba
y_pred = model.predict(X_test_scaled)

# Calcular métricas de rendimiento
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f'Error Cuadrático Medio (MSE): {mse:.2f}')
print(f'Error Absoluto Medio (MAE): {mae:.2f}')

# Visualización de los resultados
plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.scatter(X_test, y_pred, color='red', label='Predicciones de la red neuronal')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Comparación de predicciones y datos reales')
plt.legend()
plt.show()



# PASO 07. PREDICCION NUEVOS VALORES
# Predicción para nuevos datos
X_new = np.array([[12]])  # Nuevo valor a predecir
X_new_scaled = scaler.transform(X_new)
y_new_pred = model.predict(X_new_scaled)

print(f'Predicción para X=12: {y_new_pred[0][0]:.2f}')



