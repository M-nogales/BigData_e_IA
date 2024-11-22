# 09. **Registro de Visitas a una Página Web**
''' Pide al usuario que ingrese el número de visitas diarias a una página web durante 10 días.
Crea una Serie con los datos.
Calcula el total y el promedio de visitas diarias.
Muestra los días con más visitas que el promedio y reemplaza los valores de visitas < 50 con "Baja visita".
#todo Grafica el número de visitas diarias.
 '''

import pandas as pd
import matplotlib.pyplot as plt

while True:
    try:
        visits = [int(input(f'Dame el número de visitas del día {i+1}: ')) for i in range(10)]
        break
    except ValueError:
        print('Solo se permiten números enteros')

days = ['Día 1', 'Día 2', 'Día 3', 'Día 4', 'Día 5', 'Día 6', 'Día 7', 'Día 8', 'Día 9', 'Día 10']

visits = pd.Series(visits, index=days, dtype='int')
#copia de visits para no mezclar tipos de datos y la gráfica no de problemas
visits2 = visits.copy()
print('Total de visitas: ', visits.sum())
print('Promedio de visitas: ', visits.mean())
print('Días con más visitas que el promedio: ', visits[visits > visits.mean()])
visits[visits < 50] = 'Baja visita'
print('Visitas clasificadas:\n', visits)
# grafica
visits2.plot(kind='bar')
plt.title('Visitas Diarias')
plt.ylabel('Visitas')
plt.xlabel('Días')
plt.show()