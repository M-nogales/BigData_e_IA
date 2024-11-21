'''
EJERCICIO 01
a) Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con
el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número
introducido.
b) Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt
con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre
por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando
de ello
c) Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt
con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero.
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.'''

def crear_tablas(num:int):
    with open(f"results/tabla-{num}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{num} x {i} = {num * i}\n")

def leer_tablas(num:int):
    try:
        with open(f"results/tabla-{num}.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("El fichero no existe.")

def leer_linea_tablas(num:int, linea:int):
    try:
        with open(f"results/tabla-{num}.txt", "r") as f:
            lines = f.readlines()
            if 0 < linea <= len(lines):
                print(lines[linea - 1])
            else:
                print("La línea no existe.")
    except FileNotFoundError:
        print("El fichero no existe.")

num = int(input("Dame un número entre 1 y 10 para crear un fichero con su .txt: "))
crear_tablas(num)
leer_tablas(num)
linea = int(input("Dame un número de línea para leer del txt anterior: "))
leer_linea_tablas(num, linea)