'''
Escribir una función que reciba una serie de Pandas con el número de ventas de un
producto durante los meses de un trimestre y un título, y cree un diagrama de
sectores con las ventas en formato PNG con el título dado. El diagrama debe
guardarse en un fichero con el formato PNG y el título dado.
'''
import matplotlib.pyplot as plt
import pandas as pd

sales=pd.Series([100,200,300], index=['Enero','Febrero','Marzo'])

def diagram_creator (sales: pd.Series, title: str):
    plt.pie(sales, labels=sales.index, autopct='%1.1f%%')
    plt.title(title)
    
    plt.savefig(title+'.png')
    plt.show()
    print ("img saved as "+title+'.png, in where ever you are running this script')
diagram_creator(sales,'Ventas del Trimestre')