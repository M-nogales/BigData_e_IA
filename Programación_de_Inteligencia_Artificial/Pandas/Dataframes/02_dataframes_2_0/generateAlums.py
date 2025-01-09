import pandas as pd
import numpy as np

# Mostrar más filas
pd.set_option('display.max_rows', 300)  

# Mostrar más columnas
pd.set_option('display.max_columns', 500) 

# Nombres alumnos
nombres_alumnos = [
    "Juan Pérez", "María López", "Carlos García", "Ana Fernández",
    "Luis Martínez", "Sofía Gómez", "Miguel Rodríguez", "Laura Sánchez",
    "José Torres", "Lucía Morales", "Andrés Herrera", "Carmen Ruiz",
    "Raúl Castro", "Elena Jiménez", "Javier Gil", "Isabel Romero",
    "Hugo Ortiz", "Sara Delgado", "Pablo Ramírez", "Marta Vargas"
]

# Generar notas aleatorias 
notas = {
    "Alumno": nombres_alumnos,
    "Base de Datos": np.random.uniform(1, 10, 20).round(1),
    "Programación": np.random.uniform(1, 10, 20).round(1),
    "Sistemas Informáticos": np.random.uniform(1, 10, 20).round(1),
    "Lenguajes de Marcas": np.random.uniform(1, 10, 20).round(1),
    "Entornos de Desarrollo": np.random.uniform(1, 10, 20).round(1),
}

# DataFrame
df_alumnos = pd.DataFrame(notas)

# Mostrar el DataFrame
print(df_alumnos)

# Apartado 01 Renombrar 

df_alumnos.rename(columns={"Base de Datos":"BD",
                            "Programación":"PR",
                            "Sistemas Informáticos":"SI",
                            "Lenguajes de Marcas":"LM",
                            "Entornos de Desarrollo":"ED"},
                              inplace=True)
print('df_alumnos renombrado: ', df_alumnos)

# Apartado 02 Filtrado

## filtrar los suspensos en alguna de las materias
suspensos = df_alumnos[
    (df_alumnos["BD"] < 5) |
    (df_alumnos["PR"] < 5) |
    (df_alumnos["SI"] < 5) |
    (df_alumnos["LM"] < 5) |
    (df_alumnos["ED"] < 5)
]
print('suspensos: ', suspensos)

## filtrar los suspensos de la asignatura de Programación
suspensos_programacion = df_alumnos[
    (df_alumnos["PR"] < 5)
]
print('suspensos_programacion: ', suspensos_programacion)

## filtrar las notas sobresalientes en cada materia (nota superior a 9)
sobresalientes = df_alumnos[
    (df_alumnos["BD"] > 9) &
    (df_alumnos["PR"] > 9) &
    (df_alumnos["SI"] > 9) &
    (df_alumnos["LM"] > 9) &
    (df_alumnos["ED"] > 9)
]
print('sobresalientes: ', sobresalientes)

## filtrar los resultados para los alumnos "Marta Vargas" y "Carmen Ruiz"
filter_alumnos = df_alumnos[
    (df_alumnos["Alumno"] == "Marta Vargas") |
    (df_alumnos["Alumno"] == "Carmen Ruiz")
]
print('filter_alumnos: ', filter_alumnos)

# Apartado 03 Pivotar
## pivotar la tabla con la columna denominada "Asignatura"
# Convertir el DataFrame a formato largo
df_long = pd.melt(
    df_alumnos,
    id_vars=["Alumno"],
    var_name="Asignatura",
    value_name="Nota"
)

# Pivotar la tabla con la columna denominada "Asignatura"
df_pivot = df_long.pivot(index="Alumno", columns="Asignatura", values="Nota")
print('df_pivot: ', df_pivot)

# Apartado 04 Ordenar

# ordenar por nombre de alumno
df_alumnos.sort_values("Alumno", inplace=True)
print('df_alumnos filtrar por nombre: ', df_alumnos)
# ordenar por Nota de asignatura Programación ascendente
df_alumnos.sort_values("PR", inplace=True)
print('df_alumnos filtrar por programación ascendente: ', df_alumnos)
# ordenar por Nota de asignatura Base de Datos descendente
df_alumnos.sort_values("BD", ascending=False, inplace=True)
print('df_alumnos filtrar por base de datos descendente: ', df_alumnos)

# Apartado 05 Agrupar

# Generar el promedio de notas de cada alumno
promedio_por_alumno=df_alumnos.groupby("Alumno").mean()
promedio_por_alumno['Promedio_Alumno'] = promedio_por_alumno.mean(axis=1)
print('df_alumnos: \n', promedio_por_alumno)
# Generar el promedio de notas de cada materia
promedio_por_notas = df_alumnos[['BD', 'PR', 'SI', 'LM', 'ED']].mean()
print(promedio_por_notas)
# Indicar el alumno con el mejor promedio en todas las materias
mejor_alumno = promedio_por_alumno['Promedio_Alumno'].idxmax()
mejor_promedio = promedio_por_alumno.loc[mejor_alumno]
print('mejor_promedio: ', mejor_promedio)

# Apartado 06 Contatenar
def generar_nulos(df):
    df_con_nulos = df.copy()
    for columna in ['BD', 'PR', 'SI', 'LM', 'ED']:
        df_con_nulos[columna] = df_con_nulos[columna].apply(lambda x: np.nan if int(x) % 2 == 0 else x)
    return df_con_nulos

df_alumnos_con_nulos = generar_nulos(df_alumnos)
print('df_alumnos_con_nulos: ', df_alumnos_con_nulos)

# Concatenar los dos DataFrames
concat_con_nulos = pd.concat([df_alumnos, df_alumnos_con_nulos], ignore_index=True)
print('concat_con_nulos: ', concat_con_nulos)

# Eliminar registros que no dispongan de datos (NaN)
concat_sin_nulos = concat_con_nulos.dropna()
print('concat_sin_nulos: ', concat_sin_nulos)