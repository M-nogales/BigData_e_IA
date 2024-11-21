# 02. **Clase Persona**
# Define una clase Persona con atributos como nombre, edad, género y altura.
#  Implementa métodos que permitan saludar, verificar si es mayor de edad y mostrar su edad en 5 años.

class Persona:
    def __init__(self, nombre, edad, genero, altura):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.altura = altura
    
    
    def saludar(self):
        return f"Hola, soy {self.nombre}."
    
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
    def edad_en_5_anios(self):
        return self.edad + 5
    
persona1 = Persona("Juan", 25, "Masculino", 1.75)

print('persona1.saludar(): ', persona1.saludar())
print('persona1.es_mayor_de_edad(): ', persona1.es_mayor_de_edad())
print('persona1.edad_en_5_anios(): ', persona1.edad_en_5_anios())
