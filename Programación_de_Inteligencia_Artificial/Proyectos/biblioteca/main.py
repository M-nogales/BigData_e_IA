
# Manejo de usuarios
from submenus import listar_prestamos, opciones_libros, opciones_usuarios,registrar_devolucion, registrar_prestamo


def mostrar_menu():
    print("Menú principal:")
    print("1. Gestión de libros")
    print("2. Gestión de usuarios")
    print("3. Registrar préstamo")
    print("4. Registrar devolución")
    print("5. Listados de préstamos")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Introduce una opción: ")
        match opcion:
            case "1":
                print("Gestión de libros seleccionado:")
                opciones_libros()
            case "2":
                print("Gestión de usuarios seleccionado:")
                opciones_usuarios()
            case "3":
                print("Registrar de préstamo seleccionado:")
                registrar_prestamo()
            case "4":
                print("Registrar de devolución seleccionado:")
                registrar_devolucion()
            case "5":
                print("Listados de préstamos seleccionado:")
                listar_prestamos()
            case "6":
                print("Salir")
                break
            case _:
                print("Opción no válida")

if __name__ == "__main__":
    main()