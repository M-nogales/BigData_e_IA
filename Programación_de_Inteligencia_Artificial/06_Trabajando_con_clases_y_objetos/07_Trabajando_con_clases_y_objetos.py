# 07. **Clase Pelota**
# Crea una clase Pelota con atributos como tipo de deporte, tamaño y presión de aire.
#  Métodos para inflar, desinflar la pelota y mostrar el estado de la presión actual.

class Pelota:
    def __init__(self, deporte, width, presion):
        self.deporte = deporte
        self.tamano = width
        self.presion = presion
    
    def inflar(self, cantidad):
        self.presion += cantidad
    
    def desinflar(self, cantidad):
        if cantidad <= self.presion:
            self.presion -= cantidad
        else:
            print("Presión insuficiente")
    
    def mostrar_presion(self):
        return self.presion

pelota1 = Pelota("Futbol", 22, 10)
print('pelota1.mostrar_presion(): ', pelota1.mostrar_presion())
pelota1.inflar(5)
print('pelota1.inflar(5): ')
print('pelota1.mostrar_presion(): ', pelota1.mostrar_presion())
pelota1.desinflar(8)
print('pelota1.desinflar(8): ')
print('pelota1.mostrar_presion(): ', pelota1.mostrar_presion())