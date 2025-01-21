# Gráfico de Categorización. VIOLINPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.violinplot(data=data, x="day", y="total_bill", hue="sex", split=True)
plt.title("Distribución de cuenta total (Violinplot)")
plt.show()

# Uso; Analizar distribuciones complejas con múltiples categorías.