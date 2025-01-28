# RED NEURONAL REGRESIVA

# NOTA; instalar librerías
# pip install tensorflow numpy pandas matplotlib scikit-learn
# Nota; TENSORFLOW - Python versiones 8 a 11

# PASO 01. IMPORTAR LIBRERIAS
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


# PASO 02. GENERAR DATOS SINTÉTICOS
# Generar datos de ejemplo
np.random.seed(42)
X = np.linspace(-5, 5, 500).reshape(-1, 1)
y = 3 * X**3 + 2 * X**2 - X + np.random.randn(500, 1) * 5


# PASO 03. PREPROCESAMIENTO DE DATOS
# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar los datos para mejorar la convergencia del modelo
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# PASO 04. DEFINIR MODELO DE RED NEURONAL
# Definir la arquitectura de la red neuronal
model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),
    Dense(64, activation='relu'),
    Dense(1)  # Capa de salida sin activación para regresión
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# PASO 05. ENTRENAR EL MODELO
history = model.fit(X_train_scaled, y_train, epochs=200, validation_data=(X_test_scaled, y_test), verbose=0)

# Graficar la pérdida durante el entrenamiento
plt.plot(history.history['loss'], label='Entrenamiento')
plt.plot(history.history['val_loss'], label='Validación')
plt.xlabel('Épocas')
plt.ylabel('Pérdida (MSE)')
plt.legend()
plt.title('Evolución de la pérdida')
plt.show()


# PASO 06. EVALUAR MODELO
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)

print(f'Error cuadrático medio (MSE): {mse:.2f}')

