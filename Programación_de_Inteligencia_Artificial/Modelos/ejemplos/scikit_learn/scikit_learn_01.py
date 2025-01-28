# CLASIFICACION - REGRESIóN LOGíSTICA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_iris
##
'''
numpy y pandas: Para manipulación y análisis de datos.
matplotlib.pyplot: Para visualización de datos.
train_test_split: Para dividir los datos en entrenamiento y prueba.
StandardScaler: Para normalizar las características.
LogisticRegression: Implementación del modelo de regresión logística.
accuracy_score, confusion_matrix, classification_report: Métricas para evaluar el rendimiento del modelo.
load_iris: Para cargar el conjunto de datos de flores Iris.
'''
##


# Cargar el dataset Iris
iris = load_iris()
X = iris.data  # Variables de entrada
y = (iris.target == 0).astype(int)  # Convertimos a problema binario: Iris Setosa vs No Setosa
##
'''
iris.data: Contiene cuatro características (longitud y ancho de sépalo y pétalo).
iris.target: Contiene las clases (0: Setosa, 1: Versicolor, 2: Virginica).
y = (iris.target == 0).astype(int): Convierte el problema en clasificación binaria:
Clase 1 para Iris Setosa (cuando iris.target == 0).
Clase 0 para No Setosa (cuando iris.target es 1 o 2).
'''
##

# Dividir en conjunto de entrenamiento y prueba (80% - 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
##
'''
Divide el dataset en:
80% para entrenamiento (X_train, y_train).
20% para prueba (X_test, y_test).
random_state=42: Garantiza la reproducibilidad de la división.
'''
##

# Normalizar los datos (es recomendable para mejorar el rendimiento)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
##
'''
La normalización estandariza los datos restando la media y dividiendo por la desviación estándar.
fit_transform(X_train): Calcula estadísticas y transforma los datos de entrenamiento.
transform(X_test): Usa los mismos parámetros para transformar el conjunto de prueba.
Motivo de normalizar: La regresión logística es sensible a escalas de magnitud, y la normalización mejora la convergencia del modelo.
'''
##

# Inicializar y entrenar el modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)
##
'''
Se crea un modelo de regresión logística con los parámetros por defecto.
fit(): Ajusta el modelo a los datos de entrenamiento.
'''
##

# Predicción sobre el conjunto de prueba
y_pred = model.predict(X_test)
##
'''
Se predicen las clases para los datos de prueba utilizando el modelo entrenado.
'''
##

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')
##
'''
accuracy_score: Calcula la precisión (proporción de predicciones correctas sobre el total).
Se imprime la precisión con dos decimales.
'''
##

# Matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de confusión:")
print(conf_matrix)
##
'''
La matriz de confusión muestra el número de predicciones correctas e incorrectas
Filas: Clases reales.
Columnas: Clases predichas.

Ejemplo de matriz de confusión:
(TP  FN
FP  TN)

Donde:

TP: Verdaderos Positivos (correctamente predicho como Setosa).
FN: Falsos Negativos (Setosa predicha como No Setosa).
FP: Falsos Positivos (No Setosa predicha como Setosa).
TN: Verdaderos Negativos (correctamente predicho como No Setosa).
'''
##

# Reporte de clasificación
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=['No Setosa', 'Setosa']))
##
'''
classification_report proporciona las siguientes métricas:
Precisión (Precision): TP / (TP + FP) (Proporción de predicciones correctas sobre las realizadas).
Recall (Sensibilidad): TP / (TP + FN) (Proporción de positivos correctamente identificados).
F1-score: Media armónica entre precisión y recall.
Soporte: Número de muestras en cada clase.'''
##

# Visualización de la distribución de predicciones
plt.figure(figsize=(6, 4))
plt.bar(['No Setosa', 'Setosa'], np.bincount(y_pred))
plt.xlabel('Clase Predicha')
plt.ylabel('Frecuencia')
plt.title('Distribución de Predicciones')
plt.show()
##
'''
np.bincount(y_pred): Cuenta las predicciones para cada clase.
Se genera un gráfico de barras para visualizar la distribución de predicciones.
'''
##
