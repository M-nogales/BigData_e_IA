'''3. Distribución de datos con KDE Plot y rug plot
- **Dataset**: `tips` de Seaborn.
- **Pasos**:
  - Convertir las columnas `total_bill` y `tip` a arrays.
  - Generar un gráfico de densidad kernel (KDE) superpuesto con un gráfico de rug.
  - Ajustar el ancho de banda y experimentar con estilos de visualización.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')

total_bill = np.array(tips['total_bill'])
tip = np.array(tips['tip'])

sns.kdeplot(total_bill, fill=True, color='blue', label ='KDE: Total Bill',bw_adjust=0.5)
sns.rugplot(total_bill, label ='Rug: Total Bill', color='black')

plt.show()
