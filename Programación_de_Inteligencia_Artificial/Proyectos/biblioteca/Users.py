import csv
class User:
    def __init__(self, nombre, edad, dni, correo_e, tlfno, direccion):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.correo_e = correo_e
        self.tlfno = tlfno
        self.direccion = direccion

    @classmethod
    def crear_id_usuario(self):
        try:
            with open('db/biblioUsuarios.csv', 'r', encoding="utf-8") as f:
                lines = csv.reader(f)
                last_id = 0
                for line in lines:
                    last_id = int(line[0])
                return last_id + 1
        except FileNotFoundError:
            # Si no existe el archivo, el ID será 1
            return 1
        
    #añadir usuario,se crea id y se añade a biblioUsuarios.csv
    @classmethod
    def añadir_usuario(cls, nombre, edad, dni, correo_e, tlfno, direccion):
        try:
            id_usuario = cls.crear_id_usuario()
            with open('db/biblioUsuarios.csv', 'a', newline='') as f:
                line = [id_usuario, nombre, edad, dni, correo_e, tlfno, direccion]
                writer = csv.writer(f)
                writer.writerow(line)
            print("Usuario añadido exitosamente\n")
        except:
            print("Error al añadir un usuario")

    #borrar usuario, se busca por id y se borra de biblioUsuarios.csv
    @classmethod
    def borrar_usuario(cls, id_usuario):
        try:
            with open('db/biblioUsuarios.csv', 'r', newline='') as f:
                reader = csv.reader(f)
                rows = [row for row in reader if row and row[0] != id_usuario]
            
            with open('db/biblioUsuarios.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            
            print("Usuario",id_usuario,"eliminado correctamente\n")
            return id_usuario
        except:
            print("Error al eliminar un usuario")
    
    #modificar usuario, se busca por id y se modifica en biblioUsuarios.csv
    @classmethod
    def modificar_usuario(cls, id_usuario, nombre, edad, dni, correo_e, tlfno, direccion):
        try:
            with open('db/biblioUsuarios.csv', 'r', newline='') as f:
                reader = csv.reader(f)
                rows = []
                for row in reader:
                    if row[0] == id_usuario:
                        rows.append([id_usuario, nombre, edad, dni, correo_e, tlfno, direccion])
                    else:
                        rows.append(row)

            with open('db/biblioUsuarios.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            print("Usuario modificado correctamente\n")
            return id_usuario, nombre
        except:
            print("Error al actualizar un usuario")

    #buscar usuario, se busca por id y se muestra por pantalla
    @classmethod
    def buscar_usuario(cls, id_usuario):
        try:
            with open('db/biblioUsuarios.csv', 'r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] == id_usuario:
                        print(row)
                        return True
                    else:
                        print("Usuario",id_usuario,"no encontrado\n")
            return False
        except:
            print("Error al buscar un usuario")

    #listar usuarios, se muestra por pantalla todos los usuarios
    @classmethod
    def listar_usuarios(cls):
        try:
            with open('db/biblioUsuarios.csv', 'r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    print(row)
            print("Todos los usuarios listados!\n")
        except:
            print("Error al listar todos los usuarios")