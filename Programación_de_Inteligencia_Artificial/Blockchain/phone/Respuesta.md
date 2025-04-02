# 📜 Respuestas a las Actividades del Proyecto 🧪

## ❓ Preguntas y Respuestas  

### 1️⃣ ¿Por qué se usa un hash en cada bloque del blockchain?
El hash se utiliza para garantizar la integridad y seguridad de los datos en cada bloque. Dado que cada bloque contiene un resumen criptográfico de su contenido, cualquier alteración en los datos cambiaría el hash, lo que permitiría detectar modificaciones en la cadena.

### 2️⃣ ¿Qué papel cumple el `hash_anterior` en la integridad de la cadena?
El `hash_anterior` vincula cada bloque con el anterior, formando una cadena encadenada criptográficamente. Si un bloque es alterado, su hash cambia y no coincidirá con el `hash_anterior` del siguiente bloque, rompiendo la integridad de la cadena y haciendo evidente la manipulación.

### 3️⃣ ¿Qué similitudes hay entre el juego del teléfono escacharrado y esta simulación?
Ambos ilustran cómo los mensajes pueden cambiar con el tiempo y las dificultades para mantener la información original. En el juego, los cambios ocurren por error humano; en blockchain, cualquier cambio intencionado es detectado gracias a los hashes.

### 4️⃣ ¿Se puede “arreglar” la cadena alterando todos los hashes? ¿Por qué eso no es viable en blockchains reales?
Sí, se podría recalcular cada hash desde el bloque alterado en adelante, pero en blockchains reales esto no es viable debido a la descentralización y la prueba de trabajo. En redes como Bitcoin, modificar un bloque requeriría rehacer todo el trabajo computacional de la cadena y superar el consenso de la red.

---

## ⚙️ Mejoras y Personalización  

### ✅ Personaliza el mensaje inicial
Modifiqué el bloque génesis para iniciar con un mensaje único.

```python
def crear_bloque_genesis():
    return Bloque(0, "GENESIS", "TODOS", "El mensaje original del teléfono escacharrado", "0")
```

### ✅ Control del porcentaje de error aleatorio
Implementé una función que introduce un error en un porcentaje de los mensajes transmitidos.

```python
import random

def alterar_mensaje(mensaje, probabilidad=0.1):
    if random.random() < probabilidad:
        return mensaje[::-1]  # Invierte el mensaje como error
    return mensaje
```

### ✅ Modo trampa: Modificar un bloque a propósito
Se añadió una función para modificar un bloque intencionalmente y probar la detección de alteraciones.

```python
def modificar_bloque(cadena, id, nuevo_mensaje):
    if 0 < id < len(cadena):
        cadena[id].mensaje = nuevo_mensaje
        cadena[id].hash = cadena[id].calcular_hash()
```

### ✅ Guardar la cadena en un `.txt`
Código para guardar la cadena en un archivo:

```python
def guardar_cadena_txt(cadena, nombre_archivo="cadena_blockchain.txt"):
    with open(nombre_archivo, 'w') as f:
        for bloque in cadena:
            f.write(json.dumps(bloque.mostrar_info(), indent=4) + "\n")
```

### ✅ Función de reparación de cadena
Si se detecta una alteración, recalcula los hashes desde el punto afectado.

```python
def reparar_cadena(cadena):
    for i in range(1, len(cadena)):
        cadena[i].hash_anterior = cadena[i - 1].hash
        cadena[i].hash = cadena[i].calcular_hash()
```

### ✅ Verificación de integridad
Una función que revisa si los hashes concuerdan.

```python
def verificar_integridad(cadena):
    for i in range(1, len(cadena)):
        if cadena[i].hash_anterior != cadena[i - 1].hash:
            return False
    return True
```