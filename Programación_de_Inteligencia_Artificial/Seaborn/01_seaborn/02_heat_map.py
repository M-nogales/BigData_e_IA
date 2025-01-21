'''2. Análisis de correlación con mapa de calor
- **Dataset**: `penguins` de Seaborn.
- **Pasos**:
  - Convertir todas las variables numéricas a arrays.
  - Calcular la matriz de correlación.
  - Visualizar la correlación con un mapa de calor:
    - Incluir anotaciones.
    - Personalizar la paleta de colores.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
mpg_data= sns.load_dataset('penguins')
mpg_data = mpg_data.dropna()
print(mpg_data)

# Convertir todas las variables numéricas a arrays
bill_length_mm = np.array(mpg_data['bill_length_mm'])
bill_depth_mm = np.array(mpg_data['bill_depth_mm'])
flipper_length_mm = np.array(mpg_data['flipper_length_mm'])
body_mass_g = np.array(mpg_data['body_mass_g'])

# Calcular la matriz de correlación
correlation_matrix = np.corrcoef([bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g])

# Visualizar la correlación con un mapa de calor
sns.set_theme(style='whitegrid')

map=sns.heatmap(correlation_matrix,
            annot=True,
            cmap='viridis')

map.text(0, 0, 'Hi', fontsize=12, ha='center')

plt.show()

'''
# Calcular la matriz de correlación con las columnas numéricas
correlation_matrix = mpg_data.corr(numeric_only=True)

# Visualizar la matriz de correlación con un mapa de calor
sns.heatmap(correlation_matrix, 
            annot=True, 
            cmap='flare',
            xticklabels=correlation_matrix.columns, 
            yticklabels=correlation_matrix.columns)

plt.title('Matriz de Correlación - Penguins')

plt.show()
'''