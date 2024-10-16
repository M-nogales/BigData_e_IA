# Ejercicio: Variables numéricas y operaciones básicas
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

# Ejercicio: Variables de tipo cadena (string)
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido

print(len(nombre_completo))
print(nombre_completo.upper())
print(nombre_completo.lower())

# Ejercicio: Listas
nums = [3,8,1,6,0,8,4]
nums.append(33)
del nums[0]
nums.sort()

print(nums, len(nums))

# Ejercicio: Diccionarios
estudiante = dict({"nombre":"ana","edad":22,"curso":"Matematicas"})
estudiante["edad"]= 23
estudiante.update({"promedio":8.5})

print('estudiante: ', estudiante)
print('edad del estudiante: ', estudiante["edad"])

# Ejercicio: Operaciones lógicas
x = True
y = False
z = True

print(x and y)
print(x or y)
print(not x)
print((x or y) and z)
print(x == y)

# Ejercicio: Métodos de Listas
colores = ["rojo","verde","azul","amarillo"]
colores.append("morado")
colores.insert(2,"naranja")
colores.remove("verde")
colores.sort()
colores.reverse() # colores[::-1] 

print(colores)

# Ejercicio: Tuplas
puntos = (5,10,15,20,25)
print(puntos[2])
puntosLista= list(puntos)
puntosLista.append(30)
puntosLista = tuple(puntosLista)

print(puntosLista)

# Ejercicio: Sets (Conjuntos)
frutas = {"manzana", "banana", "naranja", "uva"}
# frutas.update("pera") añade cada uno de los caracteres
frutas.add("pera")
# frutas.update("banana")
frutas.discard("naranja")

print(frutas)

# Ejeccicio Diccionarios
capitales = {"España":"Madrid","Francia":"Paris","Italia":"Roma"}
capitales.update({"Alemania":"Berlín"})
capitales["Francia"] = "Lyon"
capitales.pop("Italia")

print('capitales: ', capitales.keys())
print('capitales: ', capitales.values())
print('capitales: ', capitales)

# Ejercicio: Métodos avanzados de Listas
nums2 = [12, 45, 78, 23, 56, 89, 23, 56]
nums2.count(23)
nums2.index(56)
nums2.pop()
nums2.extend([100,200,300])
# numeros_copia = nums2 comparten memoria
# numeros_copia = list(nums2) no comparten memoria
numeros_copia = nums2.copy() # idem anterior
print (numeros_copia)

# Ejercicio: Más sobre tuplas
dias_semana = ("Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo")
print("¿Está Sábado en la tupla?", "Sábado" in dias_semana)
for day in dias_semana: print(day)
# dias_semana[0] = "infierno"

print(dias_semana)

# Ejercicio: Operaciones con Sets
animales = {"gato", "perro", "loro", "pez"}
animales_domesticos ={"gato","perro","conejo"}

print(animales.intersection(animales_domesticos))
print(animales.difference(animales_domesticos))
print(animales.union(animales_domesticos))

# Ejercicio: Diccionarios anidados
estudiante1={"nombre":"carlos","edad":19,"materias":["Matemáticas","Física"]}
estudiante2={"nombre":"Marta","edad":20,"materias":["Química","Biología"]}
clase = {"estudiante1":estudiante1,"estudiante2":estudiante2}

print('clase: ', clase)