# 03. **Calcular Diferencia en Días**
# Crea una función que reciba dos cadenas de fecha en formato DD/MM/YYYY
#  y calcule cuántos días hay entre ambas.

from datetime import datetime


def days_diff(fecha1_str, fecha2_str):
    fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
    fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
    diferencia = (fecha2 - fecha1).days
    return abs(diferencia)  # Devolver la diferencia absoluta

print('days_diff("01/01/2024", "01/01/2025"): ',
       days_diff("01/01/2024", "01/01/2025"))