# CLASIFICACION - áRBOL DE DECISIóN

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
##
'''
DecisionTreeClassifier: Modelo de clasificación basado en árboles de decisión.
plot_tree: Visualización gráfica del árbol de decisión entrenado.'''
##

# Cargar el conjunto de datos Iris
health = pd.read_csv('./Dataset_Enfermedades.csv')
health.info()
print(health.head())

X = health[['edad','sexo','presion_sistolica','presion_diastolica','colesterol','glucosa','indice_masa_corporal','actividad_fisica','fumar','historia_familiar','diabetes']]
y = health['enfermedad_cardiaca']

# Dividir los datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de Árbol de Decisión
tree_clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
tree_clf.fit(X_train, y_train)
##
'''Se crea el modelo de árbol de decisión con los siguientes parámetros:
criterion='gini': Utiliza el índice de Gini como criterio de evaluación para dividir nodos (mide la impureza de los nodos).
max_depth=3: Limita la profundidad del árbol a 3 niveles para evitar sobreajuste.
random_state=42: Garantiza la reproducibilidad.
fit(X_train, y_train): Entrena el modelo utilizando los datos de entrenamiento.'''
##

# Predicción
y_pred = tree_clf.predict(X_test)
'''predict(X_test): Se predicen las etiquetas para los datos de prueba'''

# Evaluación del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

# Matriz de confusión y reporte de clasificación
print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))
print()
target_names = ['Clase 0', 'Clase 1']
print('target_name: ', target_names)
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Visualización del árbol de decisión
plt.figure(figsize=(12, 8))
feature_names=['edad','sexo','presion_sistolica','presion_diastolica','colesterol','glucosa','indice_masa_corporal','actividad_fisica','fumar','historia_familiar','diabetes']
plot_tree(tree_clf, feature_names=feature_names, class_names=target_names, filled=True)
plt.title("Árbol de Decisión - Clasificación")
plt.show()
##
'''
plt.figure(figsize=(12, 8)): Define el tamaño de la figura para mejorar la visualización.

plot_tree: Grafica el árbol de decisión entrenado, mostrando:
feature_names: Nombres de las características de entrada.
class_names: Nombres de las clases de salida (Setosa, Versicolor, Virginica).
filled=True: Colorea los nodos según la clase predominante.
'''
##
