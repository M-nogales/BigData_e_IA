# CLASIFICACION - SVM
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
##
'''
numpy: Manipulación numérica y generación de datos para visualización.
matplotlib.pyplot: Visualización de datos, incluyendo la frontera de decisión.
datasets: Permite cargar conjuntos de datos como Iris.
train_test_split: Para dividir datos en entrenamiento y prueba.
StandardScaler: Normaliza los datos para mejorar la eficiencia del modelo SVM.
SVC: Implementación de Support Vector Classification de Scikit-Learn.
accuracy_score, confusion_matrix, classification_report: Métricas de evaluación del modelo.
'''
##

# Cargar el conjunto de datos Iris
iris = datasets.load_iris()
X = iris.data[:, :2]  # Tomamos solo dos características para visualización
y = iris.target
##
'''
iris = datasets.load_iris(): Carga el conjunto de datos Iris.
X = iris.data[:, :2]: Se toman solo las dos primeras características (longitud y ancho del sépalo) para facilitar la visualización en 2D.
y = iris.target: Etiquetas de clase, que contienen tres categorías (Setosa, Versicolor, Virginica).
'''
##

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
##
'''
Divide los datos en:
80% entrenamiento (X_train, y_train).
20% prueba (X_test, y_test).
random_state=42: Garantiza la reproducibilidad de la partición.'''
##

# Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
##
'''
fit_transform: Calcula estadísticas de normalización y transforma los datos de entrenamiento.
transform: Aplica la transformación aprendida a los datos de prueba.

SVM es sensible a la escala de las características, por lo que la normalización ayuda a mejorar el rendimiento.
'''
##

# Crear y entrenar el modelo SVM con kernel RBF
model = SVC(kernel='rbf', C=1.0, gamma='scale')
model.fit(X_train, y_train)
##
'''
SVC: Se usa la implementación de clasificación de SVM.
Parámetros:
kernel='rbf': Se emplea un kernel radial base function (RBF), ideal para datos no linealmente separables.
C=1.0: Parámetro de regularización, controla la penalización de errores (mayor valor = menor margen y mayor precisión en el entrenamiento).
gamma='scale': Controla la influencia de un solo punto de entrenamiento (valor automático basado en las características).
'''
##

# Predicción sobre el conjunto de prueba
y_pred = model.predict(X_test)
##
''' Se realiza la predicción de las clases para los datos de prueba. '''
##

# Evaluación del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')
##
''' accuracy_score: Calcula la proporción de predicciones correctas sobre el total.'''
##

# Matriz de confusión y reporte de clasificación
print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
##
'''La matriz de confusión muestra la relación entre predicciones correctas e incorrectas en cada clase.'''
'''El reporte muestra métricas clave para cada clase.
Precisión (Precision): Qué tan precisa es la predicción para cada clase.
Recall (Sensibilidad): Qué proporción de instancias positivas se identificaron correctamente.
F1-score: Promedio ponderado entre precisión y recall.
Soporte: Número de muestras de cada clase.'''
##

# Visualización de la frontera de decisión
def plot_decision_boundary(X, y, model):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k')
    plt.title('Frontera de decisión con SVM')
    plt.show()

plot_decision_boundary(X_test, y_test, model)

##
'''
Definición de los límites: Se define un espacio de valores entre los mínimos y máximos de las dos características seleccionadas.
Malla de predicciones:Se predicen los valores en cada punto de la malla y se reconfiguran para su representación gráfica.
Visualización:
contourf: Muestra las regiones de decisión con colores diferenciados.
scatter: Representa las muestras reales con diferentes colores.
'''
##