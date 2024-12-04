# 02. **Añade una nueva columna llamada 'Aprobado' que indique si el alumno ha aprobado o no (si su promedio general es mayor o igual a 5).**
''' Añade una nueva columna llamada 'Aprobado' que indique si el alumno ha aprobado o no (si su promedio general es mayor o igual a 5).'''

import pandas as pd

df = pd.read_excel("results/01_datos_alumnos.xlsx")
print(df)
# apartir de una nota de 8 ya aparece 1,por si quieres comprobarlo
df["Aprobado"] = df[["Programación Final", "Base de Datos Final", "Lenguajes Final", "Sistemas Final", "Entornos Final"]].mean(axis=1) >= 5
print(df)

df.to_excel("results/02_datos_alumnos.xlsx", index=False)