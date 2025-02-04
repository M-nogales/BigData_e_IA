import pandas as pd
import matplotlib.pyplot as plt
from sklearn.base import r2_score
from sklearn.metrics import mean_absolute_error, mean_squared_error

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

metrics_result_comparation(mse, mae, r2, model = 'Lasso Regression')