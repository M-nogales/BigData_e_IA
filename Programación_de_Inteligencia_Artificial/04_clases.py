class persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido},{self.edad} años"
    
    def __len__(self):
        return self.edad
    
    def __eq__(self, persona2):
        return self.nombre == persona2.nombre and self.apellido == persona2.apellido and self.edad == persona2.edad
    
    def __gt__(self,persona2):
        return self.edad > persona2.edad
    
    def cumplir(self):
        self.edad +=1
        print(f"feliz cumpleaños, {self.nombre} ({self.edad})")
    
    def __del__(self):
        print(f"Eliminado, {self.nombre}")
        


# p1 = persona("Juan","Magan",22)
# p2 = persona("Juanes","Lopez",45)

# print(p1)
# print(p2)

# print("longitud p1 | __len__",len(p1))
# print("longitud p2",len(p2))
# print("Comparación edad | __eq__", p1 == p2)
# print("p1>p2 | __gt__", p1 > p2)
# p1.cumplir()
# del p1

print('------------------------: ')

class vehiculo:
    def __init__(self,marca:str,modelo,tipo,year,litros,vmax,vactual,encendido):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.year = int(year)
        self.litros = float(litros)
        self.vmax = int(vmax)
        self.vactual = vactual
        self.encendido = bool(encendido)

    def __str__(self):
        estado_encendido = "Encendido" if self.encendido else "Apagado"
        return (f"Vehículo: {self.marca} {self.modelo}\n"
                f"Tipo: {self.tipo}\n"
                f"Año: {self.year}\n"
                f"Capacidad del tanque: {self.litros} litros\n"
                f"Velocidad máxima: {self.vmax} km/h\n"
                f"Velocidad actual: {self.vactual} km/h\n"
                f"Estado: {estado_encendido}")
    
    def encender(self):
        if self.litros > 0:
            self.encender = True
            print("Encendido")
        else:
            print("Me falta gasoil")

    def apagar(self):
        if self.encendido:
            self.encender = False
            print("apagado")
            self.vactual = 0
        else:
            print("Ya estaba apagado")

    def acelerar(self,incr):
        if self.encender:
            self.vactual += incr
            print('vas a : ', self.vactual, "kms/s")
        else:
            print("Coche apagado. No puedes acelerar")

    def frenar(self,dcr):
        if self.encender:
            if dcr>=self.vactual:
                self.vactual = 0
                print("Coche parado")
            else:
                self.vactual -= dcr
                print('velocidad actual: ', self.vactual,"Km/s franado de:", dcr)
        else:
            print("Enciende el vehiculo con anterioridad")

    def llenar_tanque(self,litros):
        self.litros += litros
        print("Coche rellenado: ",self.litros,"L")
            

toyota = vehiculo(marca="Toyota", modelo="Corolla", tipo="Coche", year=2020, litros=50, vmax=180, vactual=60, encendido=True)
tesla = vehiculo(marca="Tesla", modelo="Model 3", tipo="Coche", year=2021, litros=0, vmax=260, vactual=90, encendido=True)

print(toyota)

toyota.llenar_tanque(30)
tesla.llenar_tanque(0)

toyota.encender()
toyota.acelerar(100)
toyota.frenar(20)
toyota.acelerar(90)
toyota.frenar(110)
toyota.apagar()
print(toyota)