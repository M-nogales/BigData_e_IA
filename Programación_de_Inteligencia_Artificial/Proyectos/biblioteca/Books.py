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

    def _crear_id_libro(self):
        try:
            with open('db/biblioLibros.csv', 'r') as f:
                lines = f.readlines()
                last_id = 0
                for line in lines:
                    row = line.strip().split(',')
                    last_id = int(row[0])
                return last_id + 1
        except FileNotFoundError:
            # Si no existe el archivo, el ID será 1
            return 1
    
    def añadir_libro(self, title, author, anyo, n_pags, genero, editorial, estado, disponible, cantidad):
        id_libro = self._crear_id_libro()
        with open('db/biblioLibros.csv', 'a') as f:
            f.write(f'{id_libro},{title},{author},{anyo},{n_pags},{genero},{editorial},{estado},{disponible},{cantidad}\n')
        return id_libro
    
    def borrar_libro(self, id_libro):
        with open('db/biblioLibros.csv', 'r') as f:
            lines = f.readlines()
        with open('db/biblioLibros.csv', 'w') as f:
            for line in lines:
                if line.split(',')[0] != id_libro:
                    f.write(line)
        return id_libro
    
    def modificar_libro(self, id_libro, title, author, anyo, n_pags, genero, editorial, estado, disponible, cantidad):
        with open('db/biblioLibros.csv', 'r') as f:
            lines = f.readlines()
        with open('db/biblioLibros.csv', 'w') as f:
            for line in lines:
                if line.split(',')[0] == id_libro:
                    f.write(f'{id_libro},{title},{author},{anyo},{n_pags},{genero},{editorial},{estado},{disponible},{cantidad}\n')
                else:
                    f.write(line)

        return id_libro,title
    
    def buscar_libro(self, id_libro):
        with open('db/biblioLibros.csv', 'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.split(',')[0] == id_libro:
                print(line)
                return True

    #todo aumentar o disminuir cantidad de libros disponibles
