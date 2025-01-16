'''
Escribir una función que reciba una serie de Pandas con las notas de los alumnos
de un curso y devuelva un diagrama de cajas con las notas. El diagrama debe tener
el título “Distribución de Notas”
'''

import matplotlib.pyplot as plt
import pandas as pd

notes=pd.Series([8,7,9,6,8,5])

def diagram_creator (notes: pd.Series):
    plt.boxplot(notes)
    plt.title('Distribución de Notas')
    plt.show()

diagram_creator(notes)