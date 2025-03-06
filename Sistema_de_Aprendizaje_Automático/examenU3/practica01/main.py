import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Carga y exploración de datos
print("Cargando el dataset MNIST...")
print("MNIST es un dataset de dígitos manuscritos del 0 al 9., por lo que existen 10 clases.")
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist.data, mnist.target.astype(int)

# Normalizar los datos entre 0 y 1
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Dividir en 80% entrenamiento y 20% prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
print("Datos cargados y divididos correctamente.")

# 2. Entrenamiento del modelo con K=3
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Realizar predicciones
y_pred = knn.predict(X_test)

# 3. Evaluación del modelo
print("\nPrecisión, recall y F1-Score para k=3: ")
print(classification_report(y_test, y_pred))

print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))

# 4. Experimentación con diferentes valores de K
k_values = [1, 3, 5, 7, 9]
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred_k = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred_k)
    accuracies.append(acc)
    print(f"Precisión con K={k}: {acc:.4f}")

# Graficar la relación entre K y la precisión
plt.figure(figsize=(8, 5))
plt.plot(k_values, accuracies, marker='o', linestyle='-', color='b')
plt.xlabel('Número de Vecinos (K)')
plt.ylabel('Precisión')
plt.title('Relación entre K y Precisión en MNIST')
plt.grid()
plt.show()
