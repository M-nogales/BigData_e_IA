'''4. Boxplot multivariado con ajuste de estilo
- **Dataset**: `diamonds`.
- **Pasos**:
  - Convertir las columnas `carat`, `price` y `depth` a arrays de NumPy.
  - Crear un gráfico de caja para analizar:
    - La distribución de precios en diferentes rangos de quilates.
    - Segmentar por el tipo de corte.
  - Personalizar estilos de borde y paletas.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
diamons_data = sns.load_dataset('diamonds')
# sample added in order get a better visualization
diamons_data = diamons_data.sample(1000)
diamons_data = diamons_data.dropna()

carat = np.array(diamons_data['carat'])
price = np.array(diamons_data['price'])
depth = np.array(diamons_data['depth'])

plt.figure(figsize=(12, 6))

sns.boxplot(x='cut',
            y=price,
            data=diamons_data,
            linewidth=2.5,
            palette='pastel')

plt.show()
