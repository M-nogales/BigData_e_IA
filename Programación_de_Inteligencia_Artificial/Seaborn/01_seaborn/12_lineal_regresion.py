'''12. Regresión lineal múltiple con visualización avanzada
- **Dataset**: `mpg`.
- **Pasos**:
  - Convertir las columnas de potencia (`horsepower`) y peso (`weight`) a arrays.
  - Generar un gráfico de regresión múltiple mostrando:
    - La relación entre peso y potencia.
    - Diferentes niveles de confianza.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
mpg_data= sns.load_dataset('mpg')

horsepower = np.array(mpg_data['horsepower'])
weight = np.array(mpg_data['weight'])

sns.lmplot(x='weight', y='horsepower', data=mpg_data, ci=95)

plt.show()