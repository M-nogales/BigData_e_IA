# 19. **Fusiona los datos de dos archivos Excel con datos de alumnos y guarda el resultado combinado en un nuevo archivo.**
''' Fusiona los datos de dos archivos Excel con datos de alumnos y guarda el resultado combinado en un nuevo archivo.'''

import pandas as pd

df1 = pd.read_excel("results/02_datos_alumnos.xlsx")
df2 = pd.read_excel("results/14_datos_alumnos_modificado.xlsx")

inner_merge = pd.merge(left=df1, right=df2, how='right', on=None)

# Añadir 0 a los valores vacíos (empty)
inner_merge.fillna(0, inplace=True)
print(inner_merge)
inner_merge.to_excel("results/19_datos_alumnos_fusionados.xlsx", index=False)
