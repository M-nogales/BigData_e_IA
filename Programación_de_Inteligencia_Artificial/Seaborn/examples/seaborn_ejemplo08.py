# Gráfico de Distribución. RUGPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.rugplot(data=data, x="total_bill")
plt.title("Distribución de datos con Rugplot")
plt.show()

# Uso; resaltar valores individuales en una distribución.