'''7. FacetGrid con múltiples gráficos de distribución
- **Dataset**: `fmri`.
- **Pasos**:
  - Convertir las columnas de `tiempo` y `respuesta` a arrays de NumPy.
  - Crear una cuadrícula de gráficos de KDE por sujeto para comparar patrones de respuesta.
  - Personalizar la disposición de las subparcelas.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
fmri_data= sns.load_dataset('fmri')
fmri_data = fmri_data.dropna()

time_data = np.array(fmri_data['timepoint'])
response_data = np.array(fmri_data['signal'])

g = sns.FacetGrid(fmri_data, col='subject', col_wrap=4, height=3, sharex=True, sharey=True)
g.map(sns.kdeplot, 'timepoint', fill=True, color='blue')

plt.show()
