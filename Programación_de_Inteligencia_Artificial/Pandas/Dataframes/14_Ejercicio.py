# 14. **Modifica las notas de los alumnos en el DataFrame y guarda los cambios en una nueva versión del archivo CSV.**
''' Modifica las notas de los alumnos en el DataFrame y guarda los cambios en una nueva versión del archivo CSV.'''

import pandas as pd
import numpy as np
df = pd.read_excel("results/02_datos_alumnos.xlsx")


notas = ["Programación Final", "Base de Datos Final", "Lenguajes Final", "Sistemas Final", "Entornos Final"]

for nota in notas:
    df[nota] = df[nota] + np.random.randint(-2, 2, len(df))

print(df.head())
df.to_excel("results/14_datos_alumnos_modificado.xlsx", index=False)