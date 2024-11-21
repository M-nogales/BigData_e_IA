'''
EJERCICIO 02
Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los
clientes de una empresa. El programa incorporar funciones crear el fichero con el listín si no
existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar
el teléfono de un cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el
nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una
línea distinta.'''

def add_data(nombre:str, telefono:str):
    with open("results/listin.txt", "a") as f:
        f.write(f"{nombre},{telefono}\n")

def delete_data(nombre:str):
    with open("results/listin.txt", "r") as f:
        lines = f.readlines()
    with open("results/listin.txt", "w") as f:
        for line in lines:
            if nombre not in line:
                f.write(line)

def read_data(nombre:str):
    with open("results/listin.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if nombre in line:
                print(line)

add_data("Juan", "123456789")
add_data("Pepe", "987654321")
add_data("Ana", "456789123")
delete_data("Pepe")
read_data("Juan")