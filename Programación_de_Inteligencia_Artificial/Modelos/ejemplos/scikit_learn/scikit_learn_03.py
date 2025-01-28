# CLASIFICACION - KNN
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

##
'''
KNeighborsClassifier: Implementación del algoritmo KNN de Scikit-Learn.
'''
##

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir los datos en entrenamiento y prueba (80% - 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar los datos para evitar influencia de escalas
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear el modelo KNN con k=5 vecinos
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(X_train, y_train)
##
'''
KNeighborsClassifier: Se crea el modelo KNN con los siguientes parámetros:
n_neighbors=5: Considera los 5 vecinos más cercanos para clasificar.
metric='euclidean': Se usa la distancia Euclidiana como métrica de distancia.
fit(X_train, y_train): Entrena el modelo con los datos normalizados de entrenamiento.
'''
##

# Realizar predicciones
y_pred = knn.predict(X_test)
##
'''predict(X_test): Se utilizan los datos de prueba para predecir las clases de las flores.'''
##

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

# Mostrar matriz de confusión y reporte de clasificación
print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

##
'''confusion_matrix(y_test, y_pred): Genera la matriz de confusión, que muestra el número de predicciones correctas e incorrectas para cada clase.
La diagonal principal indica las predicciones correctas.
Valores fuera de la diagonal indican errores de clasificación.
'''
##
