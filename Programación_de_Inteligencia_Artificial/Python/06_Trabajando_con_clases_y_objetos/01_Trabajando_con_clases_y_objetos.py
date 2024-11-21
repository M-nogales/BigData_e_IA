# 01. **Clase Libro**
# Crea una clase Libro con atributos como título, autor, número de páginas, editorial y año de publicación.
#  Implementa métodos para mostrar información del libro y verificar si es largo o corto.

class Libro:
    def __init__(self, titulo, autor, paginas, editorial, publicacion):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.editorial = editorial
        self.publicacion = publicacion
    
    def __str__(self):
        return f"Libro: {self.titulo} de {self.autor} ({self.publicacion}) - {self.editorial}"
    
    def es_largo(self):
        return self.paginas > 300
    
libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 96, "Reynal & Hitchcock", 1943)
print('__str__')
print('libro1: ', libro1)
print('libro1.es_largo(): ', libro1.es_largo())
