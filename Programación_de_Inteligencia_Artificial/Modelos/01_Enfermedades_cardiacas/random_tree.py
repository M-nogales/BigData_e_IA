import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score, recall_score, roc_auc_score


# Load the dataset and check the first rows and some info
health = pd.read_csv('./Dataset_Enfermedades.csv')
health.info()
print(health.head())

X = health[['edad','sexo','presion_sistolica','presion_diastolica','colesterol','glucosa','indice_masa_corporal','actividad_fisica','fumar','historia_familiar','diabetes']]
y = health['enfermedad_cardiaca']

# Split data into training and test sets
# 20% of the data will be used for testing, 80% for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the Random Forest model with 100 trees
rf_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf_model.fit(X_train, y_train)
''' RandomForestClassifier: Crea un modelo de bosque aleatorio con los siguientes parámetros:
n_estimators=100: Se utilizan 100 árboles en el bosque para mejorar la precisión.
max_depth=5: Se establece una profundidad máxima de 5 para evitar sobreajuste.
random_state=42: Asegura la reproducibilidad del modelo.
fit(X_train, y_train): Entrena el modelo con los datos de entrenamiento.'''

# predictions
y_pred = rf_model.predict(X_test)
y_pred_prob = rf_model.predict_proba(X_test)[:, 1]

# model evaluation
print("confussion matrix:")
print(confusion_matrix(y_test, y_pred))

accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc_roc = roc_auc_score(y_test, y_pred_prob)

# Results
print(f"🔹 Accuracy: {accuracy:.2f}")
print(f"🔹 Recall: {recall:.2f}")
print(f"🔹 F1-Score: {f1:.2f}")
print(f"🔹 AUC-ROC: {auc_roc:.2f}")

# Report
target_names = ['Prob no desease', 'Prob desease']
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=target_names))

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

metrics_result_comparation(accuracy, recall, f1, auc_roc, model = 'Logistic Regression')

# Importancia de las características
feature_names=['edad','sexo','presion_sistolica','presion_diastolica','colesterol','glucosa','indice_masa_corporal','actividad_fisica','fumar','historia_familiar','diabetes']
feature_importances = rf_model.feature_importances_
plt.barh(feature_names, feature_importances)
plt.xlabel("Importancia")
plt.ylabel("Características")
plt.title("Importancia de las características en Random Forest")
plt.show()
'''
rf_model.feature_importances_: Muestra la importancia de cada característica en la predicción del modelo.
plt.barh(): Crea un gráfico de barras horizontal que muestra qué características tienen mayor impacto en la clasificación.
iris.feature_names: Etiquetas de las características (sepal length, sepal width, petal length, petal width).
Se muestran las características ordenadas según su contribución al modelo.'''