import hashlib
import os

def calcular_hash(archivo, algoritmo):
    hash_func = hashlib.new(algoritmo)
    with open(archivo, 'rb') as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def cargar_hashes():
    """Carga los hashes desde el archivo hashes.txt si existe."""
    hashes_guardados = {}
    if os.path.exists("hashes.txt"):
        with open("hashes.txt", "r") as f:
            for line in f:
                partes = line.strip().split()
                if len(partes) == 2:
                    archivo, hash_valor = partes
                    hashes_guardados[archivo] = hash_valor
    return hashes_guardados

def guardar_hashes():
    """Genera y guarda los hashes solo si no están en el archivo."""
    archivos = {
        "data/archivo.txt": "sha256",
        "data/imagen.png": "md5",
        "data/documento.pdf": "sha1",
        "data/comprimido.zip": "sha512"
    }
    
    hashes_guardados = cargar_hashes()
    
    with open("hashes.txt", "w") as f:
        for archivo, algoritmo in archivos.items():
            if os.path.exists(archivo):
                if archivo not in hashes_guardados:
                    hash_valor = calcular_hash(archivo, algoritmo)
                    hashes_guardados[archivo] = hash_valor
                    print(f"Hash generado para {archivo} ({algoritmo}): {hash_valor}")
                else:
                    print(f"Hash ya existente para {archivo}, no se regenera.")
                
                f.write(f"{archivo} {hashes_guardados[archivo]}\n")
            else:
                print(f"El archivo {archivo} no existe.")

def verificar_integridad():
    """Verifica la integridad comparando los hashes actuales con los almacenados."""
    archivos = {
        "data/archivo.txt": "sha256",
        "data/imagen.png": "md5",
        "data/documento.pdf": "sha1",
        "data/comprimido.zip": "sha512"
    }
    
    hashes_guardados = cargar_hashes()
    
    if not hashes_guardados:
        print("No hay hashes almacenados. Ejecuta primero la generación de hashes.")
        return
    
    for archivo, algoritmo in archivos.items():
        if archivo not in hashes_guardados:
            print(f"No hay un hash registrado para {archivo}.")
            continue
        
        hash_actual = calcular_hash(archivo, algoritmo)
        hash_guardado = hashes_guardados[archivo]
        
        if hash_actual == hash_guardado:
            print(f"El archivo {archivo} no ha sido modificado.")
        else:
            print(f"¡ALERTA! El archivo {archivo} ha sido modificado.")

# Generar hashes si no existen
guardar_hashes()

# Verificar integridad de los archivos
verificar_integridad()