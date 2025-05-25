Características del recurso humano:
todos float excepto experiencia

Experiencia:

Rendimiento personal (0-10): 

Habilidades técnicas (lenguaje-(0-10)): [Python,4]

soft skills:

carga de trabajo (0-10)

Cargo o nivel en la empresa

Características de la tarea:
Tipo de tarea (categoría)

Nivel de dificultad

Herramientas requeridas

Tiempo estimado

Área o departamento
---
# Proyecto: Predicción de Éxito de Tareas Asignadas a Recursos Humanos
Este proyecto tiene como objetivo predecir el éxito de las tareas asignadas a los recursos humanos de una empresa, utilizando un modelo de machine learning. El modelo se entrena con datos históricos de empleados y sus tareas, y se evalúa su rendimiento en función de diversas métricas. Los resultados pueden no ajustarse a la realidad debido a la naturaleza sintética de los datos generados.

## Generación de Datos Sintéticos
Para la generación de datos sintéticos, se utiliza el script `task_generator`, que usando la api gratuita de gemini crea tareas en formato json siguiendo el prompt dado.

## Creación del Modelo

Este script en Python implementa un pipeline completo para generar un modelo de clasificación que predice si una asignación de tarea será **terminada a tiempo** por un empleado, basándose en datos simulados y características de los empleados y tareas.

### Descripción General

El pipeline realiza las siguientes tareas de forma automática:

1. **Carga y procesamiento inicial de datos**:

   * Lee un archivo JSON con tareas (`generated_tasks.json`).
   * Lee un CSV con información del personal (`RRHH.csv`).
   * Limpia y normaliza datos, incluyendo procesamiento de habilidades técnicas y fechas de contratación.

2. **Simulación de asignaciones**:

   * Crea asignaciones simuladas de tareas a empleados para generar datos de entrenamiento.
   * Combina datos de empleados y tareas para formar un dataset completo.

3. **Ingeniería de características y creación del objetivo**:

   * Calcula la antigüedad del empleado (tenure).
   * Crea un puntaje de correspondencia de habilidades entre la tarea y el empleado.
   * Genera artificialmente la variable objetivo `Finished_On_Time` (terminó a tiempo) en base a reglas heurísticas sobre las características.

4. **Selección y limpieza de características**:

   * Define las variables predictoras (numéricas y categóricas).
   * Imputa valores faltantes con la mediana (numéricas) o una categoría especial `'Missing'` (categóricas).

5. **Preprocesamiento y pipeline de modelado**:

   * Escala características numéricas con `StandardScaler`.
   * Codifica variables categóricas con `OneHotEncoder`.
   * Define un pipeline que incluye preprocesamiento y un modelo de regresión logística balanceado.

6. **Entrenamiento y evaluación del modelo**:

   * Divide los datos en entrenamiento y prueba (70/30) con estratificación si es posible.
   * Entrena el modelo.
   * Evalúa con métricas: exactitud, AUC-ROC, log loss y reporte de clasificación.

7. **Predicción y guardado del modelo**:

   * Predice probabilidades para el conjunto de prueba.
   * Guarda el modelo entrenado en `trained_model.pkl`.

---

### Uso

Ejecutar el script directamente:

```bash
python model_2_1.py
```

Asegúrate de tener los archivos:

* `generated_tasks.json`: archivo JSON con las tareas y sus características.
* `datasets/RRHH.csv`: archivo CSV con los datos de los empleados.

---

### Detalles técnicos

* **Archivos de entrada**:

  * `generated_tasks.json`: Debe contener un array JSON con campos como `"Task Description"`, `"Category"`, `"Skill"`, `"Difficulty Level"`, `"Estimated Time (hrs)"` y `"Area"`.
  * `RRHH.csv`: Información del empleado, con columnas clave como `Employee_ID`, `technical_abilities` (string con diccionario), `Hire_Date`, `Gender`, `Department`, `Job_Title`, `Education_Level`, etc.

* **Procesamiento de habilidades técnicas**:

  * Convierte strings que representan diccionarios en objetos Python.
  * Limpia y normaliza las claves (skills) a minúsculas.

* **Simulación de asignaciones**:

  * Asigna aleatoriamente tareas a empleados.
  * Realiza uniones (merge) para combinar datos de empleados y tareas.

* **Creación de la variable objetivo**:

  * Basada en reglas heurísticas que combinan puntaje de habilidades, desempeño, antigüedad y horas extra.
  * Probabilidad ajustada para simular un comportamiento realista.

* **Modelo**:

  * Regresión logística con solver `liblinear` y balanceo de clases.
  * Pipeline que incluye escalado y codificación.

* **Evaluación**:

  * Métricas impresas en consola.
  * Reporte de clasificación detallado.

---

### Salidas

* Modelo entrenado guardado en `trained_model.pkl`.
* Impresión en consola de:

  * Información de carga y procesamiento de datos.
  * Estadísticas de distribución de la variable objetivo.
  * Métricas de evaluación.
  * Ejemplo de predicciones con probabilidades.

---

### Notas y advertencias

* El script tiene manejo básico de errores para archivos faltantes o datos mal formateados.
* El target es generado artificialmente para simular un escenario de clasificación supervisada.
* Requiere datasets adecuados para funcionar correctamente.
* Ajustes en la generación del target o el modelo pueden ser necesarios para adaptarse a casos reales.

## Tipo de campos del modelo

| Tipo       | Campo                         |
| ---------- | ----------------------------- |
| Numérico   | Age                           |
| Numérico   | Years_At_Company              |
| Numérico   | Performance_Score             |
| Numérico   | Monthly_Salary                |
| Numérico   | Work_Hours_Per_Week           |
| Numérico   | Projects_Handled              |
| Numérico   | Overtime_Hours                |
| Numérico   | Sick_Days                     |
| Numérico   | Remote_Work_Frequency         |
| Numérico   | Team_Size                     |
| Numérico   | Training_Hours                |
| Numérico   | Promotions                    |
| Numérico   | Employee_Satisfaction_Score   |
| Numérico   | Tenure_Years                  |
| Numérico   | Skill_Match_Score             |
| Categórico | Department                    |
| Categórico | Gender                        |
| Categórico | Job_Title                     |
| Categórico | Education_Level               |
| Categórico | Category                      |

## Importancia de las variables del modelo (metrics.py)

| Variable                                | Coeficiente  | Importancia (abs) |
|-----------------------------------------|-------------|------------------|
| cat__Job_Title_technician               | 1.134841    | 1.134841         |
| num__Employee_Satisfaction_Score        | -0.820850   | 0.820850         |
| cat__Category_data science              | -0.809872   | 0.809872         |
| cat__Education_Level_master             | -0.753677   | 0.753677         |
| num__Overtime_Hours                     | -0.742161   | 0.742161         |
| cat__Department_legal                   | 0.692694    | 0.692694         |
| cat__Category_project management        | 0.535744    | 0.535744         |
| cat__Education_Level_phd                | 0.535176    | 0.535176         |
| cat__Gender_male                        | 0.486955    | 0.486955         |
| cat__Category_devops                    | -0.465033   | 0.465033         |
| num__Performance_Score                  | 0.430786    | 0.430786         |
| num__Skill_Match_Score                  | 0.419866    | 0.419866         |
| cat__Category_cloud                     | 0.404043    | 0.404043         |
| cat__Department_hr                      | -0.397032   | 0.397032         |
| num__Team_Size                          | -0.389600   | 0.389600         |
| cat__Category_testing                   | -0.386628   | 0.386628         |
| cat__Category_documentation             | -0.362645   | 0.362645         |
| num__Work_Hours_Per_Week                | -0.327646   | 0.327646         |
| cat__Job_Title_specialist               | 0.315464    | 0.315464         |
| cat__Job_Title_engineer                 | -0.263041   | 0.263041         |
| cat__Category_database                  | -0.233196   | 0.233196         |
| num__Monthly_Salary                     | -0.227385   | 0.227385         |
| cat__Category_backend                   | -0.205156   | 0.205156         |
| num__Remote_Work_Frequency              | -0.200450   | 0.200450         |
| num__Years_At_Company                   | 0.200206    | 0.200206         |
| num__Tenure_Years                       | -0.196562   | 0.196562         |
| cat__Category_ui/ux design              | -0.189007   | 0.189007         |
| cat__Department_it                      | 0.187562    | 0.187562         |
| cat__Department_sales                   | -0.185446   | 0.185446         |
| cat__Job_Title_consultant               | 0.166160    | 0.166160         |
| num__Training_Hours                     | -0.152178   | 0.152178         |
| num__Age                                | -0.149507   | 0.149507         |
| num__Sick_Days                          | 0.148444    | 0.148444         |
| cat__Education_Level_high school        | -0.126483   | 0.126483         |
| cat__Department_finance                 | 0.113874    | 0.113874         |
| cat__Job_Title_developer                | -0.100374   | 0.100374         |
| cat__Category_frontend                  | 0.083986    | 0.083986         |
| num__Promotions                         | 0.076315    | 0.076315         |
| cat__Department_marketing               | -0.060192   | 0.060192         |
| num__Projects_Handled                   | 0.059784    | 0.059784         |
| cat__Department_engineering             | -0.058541   | 0.058541         |
| cat__Category_database administration   | -0.051395   | 0.051395         |
| cat__Gender_other                       | -0.045938   | 0.045938         |
| cat__Department_operations              | -0.041717   | 0.041717         |
| cat__Job_Title_manager                  | 0.004098    | 0.004098         |

## Guía de uso del la app
Para utilizar la aplicación, simplemente ejecuta app.py(es necesario tener instalado flask y pandas) una vez ejecutado entra en la url proporcionada en la consola y rellena el formulario, como ejemplo para cada tipo de resultado puedes utilizar los del siguiente apartado, una vez rellenado el formulario pulsa en el botón de predecir y te mostrará si la tarea se completará a tiempo o no.

## Ejemplo de datos para cada resultado del modelo
| Campo                     | Resultado 1 | Resultado 0|
|---------------------------|----------------------------------|----------------------------------|
| Edad                      | 25                               | 45                               |
| Años en la empresa        | 3                                | 0                                |
| Fecha de ingreso          | 18/01/2023                       | 01/01/2023                       |
| Calificación de desempeño | 5                                | 5                                |
| Sueldo mensual            | 2300                             | 900                              |
| Horas por semana          | 18                               | 50                               |
| Proyectos manejados       | 3                                | 0                                |
| Horas extra               | 2                                | 10                               |
| Días de enfermedad        | 5                                | 0                                |
| Frecuencia de trabajo remoto | 3                             | 10                               |
| Tamaño del equipo         | 8                                | 10                               |
| Horas de entrenamiento    | 5                                | 0                                |
| Número de promociones     | 2                                | 0                                |
| Satisfacción del empleado | 8                                | 5                                |
| Habilidades técnicas      | {"python":3,"sql":4}             | {"python":10,"sql":9}            |
| Departamento              | Engineering                      | hr                               |
| Cargo                     | Engineering                      | engineer                         |
| Nivel educativo           | Bachelor                         | master                           |
| Género                    | male                             | female                           |
| Descripción de la tarea   | Write technical python specifications | Build a flask API           |
| Categoría                 | backend                          | data science                     |
| Habilidad requerida       | python                           | flask                            |