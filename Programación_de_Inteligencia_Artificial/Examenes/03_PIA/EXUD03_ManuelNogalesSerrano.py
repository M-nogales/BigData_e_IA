import json
import hashlib
import datetime
import time
import random
import os

# --- Configuración ---
BATCH_SIZE = 3                   # Número de lecturas de sensores por batch/bloque añadido manualmente
CLOUD_DATA_FILE = 'cloud_data.json' # Archivo simulando almacenamiento en la nube
DEVICE_IDS = ["Sensor_Oficina", "Sensor_Almacen", "Sensor_Exterior"]

# --- Clase para Bloques de la Blockchain ---
class Block:
    def __init__(self, index, timestamp, data_hash, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data_hash = data_hash # Hash del batch de datos IoT almacenado en la nube
        self.previous_hash = previous_hash

    def __str__(self):
        return (f"  Block #{self.index} [Timestamp: {self.timestamp}, "
                f"Hash Datos: {self.data_hash[:10]}..., " # Mostrar solo parte del hash
                f"Hash Anterior: {self.previous_hash[:10]}...]")

# --- Clase para la Blockchain Simulada ---
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # El primer bloque, sin datos asociados reales
        return Block(0, datetime.datetime.now().isoformat(), "genesis_hash_datos_0", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        self.chain.append(new_block)

    def display_chain(self):
        print("\n--- Blockchain Actual ---")
        if len(self.chain) == 0:
             print("La blockchain está vacía.")
        else:
            for block in self.chain:
                print(block)
        print("-------------------------\n")

    def get_block_by_index(self, index):
        for block in self.chain:
            if block.index == index:
                return block
        return None

# --- Funciones del Ecosistema ---

def simulate_iot_device(device_id):
    """Simula un dispositivo IoT generando datos de sensor."""
    data = {
        'device_id': device_id,
        'timestamp': datetime.datetime.now().isoformat(),
        'temperature': round(random.uniform(15.0, 30.0), 2),
        'humidity': round(random.uniform(30.0, 70.0), 2),
        'light': round(random.uniform(100, 1000), 2),
        'c02': round(random.uniform(300, 500), 2),
    }
    return data

def initialize_cloud_file(filename):
    """Asegura que el archivo JSON existe y contiene una lista vacía si es nuevo."""
    if not os.path.exists(filename):
        try:
            with open(filename, 'w') as f:
                json.dump([], f)
            print(f"Archivo '{filename}' no encontrado. Se ha creado vacío.")
        except Exception as e:
             print(f"Error al inicializar {filename}: {e}")
    else:
        try:
            with open(filename, 'r') as f:
                content = f.read()
                if not content: # Si está vacío
                     with open(filename, 'w') as fw: # Escribir lista vacía
                         json.dump([], fw)
                else:
                    data = json.loads(content)
                    if not isinstance(data, list):
                        print(f"Advertencia: {filename} no contenía una lista JSON. Se ha reiniciado.")
                        with open(filename, 'w') as fw:
                             json.dump([], fw)
        except json.JSONDecodeError:
             print(f"Advertencia: {filename} contiene JSON inválido. Se ha reiniciado.")
             with open(filename, 'w') as fw:
                  json.dump([], fw)
        except Exception as e:
             print(f"Error al verificar {filename}: {e}. Se ha reiniciado.")
             with open(filename, 'w') as fw:
                  json.dump([], fw)


def save_to_cloud(data_batch, filename):
    """Añade un batch de datos al archivo JSON simulado."""
    all_data = load_from_cloud(filename) # cargamos la lista actual

    # Asegurarnos que all_data es una lista
    if not isinstance(all_data, list):
        print(f"Advertencia: El contenido de {filename} no era una lista. Reiniciando antes de añadir.")
        all_data = []

    all_data.extend(data_batch) # Añade el nuevo batch

    try:
        with open(filename, 'w') as f:
            json.dump(all_data, f, indent=4)
        # La confirmación se hace en la función del menú
    except Exception as e:
        print(f"Error escribiendo en {filename}: {e}")
        return False
    return True

def load_from_cloud(filename):
    """Carga todos los datos desde el archivo JSON simulado."""
    initialize_cloud_file(filename) # Asegura que existe y es válido antes de leer
    try:
        with open(filename, 'r') as f:
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        print(f"Error: El archivo {filename} no contiene JSON válido.")
        return [] # Devuelve lista vacía si hay error
    except Exception as e:
        print(f"Error leyendo {filename}: {e}")
        return []

def hash_data_batch(data_batch):
    """Calcula el hash SHA-256 de un batch de datos."""
    if not data_batch: # Evitar error si el batch está vacío
         return None
    batch_string = json.dumps(data_batch, sort_keys=True).encode('utf-8')
    return hashlib.sha256(batch_string).hexdigest()

def verify_data_integrity(blockchain, cloud_filename, batch_size):
    """Verifica si los hashes en la blockchain coinciden con los datos en la nube."""
    print("\n--- Verificación de Integridad ---")
    cloud_data = load_from_cloud(cloud_filename)
    if not cloud_data and len(blockchain.chain) > 1:
         print(f"Advertencia: Hay bloques en la cadena pero no hay datos en '{cloud_filename}'.")


    is_valid = True
    # Ignoramos el bloque génesis (índice 0)
    if len(blockchain.chain) <= 1 and not cloud_data:
         print("Blockchain solo tiene bloque génesis y no hay datos en la nube. Nada que verificar.")
         return True

    for i in range(1, len(blockchain.chain)):
        block = blockchain.chain[i]
        print(f"Verificando Bloque #{block.index}...")

        # Determinar qué datos de la nube corresponden a este bloque
        start_index = (block.index - 1) * batch_size
        end_index = start_index + batch_size

        if start_index >= len(cloud_data):
             print(f"  ERROR: Faltan datos en '{cloud_filename}' para el bloque {block.index} (se esperaban registros {start_index}-{end_index-1}).")
             is_valid = False
             continue # Pasar al siguiente bloque

        current_batch_data = cloud_data[start_index:end_index]

        if not current_batch_data:
             print(f"  ERROR: No se encontraron datos en '{cloud_filename}' para el rango del bloque {block.index}.")
             is_valid = False
             continue

        # Recalcular el hash del batch de datos actual de la nube
        recalculated_data_hash = hash_data_batch(current_batch_data)
        print(f"  Hash Datos (Nube): {recalculated_data_hash}")
        print(f"  Hash Datos (Block): {block.data_hash}")

        if recalculated_data_hash != block.data_hash:
            print(f"  ¡¡INCONGRUENCIA DETECTADA!! El hash de los datos en '{cloud_filename}' (registros {start_index}-{end_index-1}) "
                  f"NO coincide con el hash almacenado en el Bloque #{block.index}.")
            is_valid = False
        else:
            print(f"  OK: Hash de datos coincide para el Bloque #{block.index}.")

        # Aquí podríamos añadir la verificación del previous_hash si calculáramos el hash del bloque entero

    print("----------------------------------")
    if is_valid:
        print("Resultado: La integridad de los datos registrados en la blockchain es VÁLIDA.")
    else:
        print("Resultado: ¡¡La integridad de los datos está COMPROMETIDA!!")
    print("----------------------------------\n")
    return is_valid


# --- Funciones del Menú ---

def display_menu():
    """Muestra las opciones del menú."""
    print("\n--- Menú Ecosistema Convergente (IoT+Cloud+Blockchain) ---")
    print("1. Añadir Nuevo Lote de Datos IoT")
    print("2. Mostrar Datos Almacenados (Nube)")
    print("3. Mostrar Blockchain")
    print("4. Alterar Datos en la Nube (para pruebas)")
    print("5. Verificar Integridad de Datos")
    print("0. Salir")
    print("--------------------------------------------------------")

def add_new_batch(blockchain, cloud_filename, batch_size, device_ids):
    """Simula, guarda, hashea y añade un nuevo batch de datos."""
    print("\n--- Añadiendo Nuevo Lote ---")
    current_batch = []
    print(f"Generando {batch_size} lecturas de sensores...")
    for i in range(batch_size):
        device_id = random.choice(device_ids)
        iot_data = simulate_iot_device(device_id)
        current_batch.append(iot_data)
        print(f"  Lectura {i+1}/{batch_size}: {iot_data}")
        time.sleep(0.2) 

    # 1. Guardar en la "nube"
    if save_to_cloud(current_batch, cloud_filename):
        print(f"\n[Cloud] Lote de {len(current_batch)} registros guardado en {cloud_filename}")

        # 2. Hashear batch
        batch_hash = hash_data_batch(current_batch)
        print(f"[Hashing] Hash del batch: {batch_hash}")

        # 3. Crear y añadir bloque
        previous_block = blockchain.get_latest_block()
        new_block_index = previous_block.index + 1
        # usamos el data_hash anterior como referencia de enlace
        new_block = Block(index=new_block_index,
                          timestamp=datetime.datetime.now().isoformat(),
                          data_hash=batch_hash,
                          previous_hash=previous_block.data_hash)
        blockchain.add_block(new_block)
        print(f"[Blockchain] Bloque #{new_block.index} añadido a la cadena.")
    else:
        print("Error: No se pudo guardar el batch en la nube. No se añadió bloque.")
    print("----------------------------\n")


def display_cloud_data(cloud_filename):
    """Muestra los datos del archivo JSON."""
    print(f"\n--- Datos Almacenados en '{cloud_filename}' ---")
    all_cloud_data = load_from_cloud(cloud_filename)
    if not all_cloud_data:
        print("No hay datos almacenados.")
    else:
        print(json.dumps(all_cloud_data, indent=2))
        print(f"(Total: {len(all_cloud_data)} registros)")
    print("-------------------------------------------\n")

def display_blockchain_data(blockchain):
    """Muestra la blockchain."""
    blockchain.display_chain()


def alter_cloud_data(cloud_filename):
    """Permite al usuario modificar un registro en el archivo JSON."""
    print("\n--- Alterar Datos en la Nube ---")
    cloud_data = load_from_cloud(cloud_filename)

    if not cloud_data:
        print(f"No hay datos en '{cloud_filename}' para alterar.")
        return

    print(f"Hay {len(cloud_data)} registros en total (índices 0 a {len(cloud_data)-1}).")

    while True:
        try:
            idx_str = input(f"Ingrese el índice del registro a modificar (0-{len(cloud_data)-1}): ")
            idx = int(idx_str)
            if 0 <= idx < len(cloud_data):
                break
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    record_to_alter = cloud_data[idx]
    print("\nRegistro seleccionado:")
    print(json.dumps(record_to_alter, indent=2))

    # Campos modificables
    available_fields = [k for k in record_to_alter.keys() if k not in ['timestamp', 'device_id']]
    if not available_fields:
        print("No hay campos modificables en este registro (ej: solo timestamp/ID).")
        return

    while True:
        field_to_alter = input(f"Ingrese el campo a modificar ({', '.join(available_fields)}): ").lower()
        if field_to_alter in available_fields:
            break
        else:
             print(f"Campo no válido. Elija entre: {', '.join(available_fields)}")

    original_value = record_to_alter[field_to_alter]
    new_value_str = input(f"Ingrese el nuevo valor para '{field_to_alter}' (valor actual: {original_value}): ")

    # Intentar convertir al tipo original si es numérico
    try:
        if isinstance(original_value, (int, float)):
            new_value = type(original_value)(new_value_str) # Convierte a int o float
        else:
            new_value = new_value_str # Mantener como string si no era numérico
    except ValueError:
         print(f"Advertencia: No se pudo convertir '{new_value_str}' al tipo original ({type(original_value).__name__}). Se guardará como string.")
         new_value = new_value_str

    # Modificar y guardar
    print(f"\nModificando registro {idx}, campo '{field_to_alter}' de '{original_value}' a '{new_value}'...")
    cloud_data[idx][field_to_alter] = new_value

    try:
        with open(cloud_filename, 'w') as f:
            json.dump(cloud_data, f, indent=4)
        print(f"¡Datos alterados guardados exitosamente en '{cloud_filename}'!")
    except Exception as e:
        print(f"Error al guardar los datos alterados: {e}")
        cloud_data[idx][field_to_alter] = original_value # Revertir cambio en memoria

    print("------------------------------\n")


# --- Ejecución Principal ---
if __name__ == "__main__":

    # Inicializar blockchain en memoria
    my_blockchain = Blockchain()
    print("Blockchain inicializada con bloque Génesis.")

    # Asegurar que el archivo de la nube existe y es válido
    initialize_cloud_file(CLOUD_DATA_FILE)

    # Bucle del menú principal
    while True:
        display_menu()
        choice = input("Seleccione una opción: ")

        # Limpiar pantalla (opcional, mejora la legibilidad)
        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == '1':
            add_new_batch(my_blockchain, CLOUD_DATA_FILE, BATCH_SIZE, DEVICE_IDS)
        elif choice == '2':
            display_cloud_data(CLOUD_DATA_FILE)
        elif choice == '3':
            display_blockchain_data(my_blockchain)
        elif choice == '4':
            alter_cloud_data(CLOUD_DATA_FILE)
        elif choice == '5':
            verify_data_integrity(my_blockchain, CLOUD_DATA_FILE, BATCH_SIZE)
        elif choice == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        # Pausa antes de volver a mostrar el menú
        input("\nPresione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')