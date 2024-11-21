# 08. **Clase Smartphone**
# Implementa una clase Smartphone con atributos como marca, modelo, memoria, batería y nivel de batería actual.
# Métodos para llamar a un contacto, cargar el teléfono y mostrar el nivel de batería.

class Smartphone:
    def __init__(self, marca, modelo, memoria, bateria, nivel_bateria):
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria
        self.bateria = bateria
        self.nivel_bateria = nivel_bateria
    
    def llamar(self, contacto):
        if self.nivel_bateria > 0:
            self.nivel_bateria -= 1
            return f"Llamando a {contacto}..."
        else:
            return "Recarga al bixo ninio tu que eres un informatico de esos"
    
    def cargar(self, cantidad):
        if self.nivel_bateria + cantidad <= self.bateria:
            self.nivel_bateria += cantidad
        else:
            print("Carga excesiva")
    
    def mostrar_nivel_bateria(self):
        return self.nivel_bateria

smartphone1 = Smartphone("Samsung", "Galaxy S20", "128GB", 5000, 100)
print('smartphone1.mostrar_nivel_bateria(): ', smartphone1.mostrar_nivel_bateria())
print('smartphone1.llamar("Mamá"): ', smartphone1.llamar("Mamá"))
print('smartphone1.mostrar_nivel_bateria(): ', smartphone1.mostrar_nivel_bateria())
smartphone1.cargar(50)
print('smartphone1.cargar(50): ')
print('smartphone1.mostrar_nivel_bateria(): ', smartphone1.mostrar_nivel_bateria())