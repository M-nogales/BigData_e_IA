'''
Escribir una función que reciba una serie de Pandas con el número de ventas de un
producto por años y una cadena con el tipo de gráfico a generar (líneas, barras,
sectores, áreas) y devuelva un diagrama del tipo indicado con la evolución de las
ventas por años y con el título “Evolución del Número de Ventas”
'''
import matplotlib.pyplot as plt
import pandas as pd

sales=pd.Series([100,200,300], index=[2018,2019,2020])

def graf_creator(sales: pd.Series, chart_type: str):
    if chart_type == 'lineas':
        plt.plot(sales)
    elif chart_type == 'barras':
        plt.barh(sales.index, sales)
    elif chart_type == 'sectores':
        plt.pie(sales, labels=sales.index, autopct='%1.1f%%')
    elif chart_type == 'areas':
        plt.fill_between(sales.index, sales)
    plt.title('Evolución del Número de Ventas')
    plt.show()

graf_creator(sales,'lineas')
graf_creator(sales,'barras')
graf_creator(sales,'sectores')
graf_creator(sales,'areas')