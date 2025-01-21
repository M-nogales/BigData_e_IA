# Gráfico de Categorización. STRIPPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.stripplot(data=data, x="day", y="total_bill", hue="sex", dodge=True)
plt.title("Puntos individuales por día")
plt.show()

# USo; Visualizar puntos individuales dentro de categorías.