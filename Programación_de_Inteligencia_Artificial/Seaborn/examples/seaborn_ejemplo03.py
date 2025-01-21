# Gráfico de Relación. LINEPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.lineplot(data=data, x="size", y="tip", hue="sex")
plt.title("Propinas según tamaño del grupo")
plt.show()
# Uso; Mostrar tendencias en ventas, crecimiento poblacional, etc.
