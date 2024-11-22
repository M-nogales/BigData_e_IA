# Lista de títulos y descripciones para cada ejercicio
titulos = [
    "Filtra a los alumnos que tienen 20 años o más y muestra sus notas finales.",
    "Añade una nueva columna llamada 'Aprobado' que indique si el alumno ha aprobado o no (si su promedio general es mayor o igual a 5).",
    "Calcula la nota máxima de cada módulo y muestra los resultados.",
    "Filtra a los alumnos que tienen una nota final superior a 9 en la asignatura de 'Lenguajes'.",
    "Cuenta cuántos alumnos tienen una nota final menor a 5 en la asignatura de 'Sistemas'.",
    "Obtén al alumno con la nota más alta en la asignatura de 'Programación'.",
    "Agrupa a los alumnos según si han aprobado o no y cuenta cuántos alumnos hay en cada grupo.",
    "Exporta a un archivo CSV los alumnos que han reprobado al menos un módulo.",
    "Crea un gráfico de dispersión que muestre la relación entre las notas finales de 'Programación' y 'Base de Datos'.",
    "Calcula la desviación estándar del promedio general de las notas.",
    "Carga un archivo Excel con datos de alumnos en un DataFrame y muestra los primeros 5 registros.",
    "Guarda una copia del archivo Excel en un archivo CSV.",
    "Filtra los alumnos que tienen una edad mayor a 22 años y guarda este subconjunto en un nuevo archivo Excel.",
    "Modifica las notas de los alumnos en el DataFrame y guarda los cambios en una nueva versión del archivo CSV.",
    "Lee un archivo CSV con datos de alumnos y calcula el promedio de las notas de un módulo específico.",
    "Agrupa a los alumnos por edad y guarda el promedio de cada grupo en un nuevo archivo Excel.",
    "Añade una nueva columna al archivo CSV para indicar si el alumno está en el grupo de honor (promedio general superior a 9).",
    "Carga un archivo Excel, calcula la nota mínima de cada módulo y guarda el resultado en un archivo CSV.",
    "Fusiona los datos de dos archivos Excel con datos de alumnos y guarda el resultado combinado en un nuevo archivo.",
    "Exporta un DataFrame a Excel y asegúrate de formatear los valores de las notas con dos decimales."
]

descripciones = titulos  # En este caso, las descripciones coinciden con los títulos.

# Crear archivos con el formato requerido
for i in range(len(titulos)):
    numero = f'{i + 1:02}'  # Formato de número de dos dígitos
    titulo = titulos[i]
    descripcion = descripciones[i]
    
    # Formato del contenido del archivo
    contenido = f"# {numero}. **{titulo}**\n''' {descripcion}'''"
    
    # Nombre del archivo
    nombre_archivo = f"Dataframes/{numero}_Ejercicio.py"
    
    # Crear el archivo y escribir el contenido
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)

print("Archivos creados con éxito.")

'''
# Generar datos para trabajar con DataFrames y exportar a Excel
nombres = ["Alejandro", "María", "Carlos", "Lucía", "José", "Ana", "Javier", "Laura",
"Pablo", "Marta",
"Sergio", "Elena", "Fernando", "Cristina", "David", "Isabel", "Rubén",
"Patricia", "Manuel", "Raquel"]
apellidos = ["García", "Martínez", "López", "Sánchez", "Pérez", "Gómez", "Fernández",
"Díaz", "Ruiz", "Moreno",
"Jiménez", "Álvarez", "Romero", "Vargas", "Silva", "Castro", "Ortega",
"Núñez", "Ramos", "Molina"]
# Generar datos para los alumnos
data = []
for i in range(20):
nombre = random.choice(nombres)
apellido = random.choice(apellidos)
correo = f"{nombre.lower()}.{apellido.lower()}@ejemplo.com"
edad = random.randint(18, 25)
programacion = [random.randint(0, 10) for _ in range(3)] # Notas de 3 trimestres
base_datos = [random.randint(0, 10) for _ in range(3)]
lenguajes = [random.randint(0, 10) for _ in range(3)]
sistemas = [random.randint(0, 10) for _ in range(3)]
entornos = [random.randint(0, 10) for _ in range(3)]
data.append([nombre, apellido, correo, edad] + programacion + base_datos + lenguajes
+ sistemas + entornos)
# Crear el DataFrame
columnas = [
"Nombre", "Apellidos", "Correo", "Edad",
"Programación T1", "Programación T2", "Programación T3",
"Base de Datos T1", "Base de Datos T2", "Base de Datos T3",
"Lenguajes T1", "Lenguajes T2", "Lenguajes T3",
"Sistemas T1", "Sistemas T2", "Sistemas T3",
"Entornos T1", "Entornos T2", "Entornos T3"
]
df_alumnos = pd.DataFrame(data, columns=columnas)
# Guardar el DataFrame en un archivo Excel
ruta_archivo = "datos_alumnos.xlsx"
df_alumnos.to_excel(ruta_archivo, index=False)
'''