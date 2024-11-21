# 08. **Análisis de Datos Meteorológicos**
''' Solicita al usuario las precipitaciones registradas durante los últimos 7 días.
Crea una Serie con los datos.
Identifica los días sin lluvia (0 mm) y reemplázalos con "Sin precipitación".
Calcula el total y el promedio de precipitaciones.
Muestra los días con precipitación por encima del promedio.
 '''

import pandas as pd

while True:
    try:
        precipitations = [int(input(f'Dime la precipitación del día {i+1}: ')) for i in range(7)]
        break
    except ValueError:
        print('Solo se permiten números enteros')

days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

precipitations = pd.Series(precipitations, index=days, dtype='object')

print('Total de precipitaciones: ', precipitations.sum())
print('Promedio de precipitaciones: ', precipitations.mean())
precipitations[precipitations.astype(float) == 0] = 'Sin precipitación'
print('precipitations: ', precipitations[precipitations.astype(float) > precipitations.mean()])