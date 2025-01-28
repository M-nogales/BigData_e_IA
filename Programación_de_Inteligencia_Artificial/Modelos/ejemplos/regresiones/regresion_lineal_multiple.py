# REGRESION LINEAL MULTIPLE

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

# Datos de ejemplo
data = {
    'X1': [1, 2, 3, 4, 5],
    'X2': [5, 4, 3, 2, 1],
    'y':  [3, 4, 2, 5, 6]
}
df = pd.DataFrame(data)

# Definir variables independientes y dependientes
X = df[['X1', 'X2']]
y = df['y']

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)

# Evaluación del modelo
print(f'Coeficiente R^2: {r2_score(y_test, y_pred):.2f}')
print(f'Error cuadrático medio: {mean_squared_error(y_test, y_pred):.2f}')
print(f'Intercepto: {model.intercept_}')
print(f'Coeficientes: {model.coef_}')
