# 05. **Convertir Fecha a Otro Formato**
# Crea una función que reciba una fecha en formato YYYY-MM-DD 
# y la convierta en el formato DD/MM/YYYY.

from datetime import datetime

def change_format(cadena_fecha):
    fecha = datetime.strptime(cadena_fecha, "%Y-%m-%d")
    return fecha.strftime("%d/%m/%Y")  # Formato DD/MM/YYYY

print('change_format("2025-01-01"): ',
       change_format("2025-01-01"))  # 01/01/2025

