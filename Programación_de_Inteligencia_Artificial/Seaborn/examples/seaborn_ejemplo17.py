# Gráfico -- PAIRPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.pairplot(data, hue="sex", diag_kind="kde")
plt.show()

# Uso; Explorar relaciones entre múltiple variables.