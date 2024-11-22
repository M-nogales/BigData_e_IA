# 08. **Exporta a un archivo CSV los alumnos que han reprobado al menos un módulo.**
''' Exporta a un archivo CSV los alumnos que han reprobado al menos un módulo.'''

import pandas as pd

df = pd.read_excel("results/02_datos_alumnos.xlsx")

suspensos = df[(df["Programación Final"] < 5) | (df["Base de Datos Final"] < 5) | (df["Lenguajes Final"] < 5) | (df["Sistemas Final"] < 5) | (df["Entornos Final"] < 5)]
print(suspensos)

suspensos.to_csv("results/08_alumnos_suspensos.csv", index=False)