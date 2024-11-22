# 11. **Carga un archivo Excel con datos de alumnos en un DataFrame y muestra los primeros 5 registros.**
''' Carga un archivo Excel con datos de alumnos en un DataFrame y muestra los primeros 5 registros.'''

import pandas as pd

df = pd.read_excel("results/02_datos_alumnos.xlsx")

print(df.head())