# 12. **Conversión de segundos a horas, minutos y segundos**
# Generar una función que tome un número total de segundos y lo convierta a horas, minutos y segundos.

def to_hours_mins_segs(seconds):
    hours = seconds // 3600
    mins = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, mins, seconds

hours, mins, seconds = to_hours_mins_segs(5445)
print(hours, "horas,", mins, "minutos,", seconds, "segundos")