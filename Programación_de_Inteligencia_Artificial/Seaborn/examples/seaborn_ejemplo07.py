# Gráfico de Distribución. ECDFPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.ecdfplot(data=data, x="tip", hue="sex")
plt.title("Distribución acumulativa de propinas")
plt.show()

# Uso; Analizar percentiles o umbrales, como p.e. ingresos del 10% superior

