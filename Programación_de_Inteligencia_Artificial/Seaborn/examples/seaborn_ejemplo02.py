# Gráfico de Relación. SCATTERPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.scatterplot(data=data, x="total_bill", y="tip", hue="sex", style="time")
plt.title("Relación entre cuenta total y propina")
plt.show()

# Uso; análisis de correlaciones simples, por ejemplo, entre ventas y gastos publicitarios.
