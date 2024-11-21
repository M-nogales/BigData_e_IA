# 07. **Análisis de Precio de un Producto en Tiendas**
''' Pide al usuario que ingrese los precios de un producto en 5 tiendas diferentes.
Crea una Serie y nombra cada tienda como índice.
Muestra el precio más bajo y más alto.
Identifica las tiendas con precios por encima de la mediana.
Rellena los precios faltantes (NaN) con el precio promedio y grafica los precios.
 '''

import pandas as pd

while True:
    try:
        prices = [float(input(f'Dime el precio del producto en la tienda {i+1}: ')) for i in range(5)]
        break
    except ValueError:
        print('Solo se permiten números')

stores = ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4', 'Tienda 5']
prices = pd.Series(prices, index=stores, dtype='object')

print('Precio más bajo: ', prices.min())
print('Precio más alto: ', prices.max())
print('Tiendas con precios por encima de la mediana:\n', prices[prices > prices.median()])
# fillna() rellena los valores NaN con el valor que le pasemos, inplace=True modifica el objeto original
prices.fillna(prices.mean(), inplace=True)
print('Precios:\n', prices)