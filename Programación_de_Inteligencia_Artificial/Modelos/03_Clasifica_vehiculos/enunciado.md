# Análisis de Datos de Vehículos y Comparación de Algoritmos de Regresión

Realizar un estudio exhaustivo de un conjunto de datos de 15,000 registros sobre vehículos, disponible en formato CSV, para aplicar diversos algoritmos de regresión con el fin de determinar el modelo más preciso para la predicción del precio de los automóviles.

## Algoritmos de Regresión a Evaluar

1. Regresión Lineal  
2. Regresión Polinómica  
3. Regresión Ridge  
4. Regresión Lasso  

El dataset proporcionado contiene información sobre diversos atributos de los vehículos que impactan en su precio.

## Atributos del Dataset

- **ID**: Identificador único del vehículo  
- **Year**: Año de fabricación  
- **Mileage**: Kilometraje recorrido en kilómetros  
- **EngineSize**: Tamaño del motor en litros  
- **FuelType**: Tipo de combustible (codificado)  
- **Transmission**: Tipo de transmisión (codificado)  
- **Horsepower**: Potencia del motor en HP  
- **Price**: Precio del vehículo (variable objetivo)  

## Pasos del Análisis

### 1. Carga de Datos
- Importar los datos desde el archivo CSV utilizando Pandas.

### 2. Exploración de Datos
- Realizar un análisis exploratorio de los datos (EDA), incluyendo:
  - Estadísticas descriptivas.
  - Visualización de la distribución de las variables.
  - Correlaciones entre variables.

### 3. Preparación de los Datos
- Manejo de valores nulos.
- Normalización de datos numéricos.
- Codificación de variables categóricas.
- División en conjuntos de entrenamiento y prueba (80%-20%).

### 4. Aplicación de Algoritmos
- Implementar los algoritmos de regresión mencionados utilizando la librería scikit-learn.
- Entrenar los modelos con el conjunto de entrenamiento.
- Evaluar el rendimiento de los modelos con el conjunto de prueba.

### 5. Métricas de Evaluación
- **Error Cuadrático Medio (MSE)**  
- **Error Absoluto Medio (MAE)**  
- **Coeficiente de Determinación (R²)**  

### 6. Comparación de Resultados
- Comparar los resultados obtenidos por cada modelo.
- Seleccionar el mejor modelo según las métricas de evaluación.

### 7. Conclusiones y Recomendaciones
- Interpretar los resultados obtenidos.
- Proponer posibles optimizaciones para mejorar la predicción.
