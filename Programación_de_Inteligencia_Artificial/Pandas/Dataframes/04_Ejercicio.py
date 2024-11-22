# 04. **Filtra a los alumnos que tienen una nota final superior a 9 en la asignatura de 'Lenguajes'.**
''' Filtra a los alumnos que tienen una nota final superior a 9 en la asignatura de 'Lenguajes'.'''

import pandas as pd

df = pd.read_excel("results/01_datos_alumnos.xlsx")
print(df[df["Lenguajes Final"] > 9])