# Gráfico Matricial. CLUSTERMAP
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
corr = data.corr(numeric_only=True)
sns.clustermap(corr, cmap="coolwarm", annot=True)
plt.title("Cluster map de correlaciones")
plt.show()

# Uso; Agrupar características similares.