# 12. **Guarda una copia del archivo Excel en un archivo CSV.**
''' Guarda una copia del archivo Excel en un archivo CSV.'''

import pandas as pd

df = pd.read_excel("results/02_datos_alumnos.xlsx")

df.to_csv("results/12_datos_alumnos.csv", index=False)