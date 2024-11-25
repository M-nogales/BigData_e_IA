class User:
    def __init__(self, nombre, edad, dni, correo_e, tlfno, dirección):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.correo_e = correo_e
        self.tlfno = tlfno
        self.dirección = dirección

    
    def crear_id_usuario(self):
        try:
            with open('db/biblioUsuarios.csv', 'r') as f:
                lines = f.readlines()
                last_id = 0
                for line in lines:
                    row = line.strip().split(',')
                    last_id = int(row[0])
                return last_id + 1
        except FileNotFoundError:
            # Si no existe el archivo, el ID será 1
            return 1
        
    #añadir usuario,se crea id y se añade a biblioUsuarios.csv
    def añadir_usuario(self, nombre, edad, dni, correo_e, tlfno, dirección):
        id_usuario = self.crear_id_usuario()
        with open('db/biblioUsuarios.csv', 'a') as f:
            f.write(f'{id_usuario},{nombre},{edad},{dni},{correo_e},{tlfno},{dirección}\n')
        return id_usuario
    
    #borrar usuario, se busca por id y se borra de biblioUsuarios.csv
    def borrar_usuario(self, id_usuario):
        with open('db/biblioUsuarios.csv', 'r') as f:
            lines = f.readlines()
        with open('db/biblioUsuarios.csv', 'w') as f:
            for line in lines:
                if line.split(',')[0] != id_usuario:
                    f.write(line)
        return id_usuario
    
    #modificar usuario, se busca por id y se modifica en biblioUsuarios.csv
    def modificar_usuario(self, id_usuario, nombre, edad, dni, correo_e, tlfno, dirección):
        with open('db/biblioUsuarios.csv', 'r') as f:
            lines = f.readlines()
        with open('db/biblioUsuarios.csv', 'w') as f:
            for line in lines:
                if line.split(',')[0] == id_usuario:
                    f.write(f'{id_usuario},{nombre},{edad},{dni},{correo_e},{tlfno},{dirección}\n')
                else:
                    f.write(line)

        return id_usuario,nombre

    #buscar usuario, se busca por id y se muestra por pantalla
    def buscar_usuario(self, id_usuario):
        with open('db/biblioUsuarios.csv', 'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.split(',')[0] == id_usuario:
                print(line)
                return True

    #listar usuarios, se muestra por pantalla todos los usuarios
    def listar_usuarios(self):
        with open('db/biblioUsuarios.csv', 'r') as f:
            lines = f.readlines()
        for line in lines:
            print(line)
    