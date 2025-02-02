import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score, recall_score, roc_auc_score
'''
numpy: Manipulación numérica y generación de datos para visualización.
matplotlib.pyplot: Visualización de datos, incluyendo la frontera de decisión.
datasets: Permite cargar conjuntos de datos como Iris.
train_test_split: Para dividir datos en entrenamiento y prueba.
StandardScaler: Normaliza los datos para mejorar la eficiencia del modelo SVM.
SVC: Implementación de Support Vector Classification de Scikit-Learn.
accuracy_score, confusion_matrix, classification_report: Métricas de evaluación del modelo.
'''

# Load the dataset and check the first rows and some info
health = pd.read_csv('./Dataset_Academico.csv')
health.info()
print(health.head())

mapping = {'Bajo': 1, 'Medio': 2, 'Alto': 3}
health['rendimiento_academico'] = health['rendimiento_academico'].map(mapping)
# Features is the input data, the columns that will be used to make predictions.
# Target variable is the output data, the column that will be predicted.
# Features:
X = health[['edad','genero','horas_estudio','asistencia','nivel_socioeconomico','acceso_internet','actividades_extracurriculares','estado_emocional','nota_promedio_anterior','apoyo_familiar']]
# Target:
y = health['rendimiento_academico']

# Split data into training and test sets
# 20% of the data will be used for testing, 80% for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Data normalization
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# train the SVM model
model = SVC(kernel='rbf', C=1.0, probability=True, gamma='scale',class_weight='balanced')
model.fit(X_train, y_train)

'''
SVC: Se usa la implementación de clasificación de SVM.
Parámetros:
kernel='rbf': Se emplea un kernel radial base function (RBF), ideal para datos no linealmente separables.
C=1.0: Parámetro de regularización, controla la penalización de errores (mayor valor = menor margen y mayor precisión en el entrenamiento).
gamma='scale': Controla la influencia de un solo punto de entrenamiento (valor automático basado en las características).
#! probability=True: Enable the probability estimates, needed for AUC-ROC calculation.
'''


# Predictions
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)
'''
print(y_pred_prob) =
[0.         0.90883978 0.09116022]
[low, medium, high]
'''

# Evaluación del modelo
print("confussion matrix:")
print(confusion_matrix(y_test, y_pred))

accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')
auc_roc = roc_auc_score(y_test, y_pred_prob, multi_class='ovr')

# Results
print(f"🔹 Accuracy: {accuracy:.2f}")
print(f"🔹 Recall: {recall:.2f}")
print(f"🔹 F1-Score: {f1:.2f}")
print(f"🔹 AUC-ROC: {auc_roc:.2f}")

# Report
target_names = ['low', 'medium', 'high']
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=target_names))

'''
Definición de los límites: Se define un espacio de valores entre los mínimos y máximos de las dos características seleccionadas.
Malla de predicciones:Se predicen los valores en cada punto de la malla y se reconfiguran para su representación gráfica.
Visualización:
contourf: Muestra las regiones de decisión con colores diferenciados.
scatter: Representa las muestras reales con diferentes colores.
'''

# Metrics comparation
def metrics_result_comparation(accuracy, recall, f1, auc_roc, model):
    metrics = ['Accuracy', 'Recall', 'F1-Score', 'AUC-ROC']
    values = [accuracy, recall, f1, auc_roc]
    
    # Create a bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(metrics, values, color=['blue', 'green', 'orange', 'red'])
    
    # Add value labels on top of bars
    for i, v in enumerate(values):
        plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontsize=12, fontweight='bold')
    
    # Labels and title
    plt.ylim(0, 1.1)
    plt.ylabel('Score')
    plt.title('Model Performance Metrics - '+ model)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Show the plot
    plt.show()

metrics_result_comparation(accuracy, recall, f1, auc_roc, model = 'SVM')

# Visualización de la frontera de decisión
# def plot_decision_boundary(X, y, model):
#     x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
#     y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
#     xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
#                          np.linspace(y_min, y_max, 200))
#     Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
#     Z = Z.reshape(xx.shape)
#     plt.contourf(xx, yy, Z, alpha=0.3)
#     plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k')
#     plt.title('Frontera de decisión con SVM')
#     plt.show()

# plot_decision_boundary(X_test, y_test, model)