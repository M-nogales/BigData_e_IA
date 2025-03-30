# Análisis Comparativo de Algoritmos de Aprendizaje No Supervisado

## 1. Diferencias Clave entre K-Means, DBSCAN y Clustering Jerárquico

| Algoritmo          | Ventajas | Desventajas |
|--------------------|----------|-------------|
| **K-Means** | Rápido y escalable, útil para grandes volúmenes de datos. | Requiere definir k previamente, sensible a la inicialización y a la escala de los datos. |
| **DBSCAN** | No necesita especificar k, detecta estructuras arbitrarias y maneja ruido. | No funciona bien en alta dimensión, requiere ajuste fino de parámetros (eps, min_samples). |
| **Clustering Jerárquico** | No requiere predefinir k, proporciona una estructura en forma de dendrograma. | Costoso computacionalmente en grandes datasets, difícil de ajustar para datos grandes. |

## 2. Comparación entre PCA y t-SNE en Reducción de Dimensionalidad

| Método  | Características | Ventajas | Desventajas |
|---------|---------------|----------|-------------|
| **PCA** | Basado en componentes principales, mantiene la varianza global. | Rápido y útil para interpretación lineal. | No captura relaciones no lineales. |
| **t-SNE** | Basado en preservación de similitudes locales, ideal para clustering visual. | Captura relaciones no lineales, excelente para visualización. | Alto costo computacional, no conserva estructura global. |

## 3. Importancia de la Detección de Anomalías en Ciberseguridad

La detección de anomalías es fundamental en ciberseguridad debido a que permite la identificación de amenazas tales como accesos no autorizados, fraudes y ataques de malware. Técnicas como Isolation Forest, One-Class SVM y Autoencoders son comúnmente utilizadas para detectar comportamientos sospechosos en grandes volúmenes de datos en tiempo real.

Ejemplo: En detección de intrusos en redes, se monitorean patrones de tráfico y se identifican anomalías basadas en desviaciones respecto al comportamiento normal de los usuarios.

## 4. Casos Reales de Aplicación

- **K-Means**: Segmentación de clientes en marketing digital para campañas personalizadas.
- **DBSCAN**: Detección de formaciones de galaxias en astronomía, ya que permite descubrir estructuras densas en datos espaciales.
- **Clustering Jerárquico**: Agrupación de documentos basada en similitudes semánticas en motores de búsqueda.
- **PCA**: Reducción de dimensionalidad en reconocimiento facial para mejorar la eficiencia de los modelos de clasificación.
- **t-SNE**: Análisis de datos genómicos para descubrir patrones en la expresión genética de enfermedades.