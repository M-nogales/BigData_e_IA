# Gráfico de Relación. RELPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.relplot(data=data, x="total_bill", y="tip", col="time", hue="sex", kind="scatter")
plt.show()

# Uso: Comparar relaciones entre variables en diferentes subconjuntos de datos.