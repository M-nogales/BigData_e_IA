'''6. Gráfico de barras con agregación de datos
- **Dataset**: `titanic`.
- **Pasos**:
  - Convertir las columnas `class` y `fare` a arrays.
  - Crear un gráfico de barras que muestre:
    - El promedio de tarifas pagadas por clase.
    - Las desviaciones estándar indicadas.
  - Aplicar una paleta de color diferenciada por género.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

titanic_data= sns.load_dataset('titanic')

class_data = np.array(titanic_data['class'])
fare_data = np.array(titanic_data['fare'])

sns.barplot(x=class_data,
            y=fare_data,
            ci='sd',
            data = titanic_data,
            palette='viridis')

plt.show()