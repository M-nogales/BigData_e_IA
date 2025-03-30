import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Generar datos simulados de transacciones bancarias
np.random.seed(42)
normal_data = np.random.normal(loc=100, scale=20, size=(200, 2))  # Transacciones normales
anomalous_data = np.random.normal(loc=200, scale=30, size=(10, 2))  # Transacciones anómalas

data = np.vstack((normal_data, anomalous_data))
df = pd.DataFrame(data, columns=["Monto", "Tiempo"])

# Aplicar Isolation Forest
iso_forest = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = iso_forest.fit_predict(df)

# Identificar transacciones con mayor probabilidad de fraude
anomalies = df[df['anomaly'] == -1]

# Visualizar las anomalías en un gráfico
plt.figure(figsize=(8, 6))
plt.scatter(df['Monto'], df['Tiempo'], c=df['anomaly'], cmap='coolwarm', edgecolors='k')
plt.xlabel("Monto de Transacción")
plt.ylabel("Tiempo")
plt.title("Detección de Anomalías con Isolation Forest")
plt.colorbar(label="Anomalía (-1) vs Normal (1)")
plt.show()