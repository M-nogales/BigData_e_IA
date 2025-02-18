# UD 02 Caracterización de Sistemas de Aprendizaje Automático

## Clasificación de Sistema de Aprendizaje Automático

1. Aprendizaje Supervisado
2. Aprendizaje No Supervisado
3. Aprendizaje Semisupervisado
4. Aprendizaje Por Refuerzo

### Aprendizaje Automático Supervisado
Tipo de aprendizaje que parte de un conjunto de datos **``etiquetados``**, se conoce el atributo de respuesta.
-existen algoritmos de Regresión y de Clasificación para predecir atributos numéricos y categórico

### Aprendizaje Automático NO Supervisado
Tipo de aprendizaje que parte de un conjunto de datos **``sin etiquetar``** y busca la agrupación de estos datos, sin ningún tipo de conocimiento para testear.

El modelo identifica patrones que le permitan separar en grupos en función de sus atributos.**"Clustering"**

### Aprendizaje Automático Semi Supervisado
Tipo mixto de los anteriores, en un conjunto de datos existen elementos etiquetados y otros que no lo están.

## Principales Técnicas de Aprendizaje Automático

| Técnicas de Aprendizaje Automático |                Forma de Almacenamiento                  |
|------------------------------------|---------------------------------------------------------|
| Redes Neuronales Artificiales      | conjunto de pesos y umbrales que conectan cada neurona  |
| Aprensizaje Inductivo              | Ramas de un árbol de decisión o conjunto de reglas      |
| Razonamiento basado en casos       | Archivo de casos                                        |
| Aprendizaje Evolutivo              | Cromosomas                                              |

### Las Redes Neuronales Artificiales (Soma, Dendritas, Axón)

- **Capa de Entrada**: encargada de **introducir** a la red información.
- **Capa Intermedia(Oculta)**:1-n capas que **procesan la información** de la capa de entrada.
- **Capa de Salida**: Suministra los resultados.

### Aprendizaje Inductivo
Sistema de aprendizaje que generaliza patrones a partir de ejemplos específicos de datos, es decir de datos extrae reglas o patrones. los datos han de ser etiquetados.

#### Pasos (RICE)
1. Recopilar ejemplos etiquetados
2. Identificar patrones
3. Construir un modelo predictivo
4. Evaluar el modelo en datos no vistos

### Razonamiento Basado en Casos (CBR)
Sistema que resuelve problemas en base de la reutilización de experiencias pasadas para resolver problemas nuevos.

Usado en IA, aprendizaje automatico y contextos con gran cantidad de datos historicos.

#### Características
- Basado en casos previos
- Reutilización
- Ciclo CBR (RRRR): el razonamiento basado en casos se estructura en un ciclo con 4 pasos
  - Recuperar: buscar casos iguales o parecidos al actual.
  - Reutilizar: adaptar lo recuperado a lo actual.
  - Revisar: validar, si es necesario, y ajustar la solución para garantizar su efectividad.
  - Retener: si ha sido exitoso, se almacena en la base de datos.

### Aprendizaje Evolutivo
Basado en la teoría evolutiva aprende y optimiza la inteligencia artificial usando la selección, mutación y cruce de información genetica para mejorar las soluciones según las generaciones.

#### Características principales
- Optimización iterativa
- Pobación de soluciones
- Selección natural
- Diversidad

## Algoritmos o modelos

### Algoritmos de Clasificación
- Regresión Logística
- Máquinas de Soporte Vectorial (SVM)
- K-Nearest neighbors (KNN)
- Árboles de Decisión
- Bosques Aleatorios
- Redes Neuronales Artificiales

### Algoritmos de Regresión
- Regresión Lineal: relación lineal entre variables
- Regresión Polinómica: relación polinómica
- Regresión de Ridge y Lasso: Versiones de regresión lineal con regularización
- Redes Neuronales para regresión: modelos no lineales para regresión compleja.

### Regresión Logística
Regresión Logística Binaria,multiclase o multietiqueta

### Máquina de Soporte Vectorial (SVM)
Su Objetivo es encontrar el **hierplano** óptimo que maximiza la margen, entre los puntos más cecanos de diferentes clases, llamados **vectores de soporte**.

