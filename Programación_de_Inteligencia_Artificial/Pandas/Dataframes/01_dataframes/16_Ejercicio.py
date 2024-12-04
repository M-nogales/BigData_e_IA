# 16. **Agrupa a los alumnos por edad y guarda el promedio de cada grupo en un nuevo archivo Excel.**
''' Agrupa a los alumnos por edad y guarda el promedio de cada grupo en un nuevo archivo Excel.'''
#? test.py??
import pandas as pd

df = pd.read_excel("results/02_datos_alumnos.xlsx")
print('df: ', df)

df_grouped = df.groupby("Edad").mean()
print('Promedio por edad:')
print(df_grouped)