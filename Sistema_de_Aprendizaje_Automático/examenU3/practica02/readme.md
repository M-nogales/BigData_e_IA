# Predecir el Precio de  Viviendas
Implementar un modelo de Regresión Lineal para predecir el precio de viviendas basado en variables como el número de habitaciones y la ubicación.

1. Carga y exploración de Datos
   
   1. Descarga y carga el dataset Boston Housing desde SCIKIT-LEARN
   2. Explora el Dataset mostrando las primeras filas
   
2. Preprocesamiento de datos
   
   1. Selecciona las características más relevantes (RM:número de habitaciones y LSTAT: porcentaje de población de bajos ingresos)
   2. Divide los datos en 80% entrenamiento y 20% prueba
   
3. Construcción del Modelo
   
   1. Entrena un modelo de Regresión Lineal con Scikit-Learn.
   2. Obtén las predicciones del modelo
   
4. Evaluación del modelo

   1. Calcula las métricas de error MSE y R2
   2. Visualiza la relación entre las predicciones y los valores reales
   
5. Analisis y mejoras
   
   1. Prueba eliminando o agregando nuevas variables en X y analiza si el modelo mejora.
   2. Evalúa la necesidad de normalización de los datos.
   3. Compara el modelo con otro enfoque, como Regresión Ridge o Lasso