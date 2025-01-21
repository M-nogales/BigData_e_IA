# DATASET de Ejemplos para trabajar con SEABORN
import seaborn as sns
import matplotlib.pyplot as plt

# Listar todos los datasets disponibles
print(sns.get_dataset_names())
print(" ------------------------- ")

# Cargamos algunos ejemplos......
propinas = sns.load_dataset("tips")
print(propinas.head())
print(" ------------------------- ")
pingus = sns.load_dataset("penguins")
print(pingus.head())
print(" ------------------------- ")
iris = sns.load_dataset("iris")
print(iris.head())
print(" ------------------------- ")
diamantes = sns.load_dataset("diamonds")
print(diamantes.head())
print(" ------------------------- ")
titanic = sns.load_dataset("titanic")
print(titanic.head())
print(" ------------------------- ")
vuelos = sns.load_dataset("flights")
print(vuelos.head())
print(" ------------------------- ")
combustible = sns.load_dataset("mpg")
print(combustible.head())
print(" ------------------------- ")
planetas = sns.load_dataset("planets")
print(planetas.head())
print(" ------------------------- ")
resonancias = sns.load_dataset("fmri")
print(resonancias.head())
print(" ------------------------- ")
puntos = sns.load_dataset("dots")
print(puntos.head())
print(" ------------------------- ")
dowjones = sns.load_dataset("dowjones")
print(dowjones.head())
print(" ------------------------- ")

sns.relplot(data=dowjones, x="Date", y="Price", kind="line")
plt.show()

sns.relplot(data=resonancias, x="timepoint", y="signal", kind="line")
plt.show()

sns.relplot(
    data=resonancias, kind="line",
    x="timepoint", y="signal", errorbar=None,
)
plt.show()
sns.relplot(
    data=resonancias, kind="line",
    x="timepoint", y="signal",
    estimator=None,
)
plt.show()
