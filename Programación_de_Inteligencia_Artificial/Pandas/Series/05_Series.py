# 05. **Inventario de Productos**
''' Pide al usuario que ingrese la cantidad de 8 productos diferentes en stock.
Crea una Serie y asigna nombres de productos como índice.
Muestra los productos con menos de 10 unidades.
Rellena cualquier valor faltante (NaN) con 0.
Muestra los productos ordenados por la cantidad en stock.
 '''

import pandas as pd

products = ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5', 'Product 6', 'Product 7', 'Product 8']

while True:
    try:
        stock = [int(input(f'Introduce la cantidad de unidades en stock para el producto {product}: ')) for product in products]
        break
    except ValueError:
        print('Dime un número válido')

stock = pd.Series(stock, index=products, dtype='int')

print('Productos con menos de 10 unidades en stock:\n', stock[stock < 10])
# fillna() rellena los valores NaN con el valor que le pasemos, inplace=True modifica el objeto original
print('Productos con valores faltantes rellenados con 0:\n', stock.fillna(0, inplace=True))
print('Productos ordenados por cantidad en stock:\n', stock.sort_values())
