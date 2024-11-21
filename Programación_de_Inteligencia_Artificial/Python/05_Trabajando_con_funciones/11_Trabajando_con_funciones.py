# 11. **Conversión de tiempo a segundos**
# Generar una función que tome un número total de horas, minutos y segundos, y devuelva el tiempo total en segundos.

def to_seconds(hour, minutes, seconds):
    result = hour * 3600 + minutes * 60 + seconds
    return result

print('to_seconds(hour=1, minutes=30, seconds=45): ', to_seconds(hour=1, minutes=30, seconds=45))