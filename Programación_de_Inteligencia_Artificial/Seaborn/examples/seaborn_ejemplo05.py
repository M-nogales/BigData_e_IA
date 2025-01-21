# Gráfico de Distribución. HISTPLOT (Histograma)
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.histplot(data=data, x="total_bill", bins=10, kde=True, hue="sex")
plt.title("Distribución de cuenta total")
plt.show()

# Uso; Visualizar distribuciones, por ejemplo, ingresos de usuarios. 