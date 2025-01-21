# Gráfico Matricial. HEATMAP
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
corr = data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Mapa de calor de correlaciones")
plt.show()

#Uso; Analizar correlaciones o dependencias entre variables.