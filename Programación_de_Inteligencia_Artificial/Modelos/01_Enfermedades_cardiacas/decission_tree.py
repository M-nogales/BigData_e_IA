import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, recall_score, roc_auc_score

'''
DecisionTreeClassifier: classification model based on decision trees.
plot_tree: graphic visualization of the decision tree created.'''

# Load the dataset and check the first rows and some info
health = pd.read_csv('./Dataset_Enfermedades.csv')
health.info()
print(health.head())

# Features is the input data, the columns that will be used to make predictions.
# Target variable is the output data, the column that will be predicted.
# Features:
X = health[['edad','sexo','presion_sistolica','presion_diastolica','colesterol','glucosa','indice_masa_corporal','actividad_fisica','fumar','historia_familiar','diabetes']]
# Target:
y = health['enfermedad_cardiaca']

# Split data into training and test sets
# 20% of the data will be used for testing, 80% for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the Decision Tree model
tree_clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
# example using all the parameters
# tree_clf = DecisionTreeClassifier(
#     criterion='entropy', #gini, entropy
#     max_depth=6,  # Limit the depth of the tree
#     min_samples_split=10,  # Minimum samples required to split a node
#     min_samples_leaf=5,  # Minimum samples required to be at a leaf node
#     class_weight='balanced',  # Handle class imbalance
#     max_features='sqrt',  # Consider only a subset of features at each split
#     random_state=42,  # For reproducibility
#     min_impurity_decrease=0.01,  # Minimum impurity decrease for a split
#     ccp_alpha=0.01  # Prune tree if needed
# )

tree_clf.fit(X_train, y_train)

# Predictions
y_pred = tree_clf.predict(X_test)
y_pred_prob = tree_clf.predict_proba(X_test)[:, 1]
'''predict(X_test): Se predicen las etiquetas para los datos de prueba'''

# Model evaluation
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
    plt.title('Model Performance Metrics - ' + model)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Show the plot
    plt.show()

metrics_result_comparation(accuracy, recall, f1, auc_roc, model = 'Decision Tree')

# Decision tree visualization
plt.figure(figsize=(12, 8))
feature_names=['edad','sexo','presion_sistolica','presion_diastolica','colesterol','glucosa','indice_masa_corporal','actividad_fisica','fumar','historia_familiar','diabetes']
plot_tree(tree_clf, feature_names=feature_names, class_names=target_names, filled=True)
plt.title("Árbol de Decisión - Clasificación")
plt.show()

'''
plt.figure(figsize=(12, 8)): Define el tamaño de la figura para mejorar la visualización.
plot_tree: Grafica el árbol de decisión entrenado, mostrando:
feature_names: Nombres de las características de entrada.
class_names: Nombres de las clases de salida (no desease, desease).
filled=True: Colorea los nodos según la clase predominante.
'''