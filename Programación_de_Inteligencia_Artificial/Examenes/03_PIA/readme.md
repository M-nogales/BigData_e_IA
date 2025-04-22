# Simulación de un ecosistema convergente: IoT + Cloud + Blockchain

Diseñar e implementar un prototipo que simule un entorno donde se recolectan datos a través de dispositivos simulados (IoT), se procesan y almacenan en la nube, y se registran hashes en una cadena simulada tipo blockchain.

## Requisitos del Proyecto

- **Simulación de dispositivos IoT**:  
  Crear un script (Python o similar) que simule dispositivos IoT generando datos cada cierto intervalo (por ejemplo, temperatura, humedad, etc.).

- **Procesamiento de los datos**:
  1. Los datos deben enviarse a un servicio en la nube simulado (puede ser un archivo JSON o una base de datos ligera tipo SQLite).
  2. Cada lote de datos debe ser hasheado usando SHA-256 y registrado en una estructura de cadena tipo blockchain (simulada localmente).

## Visualización de resultados

- Historial de datos generados.
- Hashes almacenados.
- Verificación de integridad:
  - Alterar un dato y mostrar cómo se rompe la cadena de bloques.

## Entrega

**Nombre del archivo:**  
`EXUD03_NombreApellidos.ZIP`