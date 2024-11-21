# 04. **Sumar Días a una Fecha**
# Escribe una función que reciba una fecha en formato DD/MM/YYYY 
# y un número de días, devolviendo la nueva fecha después de sumar esos días.

from datetime import datetime, timedelta

def add_days(cadena_fecha, dias):
    fecha = datetime.strptime(cadena_fecha, "%d/%m/%Y")
    nueva_fecha = fecha + timedelta(days=dias)
    return nueva_fecha.strftime("%d/%m/%Y")

print('add_days("01/01/2025", 10): ', add_days("01/01/2025", 10)) # 11/01/2025