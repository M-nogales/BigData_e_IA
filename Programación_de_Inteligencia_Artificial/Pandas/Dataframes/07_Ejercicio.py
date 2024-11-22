# 07. **Agrupa a los alumnos según si han aprobado o no y cuenta cuántos alumnos hay en cada grupo.**
''' Agrupa a los alumnos según si han aprobado o no y cuenta cuántos alumnos hay en cada grupo.'''

import pandas as pd

df = pd.read_excel("results/02_datos_alumnos.xlsx")
print(df.groupby("Aprobado").size())