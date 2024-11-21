# 03. **Análisis de Temperaturas Semanales**
''' Solicita al usuario las temperaturas registradas en una semana (7 días).
Crea una Serie con los datos y calcula la temperatura máxima y mínima.
Identifica los días que tienen temperaturas por encima de 25°C.
Rellena posibles valores faltantes (NaN) con la temperatura promedio.
#todo Grafica las temperaturas de la semana.
 '''

import pandas as pd
while True:
    try:
        temps = []
        for i in range(7):
            temp = float(input(f'Dime la temperatura del día {i+1}: '))
            temps.append(temp)
        break
    except ValueError:
        print('Dime un número válido')

temps = pd.Series(temps)
print('Temperatura máxima: ', temps.max())
print('Temperatura mínima: ', temps.min())
print('Días con temperaturas por encima de 25°C: ', temps[temps > 25])
print('Temperaturas con valores faltantes rellenados con la media: ', temps.fillna(temps.mean()))
