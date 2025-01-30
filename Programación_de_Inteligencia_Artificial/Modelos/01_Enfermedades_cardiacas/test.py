import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd

health = pd.read_csv('./Dataset_Enfermedades.csv')


# Select two features for 2D visualization
X_vis = health[['edad', 'presion_sistolica']]
y_vis = health['enfermedad_cardiaca']

# Split the dataset into training and test sets (80% training, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_vis, y_vis, test_size=0.2, random_state=42)

# Normalize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the SVM model (using the RBF kernel)
model = SVC(kernel='rbf', C=1.0, gamma='scale')
model.fit(X_train, y_train)

# Create a meshgrid to plot the decision boundary
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

# Get the predictions for each point in the meshgrid
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundary
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.75, cmap='coolwarm')

# Plot the training points
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolors='k', marker='o', cmap='coolwarm', label='Training data')

# Plot the test points
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, edgecolors='k', marker='^', cmap='coolwarm', label='Test data')

# Add labels and title
plt.xlabel('Edad')
plt.ylabel('Presión Sistólica')
plt.title('SVM Decision Boundary (2D) for Cardiac Disease Prediction')
plt.legend()
plt.show()
