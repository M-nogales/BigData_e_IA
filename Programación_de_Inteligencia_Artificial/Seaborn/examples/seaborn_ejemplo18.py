# Gráfico -- JOINTPLOT
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.jointplot(data=data, x="total_bill", y="tip", kind="reg")
plt.show()

# Uso; Relacionar dos variables con tendencias y distribuciones.