
#DataFrames

import pandas as pd
import numpy as np
datos = {'nombre': ['Juan', 'Ana', 'Pedro', 'María'],
         'edad': [25, 30, 39, 22],
         'ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']}

df = pd.DataFrame(datos)
# print(df)

datos2 = [['maria', 25, 'madrid'], ['juan', 30, 'barcelona'], ['pedro', 39, 'sevilla'], ['ana', 22, 'valencia']]
df2 = pd.DataFrame(datos2, columns=['nombre', 'edad', 'ciudad'])
# print(df2)

datos3 = [{'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'},{ 'nombre': 'Ana', 'edad': 30, 'ciudad': 'Barcelona'}, {'nombre': 'Pedro', 'ciudad': 'Sevilla'}]
df3 = pd.DataFrame(datos3)
# print(df3)

df4= pd.DataFrame(np.random.rand(4, 3), columns=['A', 'B', 'C'])
print(df4)


# devuelve info sobre el dataframe
print(df.info())
# devuelve las primeras 5 filas
print(df.head())
# devuelve las primeras 2 filas
print(df.head(2))
# devuelve las últimas 5 filas
print(df.tail())
# devuelve las filas y columnas
print(df.shape)
# devuelve indo de las columnas
print(df.columns)
# resumen estadístico de las columnas numéricas
print(df.describe())
# devuelve el valor máximo y mínimo de las columnas numéricas
print(df.max())
print(df.min())
# devuelve si una columna tiene valores nulos
print(df3.isnull())
# elimina las filas con valores nulos
print(df3.dropna())
# ordena el dataframe por una columna
print(df.sort_values('edad'))
# print(df.sort_values(by='edad', ascending=False))
# ordenar por indice
print(df.sort_index())
# cambiar el nombre una de las columnas
# df.rename(columns={'nombre': 'Nombre', 'edad': 'Edad', 'ciudad': 'Ciudad'}, inplace=True)
# print(df)
df4['A'].apply(lambda x: x*10)
print(df4)