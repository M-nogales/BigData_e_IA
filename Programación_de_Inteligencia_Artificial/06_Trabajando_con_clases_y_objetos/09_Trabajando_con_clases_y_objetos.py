# 09. **Clase Mascota**
# Crea una clase Mascota con atributos como nombre, tipo de animal y edad.
# Métodos para alimentar, jugar y mostrar la energía de la mascota.

class Mascota:
    def __init__(self, nombre, tipo_animal, edad, energia):
        self.nombre = nombre
        self.tipo_animal = tipo_animal
        self.edad = edad
        self.energia = energia
    
    def alimentar(self, cantidad):
        self.energia += cantidad
    
    def jugar(self, cantidad):
        if cantidad <= self.energia:
            self.energia -= cantidad
        else:
            print("Energía insuficiente")
    
    def mostrar_energia(self):
        return self.energia
    
mascota1 = Mascota("Rex", "Perro policia", 5, 100)
print('mascota1.mostrar_energia(): ', mascota1.mostrar_energia())
mascota1.jugar(50)
print('mascota1.jugar(50): ')
print('mascota1.mostrar_energia(): ', mascota1.mostrar_energia())
mascota1.alimentar(30)
print('mascota1.alimentar(30): ')
print('mascota1.mostrar_energia(): ', mascota1.mostrar_energia())
