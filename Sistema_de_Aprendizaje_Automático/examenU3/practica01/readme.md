# Clasificador de Imágenes con K-vecinos Más Cercanos (KNN)
Aplicar el algoritmo KNN para clasificar imágenes del dataset MNIST y analizar su rendimiento con diferentes valores de K
1. Carga y exploración de Datos
   1. importa las librerías necesarias
   2. descarga el dataset ``MNIST`` que contiene imágenes de dígitos escritos a mano (0-9)
   3. Divide los datos en ``80% entrenamiento y 20% prueba``
   4. Normaliza los datos para mejorar el rendimiento del modelo
2. Entrenamiento del modelo
   1. Implementa un modelo KNN con ``K = 3``
   2. Realiza Predicciones en el conjunto de prueba
3. Evaluación del modelo
   1. Muestra un reporte de clasificación con precisión, recall y F1-score
   2. calcula y muestra la matríz de confusión
4. Experimentación con diferentes valores de K
   1. Evalua el modelo con k = 1, 3, 5, 7, 9 y registra los valores de la precisión
   2. Genera un gráfico que muestre la relación entre K y la precisión del modelo