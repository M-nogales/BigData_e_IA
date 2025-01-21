''' 8. Pairplot para el análisis multivariado
- **Dataset**: `iris`.
- **Pasos**:
  - Convertir todas las columnas numéricas a arrays.
  - Generar un pairplot con:
    - Diferentes tipos de gráficos en la diagonal y fuera de la diagonal.
    - Estilos personalizados y regresión lineal para las relaciones.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
iris_data= sns.load_dataset('iris')

sepal_length = np.array(iris_data['sepal_length'])
sepal_width = np.array(iris_data['sepal_width'])
petal_length = np.array(iris_data['petal_length'])
petal_width = np.array(iris_data['petal_width'])

print(iris_data.head())

pairplot = sns.pairplot(iris_data,
                        diag_kind='kde',
                        kind='reg',
                        hue='species',
                        palette='husl')

plt.show()
