import pandas as pd
import numpy as np
from datetime import datetime

# Cargar el archivo Excel
df = pd.read_excel("data/datos_vehiculos.xlsx")

# Revisar los datos
print(df.head())
print(df.dtypes)
print(df.isnull().sum())

# Análisis estadístico descriptivo
estadisticas = df.describe()
estadisticas.to_excel("data/estadisticas.xlsx")

# Filtrar vehículos por marca, precio y año
filtro_marca = df[df['Marca'] == 'Toyota']
filtro_precio = df[df['Precio'] < 20000]
filtro_ano = df[df['Anyo'] == 2015]
filtro_color = df[df['Color'] == 'Rojo']

# Ordenar por precio y año
ordenado_precio = df.sort_values(by='Precio')
ordenado_ano = df.sort_values(by='Anyo', ascending=False)

# Calcular depreciación
anio_actual = datetime.now().year
df['Depreciación'] = (anio_actual - df['Anyo']) * 0.1 * df['Precio']

# Guardar los resultados con depreciación en un archivo CSV
df.to_csv("data/datos_con_depreciacion.csv", index=False)

# Mostrar resultados
print(filtro_marca.head())
print(ordenado_precio.head())
print(df[['Marca', 'Modelo', 'Anyo', 'Precio', 'Depreciación']].head())
