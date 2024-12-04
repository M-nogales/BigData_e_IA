# 15. **Lee un archivo CSV con datos de alumnos y calcula el promedio de las notas de un módulo específico.**
''' Lee un archivo CSV con datos de alumnos y calcula el promedio de las notas de un módulo específico.'''

import pandas as pd

df = pd.read_csv("results/12_datos_alumnos.csv")

print(df["Programación Final"].mean())
