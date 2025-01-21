''' 9. Gráfico de líneas con datos de series temporales
- **Datos**: DataFrame simulado con datos de ventas diarias.
- **Pasos**:
  - Convertir los datos simulados a arrays.
  - Crear un gráfico de líneas para analizar tendencias estacionales.
  - Aplicar un suavizado con Seaborn y personalizar las líneas con estilos diferenciados.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

np.random.seed(42)
fechas = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
ventas = 50 + 10 * np.sin(2 * np.pi * fechas.dayofyear / 365) + np.random.normal(0, 5, len(fechas))

ventas_df = pd.DataFrame({"Fecha": fechas, "Ventas": ventas})

x = ventas_df["Fecha"].values
y = ventas_df["Ventas"].values

plt.figure(figsize=(12, 6))

sns.lineplot(data=ventas_df, x="Fecha", y="Ventas", label="Tendencia Suavizada", linestyle="-", color="red")

plt.show()