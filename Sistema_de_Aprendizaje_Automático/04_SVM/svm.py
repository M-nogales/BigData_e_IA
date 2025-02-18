from matplotlib import pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, recall_score, roc_auc_score

# load data
data = pd.read_csv('fraude_data.csv')

fraude = data['Fraude'].value_counts()
print(fraude)

# features and targets
X = data.drop([ 'Fraude'], axis=1)
y = data['Fraude']

# split the data between training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# create the standard scaler to normalize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#create the SVM model
svm_model = SVC(kernel='rbf', C=1.0, probability=True, gamma='scale', class_weight='balanced')
svm_model.fit(X_train, y_train)

# Predictions
y_pred = svm_model.predict(X_test)
y_pred_prob = svm_model.predict_proba(X_test)[:, 1]

# Model evaluation
print("🔹 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Calculate the metrics
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc_roc = roc_auc_score(y_test, y_pred_prob)

# Results
print(f"🔹 Accuracy: {accuracy:.2f}")
print(f"🔹 Recall: {recall:.2f}")
print(f"🔹 F1-Score: {f1:.2f}")
print(f"🔹 AUC-ROC: {auc_roc:.2f}")

# Classification Report
target_names = ['Legitimate', 'Fraudulent']
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=target_names))

def metrics_result_comparation(accuracy, recall, f1, auc_roc, model):
    metrics = ['Accuracy', 'Recall', 'F1-Score', 'AUC-ROC']
    values = [accuracy, recall, f1, auc_roc]
    
    plt.figure(figsize=(8, 6))
    plt.bar(metrics, values, color=['blue', 'green', 'orange', 'red'])
    
    for i, v in enumerate(values):
        plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontsize=12, fontweight='bold')
    
    plt.ylim(0, 1.1)
    plt.ylabel('Score')
    plt.title(f'Model Performance Metrics - {model}')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

metrics_result_comparation(accuracy, recall, f1, auc_roc, model='SVM')