import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score, recall_score, roc_auc_score


iris = load_iris()
X = iris.data
y = iris.target

# Dividir los datos en entrenamiento y prueba (80% - 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar los datos para evitar influencia de escalas
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Modelo KNN con k=5 
# K = número de vecinos a considerar, por defecto es 5, 
# al ser un dataset pequeño y balanceado no tiene grán inportancia en el resultado
knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knn.fit(X_train, y_train)

# Predictions
y_pred = knn.predict(X_test)
y_pred_prob = knn.predict_proba(X_test)

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
target_names = ['setosa', 'versicolor', 'virginica']
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=target_names))

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

metrics_result_comparation(accuracy, recall, f1, auc_roc, model = 'knn')