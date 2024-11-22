# 10. **Calcula la desviación estándar del promedio general de las notas.**
''' Calcula la desviación estándar del promedio general de las notas.'''

import pandas as pd

df = pd.read_excel("results/02_datos_alumnos.xlsx")

# entiendo que de todas las columnas
desviacion_estandar = df[["Programación Final", "Base de Datos Final", "Lenguajes Final", "Sistemas Final", "Entornos Final"]].mean(axis=1).std()
print(desviacion_estandar)