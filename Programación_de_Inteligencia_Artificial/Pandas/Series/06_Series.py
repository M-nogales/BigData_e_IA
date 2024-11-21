# 06. **Evaluación de Encuesta de Satisfacción**
''' Solicita al usuario que ingrese las calificaciones de satisfacción (de 1 a 5) de 12 clientes.
Crea una Serie con las calificaciones.
Calcula la frecuencia de cada calificación y el porcentaje de clientes satisfechos (calificación ≥ 4).
Reemplaza cualquier calificación de 1 con "Insatisfecho".
#todo Muestra un resumen de las calificaciones en forma de gráfico de barras.
 '''

import pandas as pd

while True:
    try:
        satisfaction = [int(input(f'Dime la calificación de satisfacción del cliente {i+1}: ')) for i in range(12)]
        break
    except ValueError:
        print('Solo se permiten números enteros')

satisfaction = pd.Series(satisfaction, dtype='object')

print('Frecuencia de cada calificación:\n', satisfaction.value_counts(),
      'Porcentaje de clientes satisfechos: ', satisfaction[satisfaction >= 4].count() / satisfaction.count() * 100)
satisfaction[satisfaction == 1] = 'Insatisfecho'