texto_a_mostrar = "En un lugar de la mancha"
frutas = ["Melón","Sandía","Plátano","Melocotón"]
print(frutas)
nums = [1,2,25,234,8,-1]
print(nums)
mix = [ "Melón",1,"Sandía",2,"Peras",4]
print(mix)
nuevaLista = list(("A","b","C"))
print(nuevaLista)
alumnos = nuevaLista # list(nuevaLista)
print(alumnos)
# al editar alumnos se edita nueva lista, copiando con list(nuevaLista), no
# alumnos[0]=1
# print(alumnos)
# print(nuevaLista)
print(frutas[0::2])# jump 2
print(frutas[::-1])# reverse 
if "Plátano" in frutas: print("yes") 

if "Mango" in frutas:
    print("yes")
else:
    print("no")

nums.append("append")# final
nums.insert(0,"insert")# dado index
print(nums)

nums.remove("insert")# busca y elimina el primero
nums.pop() # elimina último el del array
del nums[0] # del nums elimina todo el array
print(nums)

# Las tuplas en Python tienen las siguientes características:
# 1. Inmutables: No se pueden modificar después de ser creadas.
# 2. Ordenadas: Mantienen el orden de los elementos.
# 3. Admiten datos heterogéneos: Pueden contener distintos tipos de datos.
# 4. Acceso por índices: Se accede a los elementos con índices.
# 5. Admiten duplicados: Pueden contener valores repetidos.
# 6. Eficientes: Son más rápidas y ocupan menos memoria que los arrays.
# 7. Desempaquetado: Se pueden asignar sus valores a variables.
# 8. Usables como claves en diccionarios: Debido a su inmutabilidad.

tupla=("Pera","Kiwi","Tomate")

tuFruta=tuple(("Pera","Kiwi","Tomate","Melocoton"))
tuFruta2= tuple (tuFruta)
print(tuFruta)
test = tuFruta + tuFruta2
print(test)

# Un conjunto (set) en Python tiene las siguientes características:
# 1. No ordenado: Los elementos no mantienen un orden específico.
# 2. No admite duplicados: Cada elemento en un conjunto es único.
# 3. Mutable: Se pueden agregar o eliminar elementos después de su creación.
# 4. Elementos homogéneos: Todos los elementos deben ser hashables (inmutables).
# 5. Operaciones de conjuntos: Admite operaciones matemáticas como unión, intersección y diferencia.
# 6. Eficiente: La búsqueda y operaciones como agregar y eliminar son rápidas gracias a su implementación mediante tablas hash.

conjunto = {"Pera","Kiwi","Tomate","Melocoton","Melocoton", "Fresa", "Naranja"}
cnums = set({1,2,3,4,5,6,7,8,9,9,9,9})
print(conjunto)



for el in conjunto: print(el)

conjunto.update({"Ford","Horse","BMW","Audi"})
print(conjunto)


conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# Unión: Combina todos los elementos de ambos conjuntos sin duplicados
union = conjunto_a.union(conjunto_b)
print("Unión:", union)  # {1, 2, 3, 4, 5, 6}

# Intersección: Devuelve los elementos que están en ambos conjuntos
interseccion = conjunto_a.intersection(conjunto_b)
print("Intersección:", interseccion)  # {3, 4}

# Diferencia: Devuelve los elementos que están en el primer conjunto pero no en el segundo
diferencia = conjunto_a.difference(conjunto_b)
print("Diferencia:", diferencia)  # {1, 2}

# Diferencia simétrica: Devuelve los elementos que están en uno u otro conjunto, pero no en ambos
diferencia_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print("Diferencia Simétrica:", diferencia_simetrica)  # {1, 2, 5, 6}


# Diccionario
persona1={"nombre":"pepe","edad":19,"sexo":"M","sexo":"j"}
# persona1={"nombre":"pepe","edad":19,"sexo":"M","sexo":"j"} en caso de repetir se usa el último
print (persona1)
print(persona1["nombre"])
print(len(persona1))
print(persona1.get("edad"))
print(persona1.keys())
print(persona1.values())
persona2 = dict(persona1)
print(persona2)
persona2["nombre"] = "Luis"
persona2["edad"] = "20"
print(persona2.items())
print(persona2)
if "edad" in persona1: print("he nacido,wee")
persona2.update({"sexo":"XeY"})
print(persona2)
# persona2["caballo"] = "juan"
persona2.update({"caballo":"juan"})
# persona2.pop("edad")
# persona2.popitem()
print(persona2)
# del persona2["caballo"]
# persona2.clear()
print(persona2)
for x in persona2.items(): print(x)
for x in persona2: print(x)
for x in persona2.values(): print(x)
persona3 = persona2.copy()
datos_alumno= dict()
datos_alumno.update({"alumno1":persona1})
datos_alumno.update({"alumno2":dict({"nombre":"Alvaro","edad":28})})
datos_alumno.update({"alumno3":persona2})

print('datos_alumno: ', datos_alumno)
print('datos_alumno: ', datos_alumno["alumno3"]["nombre"])