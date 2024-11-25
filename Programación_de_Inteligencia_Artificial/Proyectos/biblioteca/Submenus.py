from Users import User
from Books import Book
from Loans import Loans

def opciones_usuarios():
    print("Menú de Usuarios:")
    print("1 Añadir Usuario")
    print("2 Borrar Usuario")
    print("3 Modificar Usuario")
    print("4 Buscar Usuario")
    print("5 Listar Usuarios")
    print("6 Salir")
    
    while True:
        opcion = input("Introduce una opción: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            dni = input("DNI: ")
            correo_e = input("Correo electrónico: ")
            tlfno = input("Teléfono: ")
            dirección = input("Dirección: ")
            User.añadir_usuario(nombre, edad, dni, correo_e, tlfno, dirección)
        elif opcion == "2":
            id_usuario = input("ID del usuario a borrar: ")
            User.borrar_usuario(id_usuario)
        elif opcion == "3":
            id_usuario = input("ID del usuario a modificar: ")
            nombre = input("Nuevo nombre: ")
            edad = input("Nueva edad: ")
            dni = input("Nuevo DNI: ")
            correo_e = input("Nuevo correo electrónico: ")
            tlfno = input("Nuevo teléfono: ")
            dirección = input("Nueva dirección: ")
            User.modificar_usuario(id_usuario, nombre, edad, dni, correo_e, tlfno, dirección)
        elif opcion == "4":
            id_usuario = input("ID del usuario a buscar: ")
            User.buscar_usuario(id_usuario)
        elif opcion == "5":
            User.listar_usuarios()
        elif opcion == "6":
            print("Salir")
            break
        else:
            print("Opción no válida")

def opciones_libros():
    print("Menú de Libros:")
    print("1 Añadir Libro")
    print("2 Borrar Libro")
    print("3 Modificar Libro")
    print("4 Buscar Libro")
    print("5 Listar Libros")
    print("6 Salir")
    
    while True:
        opcion = input("Introduce una opción: ")
        if opcion == "1":
            title = input("Título: ")
            author = input("Autor: ")
            anyo = input("Año: ")
            n_pags = input("Número de páginas: ")
            genero = input("Género: ")
            editorial = input("Editorial: ")
            estado = input("Estado: ")
            disponible = input("Disponible: ")
            cantidad = input("Cantidad: ")
            Book.añadir_libro(title, author, anyo, n_pags, genero, editorial, estado, disponible, cantidad)
        elif opcion == "2":
            id_libro = input("ID del libro a borrar: ")
            Book.borrar_libro(id_libro)
        elif opcion == "3":
            id_libro = input("ID del libro a modificar: ")
            title = input("Nuevo título: ")
            author = input("Nuevo autor: ")
            anyo = input("Nuevo año: ")
            n_pags = input("Nuevo número de páginas: ")
            genero = input("Nuevo género: ")
            editorial = input("Nueva editorial: ")
            estado = input("Nuevo estado: ")
            disponible = input("Nuevo disponible: ")
            cantidad = input("Nueva cantidad: ")
            Book.modificar_libro(id_libro, title, author, anyo, n_pags, genero, editorial, estado, disponible, cantidad)
        elif opcion == "4":
            id_libro = input("ID del libro a buscar: ")
            Book.buscar_libro(id_libro)
        elif opcion == "5":
            Book.listar_libros()
        elif opcion == "6":
            print("Salir")
            break
        else:
            print("Opción no válida")

def registrar_prestamo():
    id_user = input("ID del usuario: ")
    id_book = input("ID del libro: ")
    fecha_inicio = input("Fecha de inicio: ")
    fecha_fin = input("Fecha de fin: ")
    fecha_devolución = input("Fecha de devolución: ")
    Loans.añadir_prestamo(id_user, id_book, fecha_inicio, fecha_fin, fecha_devolución)

def registrar_devolucion():
    id_prestamo = input("ID del préstamo: ")
    Loans.borrar_prestamo(id_prestamo)

def listar_prestamos():
    Loans.listar_prestamos()