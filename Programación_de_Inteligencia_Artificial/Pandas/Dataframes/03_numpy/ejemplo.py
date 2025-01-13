import numpy as np



# Crear un vector con valores dentro del rango 10-49
print("Crear un vector con valores dentro del rango 10-49")
array = np.arange(10, 50)
print(array)

# Invertir vector
print('Invertir vector: ')
array = array[::-1]
print(array)

# Crear un array de 10 ceros.
print('Crear un array de 10 ceros.: ')
array = np.zeros(10)
print(array)
# Crear un array de 10 unos.
print('Crear un array de 10 unos: ')
array = np.ones(10)
print(array)
# Crear matriz 3x3 con valores del 0 a 8.
print('Crear matriz 3x3 con valores del 0 a 8: ')
array = np.arange(0,9).reshape(3,3)
print(array)

# Crear un array de 10 cincos.
print('Crear un array de 10 cincos: ')
array = np.ones(10) * 5
print(array)
print('Crear un array de 10 cincos: ')
array = np.full(10, 5)
print(array)
# dif entre los metodos anteriores?

# Transformar el array anterior a dimensión [2,5] y [5,2]
print("Transformar el array anterior a dimensión [2,5]")
array.reshape(2,5)
print(array)
print("Transformar el array anterior a dimensión [5,2]")
array.reshape(5,2)
print(array)

# Encontrar los índices (no el valor) que no son cero dentro del siguiente array: [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]
array = np.array([1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0])
print("Encontrar los índices (no el valor) que no son cero dentro del siguiente array: [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]")
print(np.nonzero(array))

# Crear una matriz identidad 6x6
print("Crear una matriz identidad 6x6")
array = np.identity(6)
print(array)

# Crear vector con 100 valores aleatorios de formato entero.
print("Crear vector con 100 valores aleatorios de formato entero.")
array = np.random.randint(0, 100, 100)
print(array)

# Crear un array con valores al azar de forma 3x3x3 (3 dimensiones)
print("Crear un array con valores al azar de forma 3x3x3 (3 dimensiones)")
array = np.random.randint(0, 100, 27).reshape(3,3,3)
print(array)

# Encontrar los valores mínimos y máximos del anterior array
print("Encontrar los valores mínimos y máximos del anterior array")
print(array.max())
print(array.min())

# Indicar los índices (posición) de los valores mínimos y máximos del array
print("Indicar los índices (posición) de los valores mínimos y máximos del array")
print(array.argmax())
print(array.argmin())

# Generar una matriz de tamaño 10x10 en la que los bordes sean 1 y el interior ceros (0). (Utilizar rangos de índices)
print("Generar una matriz de tamaño 10x10 en la que los bordes sean 1 y el interior ceros (0). (Utilizar rangos de índices)")
array = np.ones((10,10))
array[1:-1,1:-1]= 0
print(array)

# Crear array de tamaño 5x5 con los siguientes valores; [0,1,2,3,4]
print("Crear array de tamaño 5x5 con los siguientes valores; [0,1,2,3,4]")
array = np.tile([0, 1, 2, 3, 4], (5, 1))
print(array)

# Crear dos arrays aleatorios del mismo tamaño (3x3 o 5x5) y verificar si son iguales. Comprobar si algún elemento coincide, generando matriz booleana.
print("Crear dos arrays aleatorios del mismo tamaño (3x3 o 5x5) y verificar si son iguales. Comprobar si algún elemento coincide, generando matriz booleana.")
array1 = np.random.randint(0, 100, 9).reshape(3,3)
array2 = np.random.randint(0, 100, 9).reshape(3,3)
is_equal = np.array_equal(array1, array2)

print("array1")
print(array1)

print("array2")
print(array2)

print("son iguales?", is_equal)

print("matriz boleana")
print(array1 == array2)

# Generar array de dimensión 5x5 en el que los elementos sean de tipo numérico entero aleatorio comprendido entre el 1 y 100.
print("Generar array de dimensión 5x5 en el que los elementos sean de tipo numérico entero aleatorio comprendido entre el 1 y 100.")
array = np.random.randint(1, 100, 25).reshape(5,5)
print(array)

# Dado el array anterior, obtener la suma total de la matriz 5x5.
print("Dado el array anterior, obtener la suma total de la matriz 5x5.")
print(array.sum())

# Dado el array anterior, obtener un nuevo array que contenga la suma de cada una de las columnas.
print("Dado el array anterior, obtener un nuevo array que contenga la suma de cada una de las columnas.")
array1 = np.sum(array, axis=0)
print(array1)

# Dado el array anterior, extraer fila inicial, fila intermedia (fila 3) y la última fila.
print("Dado el array anterior, extraer fila inicial, fila intermedia (fila 3) y la última fila.")
print("fila inicial", array[0,:])
print("fila intermedia", array[2,:])
print("última fila", array[-1,:])