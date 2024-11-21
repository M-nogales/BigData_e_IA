# 01. **Análisis de Ventas de una Semana**
''' Solicita al usuario que ingrese las ventas diarias de una semana (7 días).
Crea una Serie con los datos proporcionados.
Realiza el análisis: muestra el total de ventas, el promedio, y el día con las mayores ventas.
Visualiza los días que tienen ventas por encima del promedio.
 '''
import pandas as pd

while True:
    try:
        sells = [int(input('Dime las ventas del día 1: '))]
        for i in range(2, 8):
            sells.append(int(input(f'Ingrese las ventas del día {i}: ')))
        break
    except ValueError:
        print('Por favor, Dame un número entero.')

days = ['Día 1', 'Día 2', 'Día 3', 'Día 4', 'Día 5', 'Día 6', 'Día 7']

sells_series = pd.Series(sells, index=days)
print('Ventas semanales: ', sells_series)
print('Total de ventas: ', sells_series.sum())
print('Promedio de ventas: ', sells_series.mean())
#index de los dias con mayor venta
print('Día con mayores ventas: ', sells_series.idxmax())
print('Días con ventas por encima del promedio:\n', sells_series[sells_series > sells_series.mean()])
