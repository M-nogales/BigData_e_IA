# Gráfico de Categorización. BARPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.barplot(data=data, x="day", y="total_bill", hue="sex", ci="sd")
plt.title("Cuenta promedio por día")
plt.show()

# Uso; Comparar promedios, como ventas por región. 