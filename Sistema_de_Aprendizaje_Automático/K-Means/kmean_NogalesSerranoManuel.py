import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# Cargar el dataset IRIS
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Aplicar K-Means con k=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(df)

# Calcular el Silhouette Score
sil_score = silhouette_score(df[data.feature_names], df['cluster'])
print(f"Silhouette Score: {sil_score:.4f}")

# Reducir dimensiones para visualización con PCA
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df[data.feature_names])

# Graficar los clusters
plt.figure(figsize=(8, 6))
plt.scatter(df_pca[:, 0], df_pca[:, 1], c=df['cluster'], cmap='viridis', edgecolors='k')
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.title("Clustering de IRIS con K-Means")
plt.colorbar(label="Cluster")
plt.show()

# Los grupos en la gráfica se distribuyen en tres conjuntos bien definidos, 
# aunque pueden presentar cierta superposición debido a las similitudes entre especies.
# La reducción de dimensiones con PCA permite visualizar mejor la separación de los clusters,
# aunque en el espacio original (4D) la separación es más clara.
