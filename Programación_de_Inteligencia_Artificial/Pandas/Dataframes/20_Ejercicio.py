# 20. **Exporta un DataFrame a Excel y asegúrate de formatear los valores de las notas con dos decimales.**
''' Exporta un DataFrame a Excel y asegúrate de formatear los valores de las notas con dos decimales.'''

import pandas as pd

df = pd.read_excel("results/02_datos_alumnos.xlsx")

df.to_excel("results/20_datos_alumnos_exportados.xlsx", index=False, float_format="%.2f")