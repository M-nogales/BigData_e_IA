# Lista de títulos y descripciones para cada ejercicio
titulos = [
    "Análisis de Ventas de una Semana",
    "Calificaciones de Estudiantes",
    "Análisis de Temperaturas Semanales",
    "Registro de Horas de Trabajo",
    "Inventario de Productos",
    "Evaluación de Encuesta de Satisfacción",
    "Análisis de Precio de un Producto en Tiendas",
    "Análisis de Datos Meteorológicos",
    "Registro de Visitas a una Página Web",
    "Análisis de Puntuaciones de Juegos"
]

descripciones = [
    """Solicita al usuario que ingrese las ventas diarias de una semana (7 días).
Crea una Serie con los datos proporcionados.
Realiza el análisis: muestra el total de ventas, el promedio, y el día con las mayores ventas.
Visualiza los días que tienen ventas por encima del promedio.""",

    """Pide al usuario que ingrese las calificaciones de 10 estudiantes.
Crea una Serie con las calificaciones y asigna nombres de estudiantes como índice.
Calcula el promedio, la mediana y la desviación estándar de las calificaciones.
Reemplaza las calificaciones que están por debajo de 50 con "Reprobado".
Muestra los estudiantes con calificaciones aprobatorias.""",

    """Solicita al usuario las temperaturas registradas en una semana (7 días).
Crea una Serie con los datos y calcula la temperatura máxima y mínima.
Identifica los días que tienen temperaturas por encima de 25°C.
Rellena posibles valores faltantes (NaN) con la temperatura promedio.
Grafica las temperaturas de la semana.""",

    """Solicita al usuario que ingrese las horas trabajadas por un empleado durante 5 días laborales.
Crea una Serie con los datos.
Calcula el total de horas trabajadas, y muestra los días en los que el empleado trabajó más de 8 horas.
Reemplaza las horas menores a 6 con "Medio tiempo".
Muestra una lista de días y su clasificación de horas (Normal, Medio tiempo, Extra).""",

    """Pide al usuario que ingrese la cantidad de 8 productos diferentes en stock.
Crea una Serie y asigna nombres de productos como índice.
Muestra los productos con menos de 10 unidades.
Rellena cualquier valor faltante (NaN) con 0.
Muestra los productos ordenados por la cantidad en stock.""",

    """Solicita al usuario que ingrese las calificaciones de satisfacción (de 1 a 5) de 12 clientes.
Crea una Serie con las calificaciones.
Calcula la frecuencia de cada calificación y el porcentaje de clientes satisfechos (calificación ≥ 4).
Reemplaza cualquier calificación de 1 con "Insatisfecho".
Muestra un resumen de las calificaciones en forma de gráfico de barras.""",

    """Pide al usuario que ingrese los precios de un producto en 5 tiendas diferentes.
Crea una Serie y nombra cada tienda como índice.
Muestra el precio más bajo y más alto.
Identifica las tiendas con precios por encima de la mediana.
Rellena los precios faltantes (NaN) con el precio promedio y grafica los precios.""",

    """Solicita al usuario las precipitaciones registradas durante los últimos 7 días.
Crea una Serie con los datos.
Identifica los días sin lluvia (0 mm) y reemplázalos con "Sin precipitación".
Calcula el total y el promedio de precipitaciones.
Muestra los días con precipitación por encima del promedio.""",

    """Pide al usuario que ingrese el número de visitas diarias a una página web durante 10 días.
Crea una Serie con los datos.
Calcula el total y el promedio de visitas diarias.
Muestra los días con más visitas que el promedio y reemplaza los valores de visitas < 50 con "Baja visita".
Grafica el número de visitas diarias.""",

    """Solicita al usuario las puntuaciones de un jugador en 8 rondas de un juego.
Crea una Serie con las puntuaciones y asigna números de ronda como índice.
Calcula la puntuación máxima, mínima y la diferencia entre la más alta y la más baja.
Muestra las rondas en las que la puntuación es superior a 80.
Ordena las puntuaciones de menor a mayor y muestra el ranking."""
]

# Crear archivos con el formato requerido
for i in range(len(titulos)):
    numero = f'{i + 1:02}'  # Formato de número de dos dígitos
    titulo = titulos[i]
    descripcion = descripciones[i]
    
    # Formato del contenido del archivo
    contenido = f"# {numero}. **{titulo}**\n''' {descripcion}\n '''"
    
    # Nombre del archivo
    nombre_archivo = f"{numero}_Series.py"
    
    # Crear el archivo y escribir el contenido
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)

print("Archivos creados con éxito.")
