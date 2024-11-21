# 06. **Clase Estudiante**
# Define una clase Estudiante con atributos como nombre, curso, notas y promedio.
# Métodos para añadir una nueva nota, calcular el promedio y verificar si el estudiante aprobó.

class Estudiante:
    def __init__(self, nombre, curso, notas):
        self.nombre = nombre
        self.curso = curso
        self.notas = notas
        self.promedio = sum(notas) / len(notas)
    
    def anadir_nota(self, nota):
        self.notas.append(nota)
        self.promedio = sum(self.notas) / len(self.notas)
    
    def calcular_promedio(self):
        return self.promedio
    
    def aprobo(self):
        return self.promedio >= 5.0

estudiante1 = Estudiante("Juan", "1º ESO", [5, 8, 2.4, 4, 5.5])

print('estudiante1.calcular_promedio(): ', estudiante1.calcular_promedio())
print('estudiante1.aprobo(): ', estudiante1.aprobo())
estudiante1.anadir_nota(7)
print('estudiante1.anadir_nota(7): ')
print('estudiante1.calcular_promedio(): ', estudiante1.calcular_promedio())
print('estudiante1.aprobo(): ', estudiante1.aprobo())

