''' 10. Catplot para variables categóricas con ajuste de orden
- **Dataset**: `exercise`.
- **Pasos**:
  - Convertir las columnas `duración` y `tipo de ejercicio` a arrays.
  - Crear un catplot de tipo stripplot para observar:
    - La dispersión de duración en diferentes tipos de ejercicio.
  - Ajustar el orden de categorías y el ancho de puntos.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
exercise_data= sns.load_dataset('exercise')

duration = np.array(exercise_data['time'])
exercise_type = np.array(exercise_data['kind'])

catplot = sns.catplot(x=exercise_type,
                      y=duration,
                      kind='strip',
                      order=['rest', 'walking', 'running'],
                      dodge=True,
                      linewidth=2,
                      palette='viridis')
plt.show()
