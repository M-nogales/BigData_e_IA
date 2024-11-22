# 18. **Carga un archivo Excel, calcula la nota mínima de cada módulo y guarda el resultado en un archivo CSV.**
''' Carga un archivo Excel, calcula la nota mínima de cada módulo y guarda el resultado en un archivo CSV.'''

import pandas as pd

df = pd.read_excel("results/02_datos_alumnos.xlsx")

notas = ["Programación Final", "Base de Datos Final", "Lenguajes Final", "Sistemas Final", "Entornos Final"]

df["notas_minimas"] = df[notas].min(axis=1)

print(df.head())
df.to_csv("results/18_datos_alumnos_minimos.csv", index=False)