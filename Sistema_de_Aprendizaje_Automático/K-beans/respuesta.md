### **¿Cómo se distribuyen los grupos en la gráfica?**
La gráfica muestra 3 clusters: uno bien separado y dos con solapamiento parcial. El Silhouette Score (0.5528) refleja una separación moderada, limitada por la reducción dimensional (k) y la similitud entre especies.

### **Silhouette Score: ¿Qué mide?**
El **Silhouette Score** mide la calidad del clustering evaluando qué tan bien están agrupados los puntos dentro de sus clusters y qué tan separados están de otros clusters. Su valor oscila entre **-1 y 1**:

- **Cercano a 1** -> Buen clustering: los puntos están bien agrupados y separados de otros clusters.
- **Cercano a 0** -> Clusters solapados: los puntos están en el límite entre clusters.
- **Cercano a -1** -> Mal clustering: los puntos están en el cluster incorrecto.

### **Diferencia entre Cluster y Model**
- **Cluster**: Un grupo de datos que han sido agrupados basándose en su similitud. En **K-Means**, cada punto de datos se asigna a un cluster basado en su cercanía al centroide.
- **Model**: Es el algoritmo en sí, que procesa los datos y crea los clusters. En este caso, el **modelo K-Means** ajusta los datos y encuentra los mejores centroides para dividir los puntos en grupos.

### **¿Qué puntuacines nos indicarian si tenemos un buen Silhouette Score?**
- **Mayor a 0.7** -> Excelente clustering, los grupos están bien definidos.
- **Entre 0.5 y 0.7** -> Buen clustering, pero puede haber algo de solapamiento.
- **Entre 0.2 y 0.5** -> Clustering aceptable, pero se puede mejorar.
- **Menor a 0.2** -> El clustering no es bueno, los grupos pueden no ser representativos.
