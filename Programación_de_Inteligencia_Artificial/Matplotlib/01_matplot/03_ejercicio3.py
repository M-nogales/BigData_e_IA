'''
Escribir una función que reciba un diccionario con las notas de las asignaturas de
un curso y una cadena con el nombre de un color y devuelva un diagrama de barras
de las notas en el color dado.
'''
import matplotlib.pyplot as plt

def diagram_creator (results: dict,clr:str):
    grades=results.keys()
    notes = results.values()
    plt.bar(grades,notes,color=clr)
    plt.title('Notas de las asignaturas')
    plt.show()

results = {
    'math': 8,
    'english': 7,
    'science': 9,
    'history': 6,
    'art': 8
}

diagram_creator(results,'green')