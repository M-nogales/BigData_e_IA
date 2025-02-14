import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, recall_score, roc_auc_score

# Load the data
data = pd.read_csv('spam_detection_data.csv')

# Check class distribution
print("Class Distribution in Dataset:")
print(data['Spam'].value_counts())

# Separate features (X) and target (y)
X = data.drop('Spam', axis=1)
y = data['Spam']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create the Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]

# Check unique values in predictions
print("Unique values in y_pred:", np.unique(y_pred))

# Model evaluation
print("Confusion Matrix:")
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

# Classification Report with zero_division parameter
target_names = ['Not Spam', 'Spam']
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=target_names))

# Metrics Comparison
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

metrics_result_comparation(accuracy, recall, f1, auc_roc, model='Naive Bayes')

print("Dataset Shape:", data.shape)
print("Class Distribution in Dataset:")
print(data['Spam'].value_counts())
print("Unique values in y_pred:", np.unique(y_pred))
print("Correlation with Target (Spam):")
print(data.corr()['Spam'].sort_values(ascending=False))

importances = model.feature_importances_
feature_names = X.columns

# Create a DataFrame for visualization
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

print(importance_df)