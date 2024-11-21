# 01. **Obtener la Fecha Actual**
# Crea una función que obtenga la fecha y hora actuales,
#  formateada en el formato DD/MM/YYYY HH:MM:SS.

from datetime import datetime


def actual_date():
    ahora = datetime.now()
    return ahora.strftime("%d/%m/%Y %H:%M:%S")

print(actual_date())