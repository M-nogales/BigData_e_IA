'''
Escribir una función que reciba un dataframe de Pandas con los ingresos y gastos
de una empresa por meses y devuelva un diagrama de líneas con dos líneas, la
primera para los ingresos, y la segunda para los gastos. El diagrama debe tener una
leyenda identificando la línea de los ingresos y la de los gastos, un título con el
nombre “Evolución de Ingresos y Gastos” y el eje Y debe empezar en 0.
'''

import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.DataFrame({
    'Ingresos':[1000,2000,3000,4000,5000],
    'Gastos':[500,1000,1500,2000,2500],
}, index=['Enero','Febrero','Marzo','Abril','Mayo'])

def two_lane_graf_creator(dataframe: pd.DataFrame):
    plt.plot(dataframe)
    plt.legend(dataframe.columns)
    plt.title('Evolución de Ingresos y Gastos')
    plt.ylim(0)
    plt.show()

two_lane_graf_creator(dataframe)