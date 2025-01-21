# Gráfico de Categorización. SWARMPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.swarmplot(data=data, x="day", y="total_bill", hue="sex", dodge=True)
plt.title("Swarmplot: distribución ajustada")
plt.show()

# Uso; Mostrar valores individuales distribuidos.