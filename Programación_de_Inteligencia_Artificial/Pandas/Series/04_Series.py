# 04. **Registro de Horas de Trabajo**
''' Solicita al usuario que ingrese las horas trabajadas por un empleado durante 5 días laborales.
Crea una Serie con los datos.
Calcula el total de horas trabajadas, y muestra los días en los que el empleado trabajó más de 8 horas.
Reemplaza las horas menores a 6 con "Medio tiempo".
Muestra una lista de días y su clasificación de horas (Normal, Medio tiempo, Extra).
 '''

import pandas as pd

while True:
    try:
        hours = []
        for i in range(5):
            hour = float(input(f'Introduce las horas trabajadas el día {i+1}: '))
            hours.append(hour)
        break
    except ValueError:
        print('Dime un número válido')

days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

hours = pd.Series(hours, index=days, dtype='float')
# print('Total de horas trabajadas: ', hours.sum())
# print('Días en los que se trabajó más de 8 horas: ', hours[hours > 8])

'''
#? si hacemos esto mezclamos strings con floats y no podemos hacer comparaciones
hours_classified[hours_classified < 6] = 'Medio tiempo'
print('Clasificación de horas trabajadas:\n', hours_classified)
hours_classified[(hours_classified >= 6) & (hours_classified <= 8)] = 'Normal'
hours_classified[hours_classified > 8] = 'Extra'
'''

hours = pd.cut(hours, bins=[0, 6, 8, float('inf')], labels=['Medio tiempo', 'Normal', 'Extra'])

print('Clasificación de horas trabajadas:\n', hours)