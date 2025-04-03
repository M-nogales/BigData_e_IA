import random
import time
import csv
from datetime import datetime

# Sensor de Temperatura
class SensorTemperatura:
    def __init__(self):
        self.tipo = "Temperatura"
    
    def leer_dato(self):
        # Genera un valor aleatorio de temperatura entre 18°C y 30°C
        return round(random.uniform(18, 30), 2)

# Sensor de Luz
class SensorLuz:
    def __init__(self):
        self.tipo = "Luz"
    
    def leer_dato(self):
        # Genera un valor aleatorio de luminosidad entre 0 (sin luz) y 1000 lux
        return round(random.uniform(0, 1000), 2)

# Sensor de Humedad
class SensorHumedad:
    def __init__(self):
        self.tipo = "Humedad"
    
    def leer_dato(self):
        # Genera un valor aleatorio de humedad entre 30% y 70%
        return round(random.uniform(30, 70), 2)

# Sensor de CO2
class SensorCO2:
    def __init__(self):
        self.tipo = "CO2"
    
    def leer_dato(self):
        # Genera un valor aleatorio de CO2 entre 300 y 1000 ppm
        return round(random.uniform(300, 1000), 2)

# Simulación de un periodo de tiempo con 15 registros por sensor
def simular_entorno(periodo, intervalos):
    sensores = {
        "Temperatura": SensorTemperatura(),
        "Luz": SensorLuz(),
        "Humedad": SensorHumedad(),
        "CO2": SensorCO2()
    }
    
    registros = {"Temperatura": [], "Luz": [], "Humedad": [], "CO2": []}
    
    for _ in range(periodo):
        for tipo, sensor in sensores.items():
            dato = sensor.leer_dato()
            registros[tipo].append(dato)
        
        time.sleep(intervalos)
    
    return registros

# Aplicar reglas de IA basadas en los valores de los sensores
def aplicar_reglas(sensor_temperatura, sensor_humedad, sensor_co2):
    decisiones = []

    # Regla de temperatura
    if sensor_temperatura > 25:
        decisiones.append("Encender aire acondicionado")
    elif sensor_temperatura < 20:
        decisiones.append("Encender calefacción")
    
    # Regla de humedad
    if sensor_humedad > 60:
        decisiones.append("Abrir ventana")

    # Regla de CO2
    if sensor_co2 > 800:
        decisiones.append("Activar ventilación")
    
    return decisiones

# Guardar registros en un archivo CSV (si existe se añaden los nuevos)
def guardar_en_csv(registros, decisiones, archivo_csv):
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Comprobar si el archivo existe y crear el encabezado si es necesario
    archivo_existe = False
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as f:
            archivo_existe = True
    except FileNotFoundError:
        pass

    # Abrir archivo CSV en modo de anexado
    with open(archivo_csv, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Si el archivo no existe, agregar encabezado
        if not archivo_existe:
            writer.writerow(['Fecha', 'Temperatura (°C)', 'Luz (lux)', 'Humedad (%)', 'CO2 (ppm)', 'Decisiones'])

        # Guardar cada registro con su fecha y decisiones
        for i in range(len(registros['Temperatura'])):
            temperatura = registros['Temperatura'][i]
            luz = registros['Luz'][i]
            humedad = registros['Humedad'][i]
            co2 = registros['CO2'][i]
            decisiones_str = ', '.join(decisiones[i]) if decisiones[i] else 'Ninguna'

            # Escribir una fila por cada registro
            writer.writerow([fecha_actual, temperatura, luz, humedad, co2, decisiones_str])


periodo = 15  # 15 registros
intervalos = 1  # 1 segundo entre lecturas

# Simulando los datos de los sensores
registros = simular_entorno(periodo, intervalos)

# Generar las decisiones basadas en los valores de los sensores
decisiones = []
for i in range(periodo):
    temperatura = registros['Temperatura'][i]
    humedad = registros['Humedad'][i]
    co2 = registros['CO2'][i]
    
    decisiones.append(aplicar_reglas(temperatura, humedad, co2))

# Guardar los registros y las decisiones en un archivo CSV
archivo_csv = 'registros_sensores.csv'
guardar_en_csv(registros, decisiones, archivo_csv)

print("Simulación completada y registros guardados en 'registros_sensores.csv'")
