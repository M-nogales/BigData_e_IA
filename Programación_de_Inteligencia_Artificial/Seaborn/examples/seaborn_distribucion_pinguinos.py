import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
#Histograma
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plt.show()

#Estimación de densidad
sns.kdeplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plt.show()

# Distribución - histograma (con DISPLOT)
sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plt.show()

# Estimación de densidad (con DISPLOT)
sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack", kind="kde")
plt.show()

#Distribución con múltiples gráficos
sns.displot(data=penguins, x="flipper_length_mm", hue="species", col="species")
plt.show()

# Generar funciones de nivel
f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
sns.scatterplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", ax=axs[0])
sns.histplot(data=penguins, x="species", hue="species", shrink=.8, alpha=.8, legend=False, ax=axs[1])
f.tight_layout()
plt.show()

# Funciones a nivel de figura
tips = sns.load_dataset("tips")
g = sns.relplot(data=tips, x="total_bill", y="tip")
g.ax.axline(xy1=(10, 2), slope=.2, color="b", dashes=(5, 2))
plt.show()

# Personalizar gráficos (p.e. etiquetas de ejes)
g = sns.relplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", col="sex")
g.set_axis_labels("Flipper length (mm)", "Bill length (mm)")
plt.show()

# Combinar múltiples vistas de gfráficos
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")
plt.show()

# Múltiples vistas combinando variables
sns.pairplot(data=penguins, hue="species")
plt.show()

# propiedad Kind - Cambia representación
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", kind="hist")
plt.show()