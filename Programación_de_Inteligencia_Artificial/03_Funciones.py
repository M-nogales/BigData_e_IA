# loops can have else at the end

# for target_list in array:
#     pass
# else:
#     print("Hola mundo")

#todo * para x cantidad de datos,probar | parm = value para valor por defecto
def alumnos(nombre, apellido, *edad):
    print("nombre,apellido,edad: ", nombre, apellido, edad)


alumnos("juan", "magan", 22, 43)


def alumnos2(nombre, apellido, edad=18):
    print("nombre,apellido,edad: ", nombre, apellido, edad)


alumnos2("juan", "magan")

#! FIZZ-BUZZ
# 1-100
# MULTIPLOS 3 -- fizz
# MULTIPLOS 5 -- buzz
# MULTIPLOS 3-5 -- fizz-buzz


def fizzbuzz(length=101):
    for num in range(1, length):
        if num % 3 == 0 and num % 5 == 5:
            print("FIZZBUZZ")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)


# fizzbuzz()

#! Lambda

# cuadrado = lambda x: x * x

# valor = int(input("dame un valor"))

# print(cuadrado(valor))

#! Factorial

def factorial(num):

    if (num == 0 or num == 1):
        return 1
    
    return num * factorial(num-1)

print('factorial(5): ', factorial(5))

#