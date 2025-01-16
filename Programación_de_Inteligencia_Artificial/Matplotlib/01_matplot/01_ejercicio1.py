'''
Utilizar la función de la raíz cuadrada (librería Math), generar un gráfico (Matplotlib)
de dispersión (Random) en el que se muestre 20 números enteros aleatorios entre
el 0 y 100 en el eje X y su raíz cuadrada en el eje Y.
'''

import math
import matplotlib.pyplot as plt
import random

x = random.sample(range(0, 100), 20)

y = [math.sqrt(i) for i in x]


plt.scatter(x, y)
plt.show()
