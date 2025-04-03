import hashlib
import json
 
class Bloque:
    def __init__(self, id, emisor, receptor, mensaje, hash_anterior=""):
        self.id = id
        self.emisor = emisor
        self.receptor = receptor
        self.mensaje = mensaje
        self.hash_anterior = hash_anterior
        self.hash = self.calcular_hash()
 
    def calcular_hash(self):
        contenido = f"{self.id}{self.emisor}{self.receptor}{self.mensaje}{self.hash_anterior}"
        return hashlib.sha256(contenido.encode()).hexdigest()
 
    def mostrar_info(self):
        return {
            "id": self.id,
            "emisor": self.emisor,
            "receptor": self.receptor,
            "mensaje": self.mensaje,
            "hash_anterior": self.hash_anterior,
            "hash": self.hash
        }
 
class Blockchain:
    def __init__(self):
        self.cadena = [self.crear_bloque_genesis()]
 
    def crear_bloque_genesis(self):
        return Bloque(0, "GENESIS", "TODOS", "Inicio de la cadena", "0")
 
    def agregar_bloque(self, emisor, receptor, mensaje):
        ultimo_bloque = self.cadena[-1]
        nuevo_bloque = Bloque(len(self.cadena), emisor, receptor, mensaje, ultimo_bloque.hash)
        self.cadena.append(nuevo_bloque)
 
    def es_valida(self):
        for i in range(1, len(self.cadena)):
            bloque_actual = self.cadena[i]
            bloque_anterior = self.cadena[i - 1]
 
            if bloque_actual.hash != bloque_actual.calcular_hash():
                return False
            if bloque_actual.hash_anterior != bloque_anterior.hash:
                return False
        return True
 
    def mostrar_transacciones(self):
        for bloque in self.cadena[1:]:  # omitimos el bloque génesis
            print(f"{bloque.emisor} → {bloque.receptor}: {bloque.mensaje}")
 
    def guardar_en_json(self, nombre_archivo):
        datos = [bloque.mostrar_info() for bloque in self.cadena]
        with open(nombre_archivo, 'w') as f:
            json.dump(datos, f, indent=4)
 
# Uso de ejemplo
bc = Blockchain()
bc.agregar_bloque("Alice", "Bob", "Hola, ¿cómo estás?")
bc.agregar_bloque("Bob", "Carol", "Estoy bien, gracias.")
bc.agregar_bloque("Carol", "Dave", "Nos vemos mañana.")
 
print("¿Blockchain válida?", bc.es_valida())
 
bc.mostrar_transacciones()
bc.guardar_en_json("cadena_blockchain.json")