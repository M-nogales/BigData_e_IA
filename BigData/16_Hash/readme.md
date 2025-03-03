# Ejercicio: Verificación de Integridad de Archivos con Hashes

## Descripción
En esta práctica, implementarás un sistema de sumas de verificación utilizando distintos métodos de cifrado de la librería `hashlib` en Python.
El objetivo es calcular, guardar y verificar hashes de archivos para comprobar su integridad.

---

## Requisitos
Debes crear un script en Python que realice las siguientes tareas:

1. **Cálculo de hashes:**
 - Calcular el hash **SHA-256** de un archivo de texto (`archivo.txt`).
 - Calcular el hash **MD5** de una imagen (`imagen.png`).
 - Calcular el hash **SHA-1** de un archivo PDF (`documento.pdf`).
 - Calcular el hash **SHA-512** de un archivo ZIP (`comprimido.zip`).

2. **Almacenamiento de hashes:**
 - Guardar los hashes calculados en un archivo de texto llamado `hashes.txt`.
 - Cada línea del archivo debe contener el nombre del archivo seguido de su respectivo hash.

3. **Verificación de integridad:**
 - Implementar una función que compare el hash actual de un archivo con su hash previamente almacenado en `hashes.txt`.
 - Mostrar un mensaje indicando si el archivo ha sido modificado o no.

---

## Instrucciones
1. Selecciona cada archivo en tu PC.
2. Ingresa un algoritmo de hash (`md5`, `sha1`, `sha256`, `sha512`).
3. Genera y almacena el hash del archivo en un archivo de texto.
4. Verifica la integridad del archivo comparándolo con su hash almacenado.
5. Modifica el archivo original y vuelve a ejecutar la verificación para observar los resultados.
6. Documenta tu proceso con capturas de pantalla y explica los resultados obtenidos.

---

# **Verificación de Integridad de Archivos con Hashes**
## **Proceso**
### **1. Generación de Hashes**
- Se ejecuta el script para calcular y almacenar los hashes iniciales en `hashes.txt`.
- Si el archivo ya existe y contiene hashes, no se sobrescriben.
- Si algún archivo no tiene un hash registrado, se genera y se añade al archivo.

### **2. Verificación de Integridad**
- Se recalculan los hashes de los archivos actuales.
- Se comparan con los hashes almacenados en `hashes.txt`.
- Si coinciden, el archivo no ha sido modificado.
- Si no coinciden, se genera una alerta indicando una posible modificación.

## **Resultados Obtenidos**
### **1. Estado Inicial**
Salida esperada tras la primera ejecución:
```bash
Hash generado para data/archivo.txt (sha256): abc123...
Hash generado para data/imagen.png (md5): def456...
Hash generado para data/documento.pdf (sha1): ghi789...
Hash generado para data/comprimido.zip (sha512): jkl012...
```

### **2. Verificación sin Modificaciones**
Salida esperada si los archivos no han cambiado:
```bash
El archivo data/archivo.txt no ha sido modificado.
El archivo data/imagen.png no ha sido modificado.
El archivo data/documento.pdf no ha sido modificado.
El archivo data/comprimido.zip no ha sido modificado.
```

### **3. Verificación tras Modificar un Archivo**
Si editamos `data/archivo.txt` y volvemos a ejecutar el script:
```bash
¡ALERTA! El archivo data/archivo.txt ha sido modificado.
El archivo data/imagen.png no ha sido modificado.
El archivo data/documento.pdf no ha sido modificado.
El archivo data/comprimido.zip no ha sido modificado.
```
## **Capturas de imagen**
![Archivo modificado](imgs/primera_ejecucion.png)
![Archivo modificado](imgs/segunda_ejecucion.png)
![Archivo modificado](imgs/revertir_cambios_y_modificar_pdf.png)
