from Users import User

class Loans:
    def __init__(self, id_user, id_book, fecha_inicio, fecha_fin, fecha_devolución):
        self.id_user = id_user
        self.id_book = id_book
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_devolución = fecha_devolución

    #todo disminuir cantidad de libros disponibles y formato fecha prestamo
    def _crear_id_prestamo(self):
        try:
            with open('db/biblioPrestamos.csv', 'r') as f:
                lines = f.readlines()
                last_id = 0
                for line in lines:
                    row = line.strip().split(',')
                    last_id = int(row[0])
                return last_id + 1
        except FileNotFoundError:
            # Si no existe el archivo, el ID será 1
            return 1

    def añadir_prestamo(self, id_user, id_book, fecha_inicio, fecha_fin, fecha_devolución):
        #comprobar que el libro e usuario existen,buscar_libro y buscar_usuario
        if User.buscar_libro(id_book) and User.buscar_usuario(id_user):
            id_prestamo = self._crear_id_prestamo()
            with open('db/biblioPrestamos.csv', 'a') as f:
                f.write(f'{id_prestamo},{id_user},{id_book},{fecha_inicio},{fecha_fin},{fecha_devolución}\n')
            return id_prestamo
        else:
            return False

    def borrar_prestamo(self, id_prestamo):
        with open('db/biblioPrestamos.csv', 'r') as f:
            lines = f.readlines()
        with open('db/biblioPrestamos.csv', 'w') as f:
            for line in lines:
                if line.split(',')[0] != id_prestamo:
                    f.write(line)
        return id_prestamo

    
    def buscar_prestamo(self, id_prestamo):
        with open('db/biblioPrestamos.csv', 'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.split(',')[0] == id_prestamo:
                print(line)
                return True
    
    def listar_prestamos(self):
        with open('db/biblioPrestamos.csv', 'r') as f:
            lines = f.readlines()
        for line in lines:
            print(line)
        return lines
