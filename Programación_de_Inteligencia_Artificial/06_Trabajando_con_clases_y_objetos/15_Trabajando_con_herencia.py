# 15. **Sistema de Institución Educativa**
''' Crea una clase base Persona con atributos como nombre, edad y género.
    Define clases derivadas como Estudiante, Profesor y Director.
    Añade métodos para acciones específicas de cada rol: por ejemplo, enseñar() para el
    profesor, estudiar() para el estudiante y supervisar() para el director.
    Implementa en cada clase derivada un método informacion() que sobrescriba el de
    la clase base para mostrar detalles específicos de cada rol (por ejemplo, el curso del
    estudiante, la asignatura del profesor, etc.).
'''
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}"


class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, curso):
        super().__init__(nombre, edad, genero)
        self.curso = curso

    def estudiar(self):
        return f"{self.nombre} está estudiando..."

    def informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Curso: {self.curso}"
    

class Profesor(Persona):
    def __init__(self, nombre, edad, genero, asignatura):
        super().__init__(nombre, edad, genero)
        self.asignatura = asignatura

    def enseñar(self):
        return f"{self.nombre} está enseñando..."

    def informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Asignatura: {self.asignatura}"


class Director(Persona):
    def __init__(self, nombre, edad, genero, cargo):
        super().__init__(nombre, edad, genero)
        self.cargo = cargo

    def supervisar(self):
        return f"{self.nombre} está supervisando..."

    def informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Cargo: {self.cargo}"