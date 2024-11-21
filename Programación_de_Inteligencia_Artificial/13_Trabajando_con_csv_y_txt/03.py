'''
EJERCICIO 03
El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes
columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo
(precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la
jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de
euros).
1. Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los
datos del fichero por columnas.
2. Construir una función que reciba el diccionario devuelto por la función anterior y cree
un fichero en formato csv con el mínimo, el máximo y la media de dada columna.'''

#coti={"Acciona":dict({"nombre":"Acciona","Final":"95,95"})}
#coti={"nombre":dict({"nombre":"Acciona","nombre":"Acerinox"})}
#coti={"nombre":"Acciona","nombre":"Acerinox"}

def crear_diccionario(fichero):
    dictionary={}
    with open(fichero, "r", encoding="utf-8") as f:
        lines = f.readlines()
        # leemos las el nombre de las columnas
        keys = lines[0].strip().split(";")
        # creamos las claves del diccionario con los nombres de las columnas y los valores vacíos
        for key in keys:
            dictionary[key] = []
        # recorremos las lineas del fichero apartir del 1 y añadimos los valores a las claves correspondientes
        for line in lines[1:]:
            values = line.strip().split(";")
            for i in range(len(keys)):
                dictionary[keys[i]].append(values[i])

    return dictionary

def min_max_media_csv(diccionario):
    with open("results/cotizacion_resumen.csv", "w", encoding="utf-8") as f:
        f.write("Columna;Minimo;Maximo;Media\n")

        for key in diccionario.keys():
            if key != "Nombre":
                #! si pongo min como nombre de variable no me deja usar la función min
                minimum = min(diccionario[key])
                maximum = max(diccionario[key])
                avg = calc_media(diccionario[key])
                f.write(f"{key};{minimum};{maximum};{avg}\n")
    return "Fichero creado con éxito en results/cotizacion_resumen.csv"

def calc_media(key):
    sum = 0
    for value in key:
        if key != "Volumen":
            data_cleared = value.replace(".", "").replace(",", ".")
            sum += float(data_cleared)
        else:
            sum += int(value.replace(".", ""))
    return sum / len(key)


print('leer_fichero("data/cotizacion.csv"): ', crear_diccionario("data/cotizacion.csv"))
print('min_max_media_csv(leer_fichero("data/cotizacion.csv")): ', min_max_media_csv(crear_diccionario("data/cotizacion.csv")))