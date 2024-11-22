import pandas as pd

# Cargar los datos desde el archivo Excel
df = pd.read_excel("results/02_datos_alumnos.xlsx")
print('DataFrame inicial:')
print(df)

# Seleccionar solo las columnas numéricas
df_numeric = df.select_dtypes(include=["number"])

# Agregar la columna de agrupación "Edad" nuevamente
df_numeric["Edad"] = df["Edad"]

# Agrupar por edad y calcular el promedio
df_grouped = df_numeric.groupby("Edad").mean()
print('Promedio por edad:')
print(df_grouped)

# Guardar el resultado en un nuevo archivo Excel
df_grouped.to_excel("results/promedios_por_edad.xlsx", index=True)
print("Archivo guardado en 'results/promedios_por_edad.xlsx'.")
