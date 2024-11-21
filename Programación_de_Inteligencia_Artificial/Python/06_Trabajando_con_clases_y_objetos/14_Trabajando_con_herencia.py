# 14. **Sistema de Facturación**
''' Crea una clase base Producto con atributos como nombre, precio y cantidad.
    Define clases derivadas como Electrodomestico, Ropa y Alimento, cada una con
    un atributo específico (por ejemplo, consumo_energetico para los
    electrodomésticos, talla para la ropa, y fecha_de_vencimiento para los
    alimentos).
    Crea un método en cada clase derivada que calcule el costo total basado en la cantidad
    y agregue alguna condición especial, como descuentos para ropa o fechas de
    caducidad para alimentos.
'''

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Electrodomestico(Producto):
    def __init__(self, nombre, precio, cantidad, consumo_energetico, descuento):
        super().__init__(nombre, precio, cantidad)
        self.consumo_energetico = consumo_energetico

    def costo_total(self, descuento):
        return self.precio * self.cantidad * descuento
    
class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def costo_total(self, descuento):
        return self.precio * self.cantidad * descuento

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_de_vencimiento):
        super().__init__(nombre, precio, cantidad)
        self.fecha_de_vencimiento = fecha_de_vencimiento

    def costo_total(self, cerca_de_caducidad):
        if cerca_de_caducidad:
            return self.precio * self.cantidad * 0.5
        return self.precio * self.cantidad * 0.8
    
electrodomestico = Electrodomestico("Lavadora", 500, 2, "A++", 0.9)
ropa = Ropa("Camisa", 20, 3, "M")
alimento = Alimento("Leche", 2, 5, "2022-12-31")

print(electrodomestico.costo_total(0.9))
print(ropa.costo_total(0.8))
print(alimento.costo_total(True))
