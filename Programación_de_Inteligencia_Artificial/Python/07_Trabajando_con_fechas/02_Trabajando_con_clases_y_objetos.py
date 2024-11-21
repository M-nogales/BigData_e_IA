# 02. **Convertir Cadena a Fecha**
# Escribe una función que reciba una cadena en formato DD/MM/YYYY
#  y la convierta en un objeto datetime usando strptime().

from datetime import datetime


def str_to_date(cadena_fecha):
    fecha = datetime.strptime(cadena_fecha, "%d/%m/%Y")
    print(f"Fecha convertida: {fecha}")
    return fecha

print('str_to_date("01/01/2025"): ', str_to_date("01/01/2025")) # 2021-01-01 00:00:00