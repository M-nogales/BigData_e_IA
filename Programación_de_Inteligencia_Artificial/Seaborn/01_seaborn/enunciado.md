# Análisis de Datos y Visualizaciones en Python

## 1. Gráfico de dispersión avanzado con estilo personalizado
- **Dataset**: `mpg` de Seaborn.
- **Pasos**:
  - Convertir las columnas `horsepower`, `weight` y `mpg` a arrays de NumPy.
  - Crear un gráfico de dispersión donde:
    - El tamaño de los puntos represente el peso.
    - El color represente la eficiencia de combustible.
  - Personalizar con temas y ajustes de tamaño.

---

## 2. Análisis de correlación con mapa de calor
- **Dataset**: `penguins` de Seaborn.
- **Pasos**:
  - Convertir todas las variables numéricas a arrays.
  - Calcular la matriz de correlación.
  - Visualizar la correlación con un mapa de calor:
    - Incluir anotaciones.
    - Personalizar la paleta de colores.

---

## 3. Distribución de datos con KDE Plot y rug plot
- **Dataset**: `tips` de Seaborn.
- **Pasos**:
  - Convertir las columnas `total_bill` y `tip` a arrays.
  - Generar un gráfico de densidad kernel (KDE) superpuesto con un gráfico de rug.
  - Ajustar el ancho de banda y experimentar con estilos de visualización.

---

## 4. Boxplot multivariado con ajuste de estilo
- **Dataset**: `diamonds`.
- **Pasos**:
  - Convertir las columnas `carat`, `price` y `depth` a arrays de NumPy.
  - Crear un gráfico de caja para analizar:
    - La distribución de precios en diferentes rangos de quilates.
    - Segmentar por el tipo de corte.
  - Personalizar estilos de borde y paletas.

---

## 5. Violin plot con categorización de datos
- **Dataset**: `iris`.
- **Pasos**:
  - Convertir la columna de longitud del sépalo y la especie a arrays de NumPy.
  - Generar un violin plot para analizar la distribución de la longitud del sépalo por especie.
  - Ajustar la división interna y mostrar puntos individuales.

---

## 6. Gráfico de barras con agregación de datos
- **Dataset**: `titanic`.
- **Pasos**:
  - Convertir las columnas `class` y `fare` a arrays.
  - Crear un gráfico de barras que muestre:
    - El promedio de tarifas pagadas por clase.
    - Las desviaciones estándar indicadas.
  - Aplicar una paleta de color diferenciada por género.

---

## 7. FacetGrid con múltiples gráficos de distribución
- **Dataset**: `fmri`.
- **Pasos**:
  - Convertir las columnas de `tiempo` y `respuesta` a arrays de NumPy.
  - Crear una cuadrícula de gráficos de KDE por sujeto para comparar patrones de respuesta.
  - Personalizar la disposición de las subparcelas.

---

## 8. Pairplot para el análisis multivariado
- **Dataset**: `iris`.
- **Pasos**:
  - Convertir todas las columnas numéricas a arrays.
  - Generar un pairplot con:
    - Diferentes tipos de gráficos en la diagonal y fuera de la diagonal.
    - Estilos personalizados y regresión lineal para las relaciones.

---

## 9. Gráfico de líneas con datos de series temporales
- **Datos**: DataFrame simulado con datos de ventas diarias.
- **Pasos**:
  - Convertir los datos simulados a arrays.
  - Crear un gráfico de líneas para analizar tendencias estacionales.
  - Aplicar un suavizado con Seaborn y personalizar las líneas con estilos diferenciados.

---

## 10. Catplot para variables categóricas con ajuste de orden
- **Dataset**: `exercise`.
- **Pasos**:
  - Convertir las columnas `duración` y `tipo de ejercicio` a arrays.
  - Crear un catplot de tipo stripplot para observar:
    - La dispersión de duración en diferentes tipos de ejercicio.
  - Ajustar el orden de categorías y el ancho de puntos.

---

## 11. Swarmplot con ajuste de jitter
- **Dataset**: `penguins`.
- **Pasos**:
  - Convertir el tamaño de las aletas y el peso corporal a arrays de NumPy.
  - Generar un swarmplot para mostrar la relación entre estos valores.
  - Ajustar el parámetro `dodge`.

---

## 12. Regresión lineal múltiple con visualización avanzada
- **Dataset**: `mpg`.
- **Pasos**:
  - Convertir las columnas de potencia (`horsepower`) y peso (`weight`) a arrays.
  - Generar un gráfico de regresión múltiple mostrando:
    - La relación entre peso y potencia.
    - Diferentes niveles de confianza.
