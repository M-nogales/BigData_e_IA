from validations import *
from users import User
from books import Book
from loans import Loans

def opciones_usuarios():
    
    while True:
        print("Menú de Usuarios:")
        print("1 Añadir Usuario")
        print("2 Borrar Usuario")
        print("3 Modificar Usuario")
        print("4 Buscar Usuario")
        print("5 Listar Usuarios")
        print("6 Salir")
        opcion = input("Introduce una opción: ")

        if opcion == "1":
            while True:
                nombre = input("Nombre: ")
                if validar_nombre(nombre):
                    break
                
            while True:
                edad = input("Edad: ")
                if validar_edad(edad):
                    break
                
            while True:
                dni = input("DNI: ")
                if validar_dni(dni):
                    break
                
            while True:
                correo_e = input("Correo electrónico: ")
                if validar_correo(correo_e):
                    break
                
            while True:
                tlfno = input("Teléfono: ")
                if validar_tlfno(tlfno):
                    break
                
            while True:
                direccion = input("Dirección: ")
                if validar_direccion(direccion):
                    break

            User.añadir_usuario(nombre, edad, dni, correo_e, tlfno, direccion)

        elif opcion == "2":

            id_usuario = input("ID del usuario a borrar: ")

            User.borrar_usuario(id_usuario)

        elif opcion == "3":
            while True:
                id_usuario = input("ID del usuario a modificar: ")
                if User.buscar_usuario(id_usuario):
                    break

            while True:
                nombre = input("nuevo nombre: ")
                if validar_nombre(nombre):
                    break
                
            while True:
                edad = input("nueva edad: ")
                if validar_edad(edad):
                    break
                
            while True:
                dni = input("nuevo DNI: ")
                if validar_dni(dni):
                    break
                
            while True:
                correo_e = input("nuevo correo electrónico: ")
                if validar_correo(correo_e):
                    break
                
            while True:
                tlfno = input("nuevo teléfono: ")
                if validar_tlfno(tlfno):
                    break
                
            while True:
                direccion = input("nuevo dirección: ")
                if validar_direccion(direccion):
                    break

            User.modificar_usuario(id_usuario, nombre, edad, dni, correo_e, tlfno, direccion)

        elif opcion == "4":

            while True:
                id_usuario = input("ID del usuario a modificar: ")
                if id_usuario.isdigit() and int(id_usuario) > 0:
                    break

            User.buscar_usuario(id_usuario)

        elif opcion == "5":

            User.listar_usuarios()

        elif opcion == "6":
            print("Salir")
            break
        else:
            print("Opción no válida")

def opciones_libros():
    
    while True:
        print("Menú de Libros:")
        print("1 Añadir Libro")
        print("2 Borrar Libro")
        print("3 Modificar Libro")
        print("4 Buscar Libro")
        print("5 Listar Libros")
        print("6 Salir")

        opcion = input("Introduce una opción: ")

        if opcion == "1":

            while True:
                title = input("Título: ")
                if validar_titulo(title):
                    break

            while True:
                author = input("Autor: ")
                if validar_autor(author):
                    break

            while True:
                anyo = input("Año: ")
                if validar_anyo(anyo):
                    break
                
            while True:
                n_pags = input("Número de páginas: ")
                if validar_n_pags(n_pags):
                    break
                
            while True:
                genero = input("Género: ")
                if validar_genero(genero):
                    break
                
            while True:
                editorial = input("Editorial: ")
                if validar_editorial(editorial):
                    break
                
            while True:
                estado = input("Estado(Malo,Regular,Bueno,Excelente): ")
                if validar_estado(estado):
                    break
                
            while True:
                disponible = input("Disponible(True o False): ")
                if validar_disponible(disponible):
                    break
                
            while True:
                cantidad = input("Cantidad añadida: ")
                if validar_cantidad(cantidad):
                    break

            Book.añadir_libro(title, author, anyo, n_pags, genero, editorial, estado.capitalize(), disponible, cantidad)

        elif opcion == "2":

            while True:
                id_libro = input("ID del libro a borrar: ")
                if id_libro.isdigit() and int(id_libro) > 0:
                    break
            Book.borrar_libro(id_libro)

        elif opcion == "3":

            while True:
                id_libro = input("ID del libro a modificar: ")
                if id_libro.isdigit() and int(id_libro) > 0:
                    break
            while True:
                title = input("nuevo título: ")
                if validar_titulo(title):
                    break

            while True:
                author = input("nuevo autor: ")
                if validar_autor(author):
                    break

            while True:
                anyo = input("nuevo año de publicación : ")
                if validar_anyo(anyo):
                    break
                
            while True:
                n_pags = input("nuevo número de páginas: ")
                if validar_n_pags(n_pags):
                    break
                
            while True:
                genero = input("nuevo género: ")
                if validar_genero(genero):
                    break
                
            while True:
                editorial = input("nueva editorial: ")
                if validar_editorial(editorial):
                    break
                
            while True:
                estado = input("nuevo estado(Malo,Regular,Bueno,Excelente): ")
                if validar_estado(estado):
                    break
                
            while True:
                disponible = input("modificar disponible(True o False): ")
                if validar_disponible(disponible):
                    break
                
            while True:
                cantidad = input("modificar cantidad: ")
                if validar_cantidad(cantidad):
                    break

            Book.modificar_libro(id_libro, title, author, anyo, n_pags, genero, editorial, estado, disponible, cantidad)

        elif opcion == "4":

            while True:
                id_libro = input("ID del libro a buscar: ")
                if id_libro.isdigit() and int(id_libro) > 0:
                    break
            Book.buscar_libro(id_libro)

        elif opcion == "5":

            Book.listar_libros()

        elif opcion == "6":

            print("Salir")
            break
        else:
            print("Opción no válida")

def registrar_prestamo():

    while True:
        id_usuario = input("ID del usuario: ")
        if id_usuario.isdigit() and int(id_usuario) > 0:
            break

    while True:
        id_libro = input("ID del libro: ")
        if id_libro.isdigit() and int(id_libro) > 0:
            break
        
    while True:
        fecha_inicio = input("Fecha de inicio (dd,mm,yyyy): ")
        if validar_fecha(fecha_inicio):
            break

    while True:
        fecha_fin = input("Fecha de fin (dd,mm,yyyy): ")
        if validar_fecha(fecha_fin):
            break

    while True:
        fecha_devolucion = input("Fecha de devolución (dd,mm,yyyy): ")
        if validar_fecha(fecha_devolucion):
            break


    Loans.añadir_prestamo(id_usuario, id_libro, fecha_inicio, fecha_fin, fecha_devolucion)

def registrar_devolucion():

    while True:
        id_prestamo = input("ID del prestamo: ")
        if id_prestamo.isdigit() and int(id_prestamo) > 0:
            break
    Loans.borrar_prestamo(id_prestamo)

def listar_prestamos():
    Loans.listar_prestamos()