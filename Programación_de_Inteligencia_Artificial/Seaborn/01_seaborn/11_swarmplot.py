'''11. Swarmplot con ajuste de jitter
- **Dataset**: `penguins`.
- **Pasos**:
  - Convertir el tamaño de las aletas y el peso corporal a arrays de NumPy.
  - Generar un swarmplot para mostrar la relación entre estos valores.
  - Ajustar el parámetro `dodge`.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
penguins_data= sns.load_dataset('penguins')

flipper_length = np.array(penguins_data['flipper_length_mm'])
body_mass = np.array(penguins_data['body_mass_g'])

swarmplot = sns.swarmplot(x=flipper_length,
                          y=body_mass,
                          data=penguins_data,
                          hue="species",
                          dodge=True,
                          palette='viridis')

plt.show()

# with sns.scatterplot clearly better visualization
# scatterplot = sns.scatterplot(x=flipper_length,
#                               y=body_mass,
#                               data=penguins_data,
#                               hue="species",
#                               palette='viridis')
# plt.show()