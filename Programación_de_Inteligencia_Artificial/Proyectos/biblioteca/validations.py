from datetime import datetime
import re
#! usuarios
def validar_nombre(nombre):
    if nombre.isalpha() or ' ' in nombre:
        return True
    print("El nombre solo debe contener letras y espacios.")
    return False

def validar_edad(edad):
    if edad.isdigit() and int(edad) > 0:
        return True
    print("La edad debe ser un número positivo.")
    return False


def validar_dni(dni):
    if re.fullmatch(r'\d{8}[A-Za-z]', dni):
        return True
    print("El DNI debe tener 8 dígitos seguidos de una letra.")
    return False

def validar_correo(correo_e):
    if re.fullmatch(r'[^@]+@[^@]+\.[^@]+', correo_e):
        return True
    print("El correo electrónico no es válido.")
    return False

def validar_tlfno(tlfno):
    if tlfno.isdigit() and 9 <= len(tlfno) <= 15:
        return True
    print("El teléfono debe contener entre 9 y 15 dígitos.")
    return False

def validar_direccion(direccion):
    if direccion.strip():
        return True
    print("La dirección no puede estar vacía.")
    return False

#! libros
def validar_titulo(title):
    if title.strip():
        return True
    print("El título no puede estar vacío.")
    return False

def validar_autor(author):
    if all(x.isalpha() or x.isspace() for x in author):
        return True
    print("El autor solo debe contener letras y espacios.")
    return False

def validar_anyo(anyo):
    current_year = datetime.now().year
    if anyo.isdigit() and 1500 <= int(anyo) <= current_year+1:
        return True
    print(f"El año debe ser un número entre 1500 y {current_year+1}.")
    return False

def validar_n_pags(n_pags):
    if n_pags.isdigit() and int(n_pags) > 0:
        return True
    print("El número de páginas debe ser un número positivo.")
    return False

def validar_genero(genero):
    if genero.strip():
        return True
    print("El género no puede estar vacío.")
    return False

def validar_editorial(editorial):
    if editorial.strip():
        return True
    print("La editorial no puede estar vacía.")
    return False

def validar_estado(estado):
    estados_validos = {"Malo", "Regular", "Bueno", "Excelente"}
    if estado.capitalize() in estados_validos:
        return True
    print("El estado debe ser uno de los siguientes: Malo, Regular, Bueno, Excelente.")
    return False

def validar_disponible(disponible):
    if disponible.capitalize() in {"True", "False"}:
        return True
    print("Disponible debe ser True o False.")
    return False

def validar_cantidad(cantidad):
    if cantidad.isdigit() and int(cantidad) > 0:
        return True
    print("La cantidad debe ser un número entero positivo.")
    return False
#! loans

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%d,%m,%Y")
        return True
    except ValueError:
        print("La fecha debe tener el formato dd,mm,yyyy.")
        return False
