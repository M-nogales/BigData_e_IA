# 06. **Obtén al alumno con la nota más alta en la asignatura de 'Programación'.**
''' Obtén al alumno con la nota más alta en la asignatura de 'Programación'.'''

import pandas as pd

df = pd.read_excel("results/01_datos_alumnos.xlsx")
print(df[df["Programación Final"] == df["Programación Final"].max()])
