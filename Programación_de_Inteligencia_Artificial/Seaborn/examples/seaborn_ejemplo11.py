# Gráfico de Categorización. BOXPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.boxplot(data=data, x="day", y="total_bill", hue="sex")
plt.title("Distribución de cuenta total por día")
plt.show()

# Uso; Comparar distribuciones, como p.e. rendimiento por departamento.