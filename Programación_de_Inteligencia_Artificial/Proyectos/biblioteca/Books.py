import csv
class Book:
    def __init__(self, title, author, anyo, n_pags, genero, editorial, estado, disponible, cantidad):
        self.title = title
        self.author = author
        self.anyo = anyo
        self.n_pags = n_pags
        self.genero = genero
        self.editorial = editorial
        self.estado = estado
        self.disponible = disponible
        self.cantidad = cantidad

    @classmethod
    def _crear_id_libro(self):
        try:
            with open('db/biblioLibros.csv', 'r', encoding="utf-8") as f:
                lines = csv.reader(f)
                last_id = 0
                for line in lines:
                    last_id = int(line[0])
                return last_id + 1
        except FileNotFoundError:
            # Si no existe el archivo, el ID será 1
            return 1
    
    @classmethod
    def añadir_libro(cls, title, author, anyo, n_pags, genero, editorial, estado, disponible, cantidad):
        with open('db/biblioLibros.csv', 'a',newline='',encoding="utf-8") as f:
            id_libro = cls._crear_id_libro()
            line = [id_libro, title, author, anyo, n_pags, genero, editorial, estado, disponible, cantidad]
            writer = csv.writer(f)
            writer.writerow(line)

    
    @classmethod
    def borrar_libro(cls, id_libro):
        with open('db/biblioLibros.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            libros = [row for row in reader if row[0] != id_libro]
        
        with open('db/biblioLibros.csv', 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(libros)
    
    @classmethod
    def modificar_libro(cls, id_libro, title, author, anyo, n_pags, genero, editorial, estado, disponible, cantidad):
        libros = []
        
        with open('db/biblioLibros.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == id_libro:
                    row = [id_libro, title, author, anyo, n_pags, genero, editorial, estado, disponible, cantidad]
                libros.append(row)

        with open('db/biblioLibros.csv', 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(libros)

    
    @classmethod
    def buscar_libro(cls, id_libro):
        with open('db/biblioLibros.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == id_libro:
                    print(row)
                    return True
        return False
    
    @classmethod
    def listar_libros(cls):
        with open('db/biblioLibros.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    
    @classmethod
    def aumentar_disminuir_cantidad(cls, id_libro, cantidad, instruccion):
        libros = []
        with open('db/biblioLibros.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == id_libro:
                    if instruccion == "aumentar":
                        row[-1] = str(int(row[-1]) + abs(cantidad))
                    else:
                        row[-1] = str(int(row[-1]) - abs(cantidad))
                libros.append(row)

        with open('db/biblioLibros.csv', 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(libros)

#todo integrar errores borrar y cantidad máxima
'''
    def aumentar_disminuir_cantidad(cls, id_libro, cantidad, instruccion):
        libros = []
        with open('db/biblioLibros.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == id_libro:
                    current_quantity = int(row[-1])
                    if instruccion == "aumentar":
                        row[-1] = str(current_quantity + abs(cantidad))
                    else:
                        if current_quantity == 0:
                            return False
                        row[-1] = str(current_quantity - abs(cantidad))
                libros.append(row)

        with open('db/biblioLibros.csv', 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(libros)

        return True
'''