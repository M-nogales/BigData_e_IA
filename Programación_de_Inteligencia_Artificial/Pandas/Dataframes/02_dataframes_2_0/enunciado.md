Dado el fichero dataframe02.py en el que se genera un DataFrame de 20 alumnos
con las notas correspondientes a diversos módulos, realizar las siguientes operaciones:

## Apartado 01. Renombrar.
Renombrar las columnas de los módulos disponibles y visualizar el resultado final.

Base de Datos → BD

Programación → PR

Sistemas Informáticos → SI

Lenguajes de Marcas → LM

Entornos de Desarrollo → ED

## Apartado 02. Filtrado.
Filtrar los datos contenidos en el DataFrame con las siguientes condiciones:
- Filtrar los suspensos en alguna de las materias
- Filtrar los suspensos de la asignatura de Programación
- Filtrar las notas sobresalientes en cada materia (nota superior al 9)
- Filtrar los resultados para los alumnos “Marta Vargas” y “Carmen Ruiz”

## Apartado 03. Pivotar.
Pivotar la tabla (DataFrame) con columna denominada “Asignatura”

## Apartado 04. Ordenar.
Realizar la ordenación de los resultados del dataframe:
- Ordenar por nombre de alumno
- Ordenar por Nota de asignatura Programación ascendente
- Ordenar por Nota de asignatura Base de Datos descendente

## Apartado 05. Agrupar.
Realizar la agrupación de datos del dataframe talque;
- Generar el promedio de notas de cada alumno
- Generar el promedio de notas de cada materia
- Indicar el alumno con el mejor promedio en todas las materias.

## Apartado 06. Concatenar.
Generar un nuevo dataframe (partiendo del original) en el que falten algunas notas
en algunas asignaturas a algunos alumnos. (No rellenar todos los datos, deben
faltar aleatoriamente datos)

Se deberá realizar la concatenación de los dos DataFrames de la siguiente forma;
- Mantener los datos nulos (NaN)
- Eliminar los registros que no dispongan de datos (NaN)