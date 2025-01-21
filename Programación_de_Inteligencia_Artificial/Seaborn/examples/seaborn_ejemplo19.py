# Gráfico -- FACETGRID
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
g = sns.FacetGrid(data, col="sex", row="time")
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()

#Uso; Comparar patrones en subconjuntos, como p.e. género o tiempo.