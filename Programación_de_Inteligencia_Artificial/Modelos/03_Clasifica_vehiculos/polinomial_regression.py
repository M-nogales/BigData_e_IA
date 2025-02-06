import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures


df = pd.read_csv('Dataset_Vehiculos.csv')

print('df.head(): ', df.head())

print('df.describe(): ', df.describe())
print('df.info(): ', df.info)

# Features
X = df.drop(columns=['ID', 'Price'])
# Target
y = df['Price']

# Split data into training and test sets
# 20% of the data will be used for testing, 80% for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalization
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
y_pred = lin_model.predict(X_test)



poly = PolynomialFeatures(degree=2)  # Cambiar el grado según necesidad
X_poly = poly.fit_transform(X_train)

# Ajustar el modelo de regresión polinómica
poly_model = LinearRegression()
poly_model.fit(X_poly, y_train)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Results
print(f"🔹 MSE (Error Cuadrático Medio): {mse:.2f}")
print(f"🔹 MAE (Error Absoluto Medio): {mae:.2f}")
print(f"🔹 R² (Coeficiente de Determinación): {r2:.2f}")

# Report
print("\n")

# Métricas de comparación
def metrics_result_comparation(mse, mae, r2, model):
    metrics = ['MSE', 'MAE', 'R²']
    values = [mse, mae, r2]
    
    # Create a bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(metrics, values, color=['blue', 'green', 'red'])
    
    # Add value labels on top of bars
    for i, v in enumerate(values):
        plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontsize=12, fontweight='bold')
    
    # Labels and title
    plt.ylim(0, max(values) + 0.1)
    plt.ylabel('Score')
    plt.title(f'Model metrics - {model}')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

metrics_result_comparation(mse, mae, r2, model = 'Polinomial Regression')