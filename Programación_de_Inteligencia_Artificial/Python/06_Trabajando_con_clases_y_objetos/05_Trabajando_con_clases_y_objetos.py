# 05. **Clase Restaurante**
# Crea una clase Restaurante con atributos como nombre, tipo de cocina y menú.
# Métodos para añadir un plato, mostrar el menú completo y tomar un pedido.

class Restaurante:
    def __init__(self, nombre, tipo_cocina, menu):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.menu = menu
    
    def anadir_plato(self, plato):
        self.menu.append(plato)
    
    def mostrar_menu(self):
        return self.menu
    
    def tomar_pedido(self, plato):
        if plato in self.menu:
            return f"Pedido anotado: {plato}"
    
    def con_permiso(self):
        return 'Con permiso caballero'
    
restaurante1 = Restaurante("La roja", "Española", ["Paella", "Tortilla", "Gazpacho manchego"])

restaurante1.anadir_plato("Callos")
print('restaurante1.anadir_plato("Callos"): ')
print('restaurante1.mostrar_menu(): ', restaurante1.mostrar_menu())
print('restaurante1.tomar_pedido("Paella"): ',restaurante1.tomar_pedido("Paella"))
print('restaurante1.tomar_pedido("Paella"): ',restaurante1.tomar_pedido("Paella"))
print('restaurante1.con_permiso(): ', restaurante1.con_permiso())
