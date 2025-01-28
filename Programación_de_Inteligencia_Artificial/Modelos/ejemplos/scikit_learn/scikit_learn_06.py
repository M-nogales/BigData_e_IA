# CLASIFICACIÓN -- ANN (Redes Neuronales)
import tensorflow as tf # Tensorflow compatible con versiones Python 3.8 a 3.11 (tengo 3.13)
from tensorflow import keras
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np

# Cargar datos Iris
iris = load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Codificación one-hot de la variable objetivo
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y)

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Definir el modelo ANN
model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(4,), activation='relu'),
    keras.layers.Dense(8, activation='relu'),
    keras.layers.Dense(3, activation='softmax')
])
##
'''Se define una red neuronal con la arquitectura siguiente:

Capa de entrada:
Dense(10, input_shape=(4,), activation='relu')
10 neuronas, activación ReLU, 4 entradas correspondientes a las características del dataset.

Capa oculta:
Dense(8, activation='relu')
8 neuronas, activación ReLU para capturar patrones complejos.

Capa de salida:
Dense(3, activation='softmax')
3 neuronas de salida (una por clase), activación softmax para generar probabilidades.
'''
##

# Compilar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
##
'''
Optimizador; adam: Optimizador eficiente basado en gradientes adaptativos, adecuado para redes neuronales profundas.
Función de pérdida; categorical_crossentropy: Se usa para problemas de clasificación multiclase con etiquetas codificadas en one-hot.
Métrica; accuracy: Proporción de predicciones correctas sobre el total.'''
##

# Entrenar el modelo
model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1)
##
'''
X_train, y_train: Datos de entrenamiento.
epochs=50: Número de veces que el modelo verá el conjunto completo de datos.
batch_size=8: Número de muestras procesadas antes de actualizar los pesos.
verbose=1: Muestra información sobre el proceso de entrenamiento.'''
##

# Evaluar el modelo
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Precisión del modelo: {accuracy:.2f}')
##
'''evaluate(X_test, y_test): Evalúa el modelo con los datos de prueba para medir su rendimiento.
Se obtiene:
loss: Pérdida total en los datos de prueba.
accuracy: Precisión del modelo.'''
##