# 04. **Clase Cafetera**
# Implementa una clase Cafetera con atributos como marca, capacidad máxima y nivel actual de café.
# Métodos para servir café, rellenar la cafetera y verificar si está vacía o llena.

class Cafetera:
    def __init__(self, marca, capacidad_maxima, nivel_actual):
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima
        self.nivel_actual = nivel_actual
    
    def servir_cafe(self, cantidad):
        if cantidad <= self.nivel_actual:
            self.nivel_actual -= cantidad
        else:
            print("Cafetera vacía")
    
    def rellenar_cafetera(self):
        self.nivel_actual = self.capacidad_maxima
    
    def esta_vacia(self):
        return self.nivel_actual == 0
    
    def esta_llena(self):
        return self.nivel_actual == self.capacidad_maxima
    
cafetera1 = Cafetera("Nespresso", 1000, 500)

cafetera1.servir_cafe(200)
print('cafetera1.servir_cafe(200): ')
print('cafetera1.nivel_actual: ', cafetera1.nivel_actual)
print('cafetera1.esta_vacia(): ', cafetera1.esta_vacia())
print('cafetera1.esta_llena(): ', cafetera1.esta_llena())
cafetera1.rellenar_cafetera()
print('cafetera1.rellenar_cafetera()')
print('cafetera1.nivel_actual: ', cafetera1.nivel_actual)