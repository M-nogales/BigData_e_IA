'''
El fichero “bancos.csv” contiene las cotizaciones de los principales bancos de
España con los siguientes datos:
- Empresa: Nombre de la empresa
- Apertura: Precio de la acción a la apertura de la Bolsa
- Máximo: Precio máximo de la acción durante la jornada.
- Mínimo: Precio mínimo de la acción durante la jornada.
- Cierre: Precio de la acción al cierre de la Bolsa
- Volumen: Volumen de negocios al cierre de la Bolsa
Construir una función que reciba el fichero “bancos.csv” y cree un diagrama de
líneas con las series temporales de las cotizaciones de cierre de cada banco.
'''
import matplotlib.pyplot as plt
import pandas as pd

def diagram_creator (file: str):
    df = pd.read_csv(file)
    pivot_data = df.pivot_table(index='Empresa', values='Cierre')
    print(pivot_data)
    # para añadir todas las empresas en el mismo gráfico tenemos que usar un bucle for
    for company in pivot_data.columns:
        plt.plot(pivot_data.index, pivot_data[company], label=company)

    plt.xlabel("Time")
    plt.ylabel("Closing Price (Cierre)")
    plt.title("Closing Prices of Banks Over Time")
    plt.legend(title="Banks")
    plt.grid()
    plt.tight_layout()

    plt.show()

diagram_creator('bancos.csv')
