
# Manejo de usuarios
from Users import hola as hola_users
# Manejo de libros
from Books import hola as hola_books
# Manejo de prestamos
from Loans import hola as hola_loans

def mostrar_menu():
    print("Menú principal:")
    print("1. Gestión Libros")
    print("2. Gestión Usuarios")
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
                print("Gestión Libros")
                hola_books()
            case "2":
                print("Gestión Usuarios")
                hola_users()
            case "3":
                print("Registrar Préstamo")
                hola_loans()
            case "4":
                print("Registrar Devolución")
            case "5":
                print("Listados de Préstamos")
            case "6":
                print("Salir")
                break
            case _:
                print("Opción no válida")

if __name__ == "__main__":
    main()