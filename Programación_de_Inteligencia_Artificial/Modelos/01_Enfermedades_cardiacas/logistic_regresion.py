from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd

# Cargar datos de enfermedad y mostrar información
health = pd.read_csv('./Dataset_Enfermedades.csv')
health.info()
print(health.head())

X = health[['edad','sexo','presion_sistolica','presion_diastolica','colesterol','glucosa','indice_masa_corporal','actividad_fisica','fumar','historia_familiar','diabetes']]
y = health['enfermedad_cardiaca']

# División de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalización de datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Entrenar el modelo de regresión logística
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)

# Evaluación del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))

target_names = ['Clase 0', 'Clase 1']
print('target_name: ', target_names)
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=target_names))
