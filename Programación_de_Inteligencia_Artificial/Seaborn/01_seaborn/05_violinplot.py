'''5. Violin plot con categorización de datos
- **Dataset**: `iris`.
- **Pasos**:
  - Convertir la columna de longitud del sépalo y la especie a arrays de NumPy.
  - Generar un violin plot para analizar la distribución de la longitud del sépalo por especie.
  - Ajustar la división interna y mostrar puntos individuales.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
iris_data= sns.load_dataset('iris')

sepal_length = np.array(iris_data['sepal_length'])
species = np.array(iris_data['species'])

sns.violinplot(x=species,
               y=sepal_length,
               data=iris_data,
               inner='quartile',
               dodge=True)

# not sure if the exercise is asking for this or just inner = "point" on violinplot
sns.stripplot(x='species', y='sepal_length', data=iris_data, 
              color='black', alpha=0.6, jitter=True, size=4)

plt.show()
