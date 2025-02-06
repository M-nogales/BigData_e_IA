import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

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
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train, y_train)
y_pred = ridge_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Results
print(f"🔹 MSE (Error Cuadrático Medio): {mse:.2f}")
print(f"🔹 MAE (Error Absoluto Medio): {mae:.2f}")
print(f"🔹 R² (Coeficiente de Determinación): {r2:.2f}")

# Model Coefficients
plt.plot(ridge_model.coef_, label='Regresión Ridge', marker='s')
plt.xlabel("Coeficiente de la característica")
plt.ylabel("Valor del coeficiente")
plt.title("Comparación de Coeficientes")
plt.legend()
plt.show()