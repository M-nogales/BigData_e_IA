# REGRESION LINEAL SIMPLE

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de ejemplo
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

# Crear el modelo y ajustarlo
model = LinearRegression()
model.fit(X, y)

# Predicción
y_pred = model.predict(X)

# Visualización
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, y_pred, color='red', label='Línea de regresión')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresión Lineal Simple')
plt.legend()
plt.show()

# Coeficientes del modelo
print(f'Intercepto: {model.intercept_}')
print(f'Pendiente: {model.coef_[0]}')

