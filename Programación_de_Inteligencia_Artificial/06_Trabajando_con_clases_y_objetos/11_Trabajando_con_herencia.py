# 11. **Sistema de Transporte**
''' Crea una clase base Vehiculo con atributos comunes como marca, modelo y año.
    Luego, define clases derivadas como Coche, Motocicleta y Bicicleta.
    Agrega métodos a las clases derivadas que simulen acciones específicas, como
    acelerar, frenar, o tocar_claxon.
    Ejemplo de método adicional para la bicicleta: pedalear.
'''
#! yo he visto más lógico que se hereden los metodos comunes
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def acelerar(self):
        return f"{self.marca} {self.modelo} está acelerando..."
    
    def frenar(self):
        return f"{self.marca} {self.modelo} está frenando..."
    
    def tocar_claxon(self):
        return f"{self.marca} {self.modelo} dice: pi,PIII..."


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
    

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
    
    def pedalear(self):
        return "Bici goes brummm, brummm..."
    
coche = Coche("Toyota", "Corolla", 2020)
moto = Motocicleta("Honda", "CBR", 2019)
bici = Bicicleta("Giant", "Escape", 2021)

print(coche.acelerar())
print(moto.frenar())
print(bici.tocar_claxon())
print(bici.pedalear())