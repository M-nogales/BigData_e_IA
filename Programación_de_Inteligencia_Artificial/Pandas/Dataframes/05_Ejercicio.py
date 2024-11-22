# 05. **Cuenta cuántos alumnos tienen una nota final menor a 5 en la asignatura de 'Sistemas'.**
''' Cuenta cuántos alumnos tienen una nota final menor a 5 en la asignatura de 'Sistemas'.'''

import pandas as pd

df = pd.read_excel("results/01_datos_alumnos.xlsx")
#shape[0] para obtener el número de filas, shape[1] para obtener el número de columnas
print("Han suspendido sistemas", df[df["Sistemas Final"] < 5].shape[0], "alumnos")

