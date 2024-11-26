import csv
from books import Book
from users import User

class Loans:
    def __init__(self, id_user, id_book, fecha_inicio, fecha_fin, fecha_devolucion):
        self.id_user = id_user
        self.id_book = id_book
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_devolucion = fecha_devolucion
    
    @classmethod
    def _crear_id_prestamo(self):
        try:
            with open('db/biblioPrestamos.csv', 'r', encoding="utf-8") as f:
                lines = csv.reader(f)
                last_id = 0
                for line in lines:
                    last_id = int(line[0])
                return last_id + 1
        except FileNotFoundError:
            # Si no existe el archivo, el ID será 1
            return 1

    @classmethod
    def añadir_prestamo(cls, id_user, id_book, fecha_inicio, fecha_fin, fecha_devolucion):
        #comprobar que el libro e usuario existen,buscar_libro y buscar_usuario
        if Book.buscar_libro(id_book) and User.buscar_usuario(id_user):
            id_prestamo = cls._crear_id_prestamo()
            with open('db/biblioPrestamos.csv', 'a', newline='', encoding="utf-8") as f:
                row = [id_prestamo, id_user, id_book, fecha_inicio, fecha_fin, fecha_devolucion]
                writer = csv.writer(f)
                writer.writerow(row)
            Book.aumentar_disminuir_cantidad(id_book, 1, "disminuir")
            return id_prestamo
        else:
            return False
        
    @classmethod
    def borrar_prestamo(cls, id_prestamo):
        rows = []
        with open('db/biblioPrestamos.csv', 'r', newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0] == id_prestamo:
                    Book.aumentar_disminuir_cantidad(row[2], 1, "aumentar")
                else:
                    rows.append(row)

        with open('db/biblioPrestamos.csv', 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        
        return id_prestamo

    @classmethod
    def buscar_prestamo(cls, id_prestamo):
        with open('db/biblioPrestamos.csv', 'r', newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == id_prestamo:
                    print(row)
                    return True
        return False

    # Listar todos los préstamos
    @classmethod
    def listar_prestamos(cls):
        with open('db/biblioPrestamos.csv', 'r', newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            prestamos = list(reader)
            for prestamo in prestamos:
                print(prestamo)
        return prestamos