## Simulación del Teléfono Escacharrado con Blockchain

###  ¿Por qué se usa un hash en cada bloque del blockchain?
El hash se utiliza para garantizar la integridad y seguridad de los datos en cada bloque. Dado que cada bloque contiene un resumen criptográfico de su contenido, cualquier alteración en los datos cambiaría el hash, lo que permitiría detectar modificaciones en la cadena.

###  ¿Qué papel cumple el `hash_anterior` en la integridad de la cadena?
El `hash_anterior` vincula cada bloque con el anterior, formando una cadena encadenada criptográficamente. Si un bloque es alterado, su hash cambia y no coincidirá con el `hash_anterior` del siguiente bloque, rompiendo la integridad de la cadena y haciendo evidente la manipulación.

###  ¿Qué similitudes hay entre el juego del teléfono escacharrado y esta simulación?
Ambos ilustran cómo los mensajes pueden cambiar con el tiempo y las dificultades para mantener la información original. En el juego, los cambios ocurren por error humano; en blockchain, cualquier cambio intencionado es detectado gracias a los hashes.

###  ¿Se puede “arreglar” la cadena alterando todos los hashes? ¿Por qué eso no es viable en blockchains reales?
Sí, se podría recalcular cada hash desde el bloque alterado en adelante, pero en blockchains reales esto no es viable debido a la descentralización y la prueba de trabajo. En redes como Bitcoin, modificar un bloque requeriría rehacer todo el trabajo computacional de la cadena y superar el consenso de la red.

---

## Mejoras y Personalización

### Personaliza el mensaje inicial
```python
def crear_bloque_genesis(self):
    return Bloque(0, "GENESIS", "TODOS", "Inicio de la cadena", "0")
```

### Control del porcentaje de error aleatorio y modificar un bloque a propósito
```python
def alterar_mensajes(self, probabilidad=0.2):
    for bloque in self.cadena[1:]:  # Omitimos el bloque génesis
        if random.random() < probabilidad:
            bloque.mensaje += " [ALTERADO]"
            bloque.hash = bloque.calcular_hash()
```

### Guardar la cadena en un `.txt`
```python
def guardar_en_txt(self, nombre_archivo="phone_blockchain.txt"):
    with open(nombre_archivo, 'w', encoding="utf-8") as f:
        for bloque in self.cadena:
            f.write(json.dumps(bloque.mostrar_info(), indent=4, ensure_ascii=False) + "\n")
```

### Función de reparación de cadena
Recalcula hashes desde un bloque específico hacia adelante:

```python
def reparar_cadena(self, desde):
    for i in range(desde, len(self.cadena)):
        hash_anterior = self.cadena[i-1].hash if i > 0 else ""
        self.cadena[i].hash_anterior = hash_anterior
        self.cadena[i].hash = self.cadena[i].calcular_hash()
```

### Verificación de integridad mejorada
Retorna estado de integridad y ubicación de fallos:

```python
def es_valida(self):
    for i in range(1, len(self.cadena)):
        bloque_actual = self.cadena[i]
        bloque_anterior = self.cadena[i-1]
        
        if bloque_actual.hash != bloque_actual.calcular_hash():
            return False, i
        if bloque_actual.hash_anterior != bloque_anterior.hash:
            return False, i
    return True, -1
```