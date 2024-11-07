# 13. **Jerarquía de Figuras Geométricas**
''' Crea una clase base Figura con atributos como color y tipo.
    Define clases derivadas como Circulo, Cuadrado y Triangulo.
    Cada clase derivada debe tener un método calcular_area que calcule el área según
    la figura.
    Agrega otro método calcular_perimetro para cada figura geométrica.
'''

class Figura:
    def __init__(self, color, tipo):
        self.color = color
        self.tipo = tipo

class Circulo(Figura):
    def __init__(self, color, tipo, radio):
        super().__init__(color, tipo)
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * 3.1416 * self.radio
    
class Cuadrado(Figura):
    def __init__(self, color, tipo, lado):
        super().__init__(color, tipo)
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Triangulo(Figura):
    def __init__(self, color, tipo, base, altura):
        super().__init__(color, tipo)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + (self.base ** 2 + self.altura ** 2) ** 0.5
    
circulo = Circulo("rojo", "círculo", 5)
cuadrado = Cuadrado("azul", "cuadrado", 4)
triangulo = Triangulo("verde", "triángulo", 3, 4)

print(circulo.calcular_area())
print(circulo.calcular_perimetro())
print(cuadrado.calcular_area())
print(cuadrado.calcular_perimetro())
print(triangulo.calcular_area())
print(triangulo.calcular_perimetro())