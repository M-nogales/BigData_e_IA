# Gráfico de Categorización. COUNTPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.countplot(data=data, x="day", hue="sex")
plt.title("Cantidad de observaciones por día")
plt.show()

# Uso; Evaluar la frecuencia de eventos categóricos.