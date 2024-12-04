# 17. **Añade una nueva columna al archivo CSV para indicar si el alumno está en el grupo de honor (promedio general superior a 9).**
''' Añade una nueva columna al archivo CSV para indicar si el alumno está en el grupo de honor (promedio general superior a 9).'''

import pandas as pd

df = pd.read_csv("results/12_datos_alumnos.csv")

df["Grupo de Honor"] = df[["Programación Final", "Base de Datos Final", "Lenguajes Final", "Sistemas Final", "Entornos Final"]].mean(axis=1) > 9
print(df)

df.to_csv("results/17_datos_alumnos_grupo_honor.csv", index=False)