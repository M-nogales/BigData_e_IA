# 12. **Sistema de Animales**
''' Define una clase base Animal con atributos como nombre y edad, y un método
    común hacer_sonido.
    Crea clases derivadas como Perro, Gato y Pájaro.
    Cada clase derivada debe sobrescribir el método hacer_sonido para producir el
    sonido específico de ese animal (ejemplo: el perro ladra, el gato maúlla).
    Añade métodos específicos, como correr para el perro o volar para el pájaro.
'''
class Animal:
    def __init__(self, nombre, edad, sonido):
        self.nombre = nombre
        self.edad = edad
        # self.sonido = sonido
    
    # def hacer_sonido(self):
    #     return f"{self.nombre} está: {self.sonido}"
    def hacer_sonido(self):
        return f"{self.nombre} está haciendo un sonido..."

class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "guau, guau")
    
    def correr(self):
        return f"{self.nombre} está corriendo..."
    
    def hacer_sonido(self):
        return "guau, guau"

class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "miau, miau")
    
    def saltar(self):
        return f"{self.nombre} está saltando..."

    def hacer_sonido(self):
        return "mau,mau"


class Pajaro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "pio, pio")
    
    def volar(self):
        return f"{self.nombre} está volando..."    

    def hacer_sonido(self):
        return "pio, pio"
    
perro = Perro("Rex", 3)
gato = Gato("Garfield", 5)
pajaro = Pajaro("Piolín", 1)

print(perro.hacer_sonido())
print(perro.correr())
print(gato.hacer_sonido())
print(gato.saltar())
print(pajaro.hacer_sonido())
print(pajaro.volar())