from functools import reduce

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

print('1: ', 1)
print('nums: ', nums1[2])

#2
nums2 = list()
i=1
for i in range(11):
     nums2.append(i)

print('2: ', 2)
print('num2: ', nums2)

#3
countries = ["España","Italia","Marruecos","Grecia","3000 viviendas"]
countries[1] = "Alemania"

print('3: ', 3)
print('countries: ', countries)

#4
colors = ["Yellow","Orange","Blue","Red"]
colors.insert(2,"White")

print('4: ', 4)
print('colors: ', colors)

#5
fruits = ["Peach","Strawberry","Watermelon"]
fruits.reverse()
fruits[::-1].pop()
fruits.reverse()

print('5: ', 5)
print('fruits: ', fruits)

#6
nums6 = [0,1,2,3]
nums6.remove(3)

print('6: ', 6)
print('nums6: ', nums6)

#7
nums7 = [0,1,2,3,4,5]
nums7.reverse()

print('7: ', 7)
print('nums7: ', nums7)

#8
nums8 = [1123,543,2,765,21,456]
nums8.sort()

print('8: ', 8)
print('nums8: ', nums8)

#9
names9 = ["Juan","Juan","Pepe","Alvaro","Miguel"]
print('9: ', 9)
print('names9.count("Juan"): ', names9.count("Juan"))

#10
animals = ["Tiger","Crocodile", "Turtoise","Cat"]
print('10: ', 10)
print('"Tiger" in animals: ', "Tiger" in animals)

#11
nums11_a = [0,1,2,3]
nums11_b = [4,5,6,7]

print('11: ', 11)
print('nums11_a + nums11_b: ', nums11_a + nums11_b)

#12
string12 = ["cadenaInicial","cadena1","cadena2","cadenaFinal"]
result = ""
for i in string12: 
    result +=i 

print('12: ', 12)
print('result: ', result)

#13
nums13 = [0,1,2,3,4,5]

print('13: ', 13)
print('len(nums13): ', len(nums13))

#14
letters = ["a","b","c","d","e","f","g","h"]
print('14: ', 14)
print('letter f: ', letters.index("f"))

#15
nums15_a = [0,1,2,3,4]
nums15_b = [5,6,7,8,9]
nums15_a.extend(nums15_b)

print('15: ', 15)
print('extend: ', nums15_a)

#16
nums16 = [0,1,2,3,4,5,6,7,8,9,10]

print('16: ', 16)
print('nums16: ', nums16[-3:])

#17
colors2 = colors.copy()

print('17: ', 17)
print('colors: ', colors2)

#18
nested_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print('18: ', 18)
print('nested_array: ', nested_array)

print('nested_array[1][1]: ', nested_array[1][1])

#19
print('19: ', 19)
cleared_list = [0,1,2,3,4,5]
print('cleared_list: ', cleared_list)
cleared_list.clear()
print('cleared_list: ', cleared_list)

#20
print('20: ', 20)
nums20 = [0,1,2]

for i in nums20: print( i*4)

#21
nums21 = [0,1,2,3,4,5,6,7,8,10]
print('21: ', 21)
print('sum(nums21): ', sum(nums21))

#22
booleans = [True,True,False,True,True,False]
print('22: ', 22)
print('all(booleans): ', all(booleans))

#23
print('23: ', 23)
print('any(booleans): ', any(booleans))

#24
strings24 = ["cadenaInicial","cadema2","cadena3","cadenaFinal"]
result= ", ".join(strings24)

print('24: ', 24)
print(result)

#25
strings25 = list("cadenaInicial")
print('25: ', 25)
print('strings25: ', strings25)

#26
nums26 = [0,1,2,3,4,5,6,7,8,9]
print('26: ', 26)
print('nums26[2:6]: ', nums26[2:6])

#27
cities = ["Barcelona","Sydney","Singapur","New York"]
print('27: ', 27)
print('cities.pop(-1): ', cities.pop(-1))

#28
nums28 = [0,2,123,543,123,645]
print('28: ', 28)
print('max(nums28): ', max(nums28))

#29
nums29 = [0,2,123,543,123,645]
print('29: ', 29)
print('min(nums29): ', min(nums29))

#30
nums30 = [1123,543,2,765,21,456]
print('30: ', 30)
print('sorted(nums30): ', sorted(nums30))

#31
array31 = ["cadena1",0,2,5,"cadena2","cadena5"]
print('31: ', 31)
print('array31[2]: ', array31[2])

#32
strings32 = ["cadenaInicial","cadema2","cadena3","cadenaFinal"]

print('32: ', 32)
for index, value in enumerate(strings32):    print(f"Índice: {index}, Valor: {value}")

#33
nested_array33 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print('33: ', 33)
for i in nested_array33:
    for j in i:
        print(j)

#34
nums34 = [0,1,2,3,4,5,6]
print('34: ', 34)
print('nums34: ', nums34)
del nums34[2:5]

print('nums34: ', nums34)

#35
nums35 = [0,1,2,3,4,5,6]
bigger_than_5 = [num for num in nums35 if num > 5]

print('35: ', 35)
print('bigger_than_5: ', bigger_than_5)

#36
strings36 = ["cadenaInicial","cadema2","cadena3","cadenaFinal"]

result36 = []

for i in strings36:
    palabras = i.split()
    result36.append(palabras)

print('36: ', 36)
print('result36:', result36)

#37
tuple_array = ( 0,1,2,3,4,5,6 )
array = list(tuple_array)
array.append(99)
print('37: ', 37)
print('array.append(99): ', array)

#38
nums38 = [0,1,2,2,3,3,4,5,6]
print('38: ', 38)
print('list(set(nums38)): ', list(set(nums38)))

#39
nums39 = [0,1,2,3,4,5,6]
result = nums39[::-1]

print('39: ', 39)
print('result: ', result)

#40
nums40 = [0,1,2,3,4,5,6,7,8,9,10,11,12]

slices = 4

width_results = len(nums40) // slices

# range(start,end,step)
# para cada uno de los elementos (0) hasta el final del array(13),saltando en grupos de (3,25 = 3)
# cogemos el valor del array en ese grupo (nums40[0:0 + 3]) = [0,1,2]
# finalmente se almacena en una lista anidada
results = [nums40[i:i + width_results] for i in range(0, len(nums40), width_results)]

print('40: ', 40)
for value in results:
    print(value)

#41
nums41 = [0,1,20,3,4,4,4,8,8,9]
print('41: ', 41)
print('sum(nums41)/len(nums41): ', sum(nums41)/len(nums41))

#42
nums42 = [0, 10, 20, 30, 40, 100]

#farenheint = ((9/5) * C) + 32 
farenheint = [ ((9/5)*temp) + 32 for temp in nums42 ]

print('42: ', 42)
print('farenheint: ', farenheint)

#43
nums43 = [0,1,2,3,4,5,6,7,8,9,10]
result = [value for value in nums43 if value %2 == 0]

print('43: ', 43)
print('result: ', result)

#44
string44 = ["cadenaInicial","cadena1","cadena2","cadenaFinal"]
result = list(map(str.upper, string44))

print('44: ', 44)
print('result: ', result)

#45
nums45 = []

nums45.append(1)
nums45.append(2)
nums45.append(3)
nums45.append(4)

nums45.pop(0)

print('45: ', 45)
print('nums45: ', nums45 )

#46
strings46 = ["Ana", "Luis", "Elena", "Oscar", "Ignacio", "Ursula", "Pedro", "Eva", "Manuel"]

def starts_with_vocals(str):
    vocals = "AEIOUaeiou"
    return str[0] in vocals

print('46: ', 46)
print('list(filter(starts_with_vocals,strings46)): ', list(filter(starts_with_vocals,strings46)))

#47
nums47 = [0,1,2,2,3,3,4,5]
print('47: ', 47)
print('list(set(nums47)): ', list(set(nums47)))

#48
strings48 = ["A","An","Ana","Fernando","Luis"]
print('48: ', 48)
print('sorted(strings48, key = len): ', sorted(strings48, key = len))

#49
strings49 = ['Ana', 'Juan', 'Oscar', 'Isa', 'Luis', 'Ana', 'Carlos', 'Rosa']

grup_1 = [value for i, value in enumerate(strings49) if i % 2 == 0]
grup_2 = [value for i, value in enumerate(strings49) if i % 2 != 0]

print('49: ', 49)
print('grupo_1: ', grup_1)
print('grupo_2: ', grup_2)

#50
nums50 = [1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def mult (num1,num2):
    return num1 * num2

print('50: ', 50)
print('reduce(mult,nums50): ', reduce(mult,nums50))