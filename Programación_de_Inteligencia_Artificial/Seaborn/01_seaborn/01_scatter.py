''' 1. Gráfico de dispersión avanzado con estilo personalizado
- Dataset: `mpg` de Seaborn.
- Pasos:
  - Convertir las columnas `horsepower`, `weight` y `mpg` a arrays de NumPy.
  - Crear un gráfico de dispersión donde:
    - El tamaño de los puntos represente el peso.
    - El color represente la eficiencia de combustible.
  - Personalizar con temas y ajustes de tamaño.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
mpg_data= sns.load_dataset('mpg')

horsepower = np.array(mpg_data['horsepower'])
weight = np.array(mpg_data['weight'])
np_mpg_data = np.array(mpg_data['mpg'])

sns.scatterplot(x=horsepower,
                y=np_mpg_data,
                size=weight,
                hue=np_mpg_data,
                sizes=(20, 200),
                palette='viridis')

# same without numpy
# sns.scatterplot(x='horsepower',
#                 y='mpg',
#                 data=mpg_data,
#                 size='weight',
#                 hue='weight',
#                 sizes=(20, 200),
#                 palette='viridis')
plt.show()
