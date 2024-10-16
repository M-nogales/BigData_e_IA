# Ejercicio extra: Diccionario
# cantidad = int(input("¿Cuantos alumnos tiene el aula?"))
# aula = dict()
# for i in range(cantidad):
#     nombre = str(input("¿Cuaal es el nombre del alumno?"))
#     apellido = str(input("¿Cuaal es el apellido del alumno?"))
#     edad = int(input("¿Cuantos años tiene el alumno?"))
#     correo = str(input("¿Cuaal es el correo del alumno?"))
#     provincia = str(input("¿Cuaal es la provincia del alumno?"))
#     alumno = {"nombre":nombre,"apellido":apellido,"edad":edad,"correo":correo,"provincia":provincia}
#     aula.update({f"alumno{i}":alumno})

# print('aula: ', aula)

#1
nums1 = [0,1,2,3,4]

print('nums: ', nums1[2])

#2
nums2 = list()
i=1
for i in range(11):
     nums2.append(i)

print('num2: ', nums2)

#3
countries = ["España","Italia","Marruecos","Grecia","3000 viviendas"]
countries[1] = "Alemania"

print('countries: ', countries)

#4
colors = ["Yellow","Orange","Blue","Red"]
colors.insert(2,"White")

print('colors: ', colors)

#5
fruits = ["Peach","Strawberry","Watermelon"]
fruits.reverse()
fruits[::-1].pop()
fruits.reverse()

print('fruits: ', fruits)

#6
nums6 = [0,1,2,3]
nums6.remove(3)

print('nums6: ', nums6)

#7
nums7 = [0,1,2,3,4,5]
nums7.reverse()

print('nums7: ', nums7)

#8
nums8 = [1123,543,2,765,21,456]
nums8.sort()

print('nums8: ', nums8)

#9
names9 = ["Juan","Juan","Pepe","Alvaro","Miguel"]
print('names9.count("Juan"): ', names9.count("Juan"))

#10
animals = ["Tiger","Crocodile", "Turtoise","Cat"]
print('"Tiger" in animals: ', "Tiger" in animals)

#11
nums11_a = [0,1,2,3]
nums11_b = [4,5,6,7]

print('nums11_a + nums11_b: ', nums11_a + nums11_b)

#12
string12 = ["cadenaInicial","cadena1","cadena2","cadenaFinal"]
result = ""
for i in string12: 
    result +=i 

print('result: ', result)

#13
nums13 = [0,1,2,3,4,5]

print('len(nums13): ', len(nums13))

#14
letters = ["a","b","c","d","e","f","g","h"]
print('letter f: ', letters.index("f"))

#15
nums15_a = [0,1,2,3,4]
nums15_b = [5,6,7,8,9]
nums15_a.extend(nums15_b)

print('extend: ', nums15_a)

#16
nums16 = [0,1,2,3,4,5,6,7,8,9,10]

print('nums16: ', nums16[-3:])

#17
colors2 = colors.copy()

print('colors: ', colors2)

#18
nested_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print('nested_array: ', nested_array)

print('nested_array[1][1]: ', nested_array[1][1])

#19
cleared_list = [0,1,2,3,4,5]
cleared_list.clear()

#20
nums20 = [0,1,2]

for i in nums20: print( i*4)

#21
nums21 = [0,1,2,3,4,5,6,7,8,10]
print('sum(nums21): ', sum(nums21))

#22
booleans = [True,True,False,True,True,False]
print('all(booleans): ', all(booleans))

#23
print('any(booleans): ', any(booleans))

#24
strings24 = ["cadenaInicial","cadema2","cadena3","cadenaFinal"]
result= ", ".join(strings24)

print(result)

#25
strings25 = list("cadenaInicial")
print('strings25: ', strings25)

#26
nums26 = [0,1,2,3,4,5,6,7,8,9]
print('nums26[2:6]: ', nums26[2:6])

#27
cities = ["Barcelona","Sydney","Singapur","New York"]
print('cities.pop(-1): ', cities.pop(-1))

#28
nums28 = [0,2,123,543,123,645]
print('max(nums28): ', max(nums28))

#29
nums29 = [0,2,123,543,123,645]
print('min(nums29): ', min(nums29))

#30
nums30 = [1123,543,2,765,21,456]
print('sorted(nums30): ', sorted(nums30))

#31
array31 = ["cadena1",0,2,5,"cadena2","cadena5"]
print('array31[2]: ', array31[2])

#32
strings32 = ["cadenaInicial","cadema2","cadena3","cadenaFinal"]

for index, value in enumerate(strings32):    print(f"Índice: {index}, Valor: {value}")

#33
nested_array33 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in nested_array33:
    for j in i:
        print(j)

#34
nums34 = [0,1,2,3,4,5,6]
print('nums34: ', nums34)
del nums34[2:5]

print('nums34: ', nums34)

#35
nums35 = [0,1,2,3,4,5,6]
bigger_than_5 = [num for num in nums35 if num > 5]

print('bigger_than_5: ', bigger_than_5)

#36
strings36 = ["cadenaInicial","cadema2","cadena3","cadenaFinal"]

result36 = []

for i in strings36:
    palabras = i.split()
    result36.append(palabras)

print('result36:', result36)

#37
tuple_array = ( 0,1,2,3,4,5,6 )
array = list(tuple_array)
array.append(99)
print('array.append(99): ', array)

#38
#39
#41 
#42
#43
#44
#45
#46
#47
#48
#49
#50