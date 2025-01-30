# Predicción de Enfermedades Cardíacas Basada en Factores de Riesgo Clínicos

Se requiere desarrollar un modelo de clasificación que ayude a predecir la presencia de enfermedades cardíacas en pacientes, utilizando un conjunto de datos clínicos con más de 10,000 muestras. El objetivo es identificar de manera precisa si un paciente tiene o no una enfermedad cardíaca en función de diversas métricas de salud.

El conjunto de datos contiene información recopilada de pacientes de diferentes edades, géneros y antecedentes médicos, abarcando múltiples factores de riesgo relacionados con enfermedades cardiovasculares.

## Objetivos del Estudio

1. **Construcción del Modelo**: Entrenar y evaluar diferentes algoritmos de clasificación para predecir la presencia de enfermedades cardíacas.
2. **Análisis de Factores de Riesgo**: Determinar qué variables tienen mayor impacto en la predicción de la enfermedad.
3. **Optimización del Modelo**: Comparar el desempeño de varios algoritmos para seleccionar el más adecuado en términos de precisión, sensibilidad y especificidad.

## Estructura del Conjunto de Datos


| Variable                     | Descripción                                                    | Tipo de Dato  |
|------------------------------|----------------------------------------------------------------|---------------|
| edad                         | Edad del paciente (años)                                       | Numérico      |
| sexo                         | Género del paciente (0=Mujer, 1=Hombre)                        | Categórico    |
| presion_sistolica            | Presión arterial sistólica (mm Hg)                             | Numérico      |
| presion_diastolica           | Presión arterial diastólica (mm Hg)                            | Numérico      |
| colesterol                   | Nivel de colesterol (mg/dL)                                    | Numérico      |
| glucosa                      | Nivel de glucosa en ayunas (mg/dL)                             | Numérico      |
| indice_masa_corporal         | Índice de Masa Corporal (IMC)                                  | Numérico      |
| actividad_fisica             | Nivel de acticidad física (1 Regular,0 Sedentario)             | Categórico    |
| fumar                        | Fumador actual (1=Sí, 0=No)                                    | Categórico    |
| historia_familiar            | Antecedentes familiares de enfermedad cardiaca (Sí/No)         | Categórico    |
| diabetes                     | Diagnostico de diabetes previo (1=Sí,0=No)                     | Categórico    |
| enfermedad_cardiaca          | Presencia de enfermedad cardiaca (1=Sí,0=No)                   | Categórico    |


### A realizar:

1. **Carga y Exploración de Datos**:
   - Cargar el dataset y realizar un análisis exploratorio para identificar valores faltantes o inconsistencias. *(Dataset en formato CSV adjunto).*
   - Visualización de datos para encontrar patrones en los factores de riesgo.

2. **Entrenamiento de Modelos**:
   Probar diferentes algoritmos de clasificación como:
   - Regresión Logística
   - Árboles de Decisión
   - Random Forest
   - Support Vector Machines (SVM)

3. **Evaluación del Modelo**:
   - Utilizar métricas como precisión, recall, F1-score y AUC-ROC para evaluar el rendimiento.
   - Comparación de resultados entre diferentes algoritmos.