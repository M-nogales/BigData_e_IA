# 03. **Calcula la nota máxima de cada módulo y muestra los resultados.**
''' Calcula la nota máxima de cada módulo y muestra los resultados.'''

# entiendo que de cada columna
import pandas as pd

df = pd.read_excel("results/01_datos_alumnos.xlsx")
print(df)

maximas_notas = df[["Programación Final", "Base de Datos Final", "Lenguajes Final", "Sistemas Final", "Entornos Final"]].max()
print(maximas_notas)