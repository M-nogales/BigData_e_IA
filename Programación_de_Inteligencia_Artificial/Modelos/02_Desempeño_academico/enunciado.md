# Predicción del Desempeño Académico de Estudiantes Basado en Factores Socioeconómicos y Académicos

El objetivo de este estudio es desarrollar un modelo de clasificación que prediga el desempeño académico de los estudiantes utilizando un conjunto de datos que contiene información sobre más de 21,000 alumnos. La clasificación se realizará en tres categorías de rendimiento: **"Bajo"**, **"Medio"** y **"Alto"**. Los factores considerados incluyen aspectos académicos, socioeconómicos y de hábitos de estudio.

Este estudio permitirá identificar patrones que influyen en el rendimiento estudiantil, ayudando a las instituciones educativas a tomar decisiones informadas y a diseñar intervenciones personalizadas para mejorar el éxito académico.

## Objetivos del Estudio

1. **Predicción**: Desarrollar un modelo de clasificación para predecir el nivel de desempeño académico de los estudiantes.
2. **Identificación de Factores Clave**: Analizar qué variables tienen mayor impacto en el rendimiento académico.
3. **Recomendaciones Educativas**: Proponer estrategias de mejora basadas en los resultados obtenidos.

## Estructura del Conjunto de Datos

| Variable                     | Descripción                                                    | Tipo de Dato  |
|------------------------------|----------------------------------------------------------------|---------------|
| edad                         | Edad del estudiante (años)                                    | Numérico      |
| genero                       | Género del estudiante (0=Mujer, 1=Hombre)                     | Categórico    |
| horas_estudio                | Promedio de horas de estudio diarias                          | Numérico      |
| asistencia                   | Porcentaje de asistencia a clases (%)                        | Numérico      |
| nivel_socieconomico          | Nivel socioeconómico (1=Bajo, 2=Medio, 3=Alto)               | Categórico    |
| acceso_internet              | Acceso a internet en casa (1=Sí, 0=No)                       | Categórico    |
| actividades_extracurriculares| Participación en actividades (1=Sí, 0=No)                    | Categórico    |
| estado_emocional             | Estado emocional autoevaluado (1=Bajo, 2=Medio, 3=Alto)      | Categórico    |
| nota_promedio_anterior       | Nota promedio del año anterior (0-100)                       | Numérico      |
| apoyo_familiar               | Nivel de apoyo familiar (1=Bajo, 2=Medio, 3=Alto)            | Categórico    |
| rendimiento_academico        | Clasificación del rendimiento (Bajo, Medio, Alto)            | Categórico    |

### A realizar:

1. **Carga y Exploración de Datos**:
   - Cargar el dataset y realizar un análisis exploratorio para identificar valores faltantes o inconsistencias. *(Dataset en formato CSV adjunto).*
   - Visualización de datos para encontrar patrones.

2. **Entrenamiento de Modelos**:
   Probar diferentes algoritmos de clasificación como:
   - Random Forest
   - Árboles de Decisión
   - K-Nearest Neighbors (KNN)
   - Support Vector Machines (SVM)

3. **Evaluación del Modelo**:
   - Utilizar métricas como precisión, recall, F1-score y AUC-ROC para evaluar el rendimiento.
   - Comparación de resultados entre diferentes algoritmos.
