# CLASIFICACION -- BOSQUE ALEATORIO
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
'''RandomForestClassifier: Implementación del modelo Random Forest en Scikit-Learn'''

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de Random Forest con 100 árboles
rf_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf_model.fit(X_train, y_train)
''' RandomForestClassifier: Crea un modelo de bosque aleatorio con los siguientes parámetros:
n_estimators=100: Se utilizan 100 árboles en el bosque para mejorar la precisión.
max_depth=5: Se establece una profundidad máxima de 5 para evitar sobreajuste.
random_state=42: Asegura la reproducibilidad del modelo.
fit(X_train, y_train): Entrena el modelo con los datos de entrenamiento.'''

# Realizar predicciones
y_pred = rf_model.predict(X_test)

# Evaluación del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

# Matriz de confusión y reporte de clasificación
print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Importancia de las características
feature_importances = rf_model.feature_importances_
plt.barh(iris.feature_names, feature_importances)
plt.xlabel("Importancia")
plt.ylabel("Características")
plt.title("Importancia de las características en Random Forest")
plt.show()
'''
rf_model.feature_importances_: Muestra la importancia de cada característica en la predicción del modelo.
plt.barh(): Crea un gráfico de barras horizontal que muestra qué características tienen mayor impacto en la clasificación.
iris.feature_names: Etiquetas de las características (sepal length, sepal width, petal length, petal width).
Se muestran las características ordenadas según su contribución al modelo.'''