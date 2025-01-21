# Gráfico de Distribución. KDEPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.kdeplot(data=data, x="total_bill", hue="sex", fill=True)
plt.title("Densidad de cuenta total")
plt.show()

# Uso; Identificar patrones en distribuciones (p.e.: detección de anomalías)