# 13. **Filtra los alumnos que tienen una edad mayor a 22 años y guarda este subconjunto en un nuevo archivo Excel.**
''' Filtra los alumnos que tienen una edad mayor a 22 años y guarda este subconjunto en un nuevo archivo Excel.'''

import pandas as pd

df = pd.read_excel("results/02_datos_alumnos.xlsx")

df_mayores = df[df["Edad"] > 22]

df_mayores.to_excel("results/13_datos_alumnos_mayores.xlsx", index=False)