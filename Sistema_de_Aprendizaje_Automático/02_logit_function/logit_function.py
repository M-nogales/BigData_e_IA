
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, recall_score, roc_auc_score, roc_curve

# load the data
data = pd.read_csv('credit_approval_data.csv')


X = data.drop([ 'Aprobado'], axis=1)
y = data['Aprobado']

# split the data between training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# create the logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]

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
target_names = ['Approved', 'Rejected']
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

# Feature Importance in Logistic Regression
feature_importances = model.coef_[0]
feature_names = X.columns

# Create a DataFrame for visualization
importance_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': feature_importances})
importance_df['Absolute_Coefficient'] = np.abs(importance_df['Coefficient'])
importance_df = importance_df.sort_values(by='Absolute_Coefficient', ascending=False)

# Plot feature importance
plt.figure(figsize=(10, 6))
plt.barh(importance_df['Feature'], importance_df['Absolute_Coefficient'], color='skyblue')
plt.xlabel('Absolute Coefficient Value')
plt.title('Feature Importance in Logistic Regression')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Print feature importance
print("\nFeature Importances (Coefficients):")
print(importance_df)