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
------
¡Claro! Vamos a construir ese modelo. El objetivo es predecir la probabilidad de éxito de una tarea basándonos en las características del recurso humano asignado y la tarea en sí.

**Paso 1: Entender los Datos y el Objetivo**

Tenemos dos fuentes de datos:

1.  `task_categories.csv`: Describe tareas, su categoría general y la habilidad *específica* requerida para *esa instancia* de la tarea.
2.  `recursos_humanos.csv`: Describe a los empleados con su experiencia, rendimiento, habilidades blandas, carga de trabajo y un diccionario de habilidades técnicas con su nivel de competencia.

El objetivo es, para una asignación específica (Recurso X haciendo Tarea Y), predecir la probabilidad de que la tarea sea completada con éxito.

**Pregunta Clave / Limitación Principal:**

* **¿Cómo se define el "éxito"?** Tus datos actuales describen las tareas y los recursos, pero *no* contienen información histórica sobre si las asignaciones pasadas fueron exitosas o no. **Para entrenar un modelo de Machine Learning supervisado que prediga el éxito, necesitamos ejemplos de tareas pasadas donde sepamos el resultado (Éxito = 1, Fracaso = 0).**

**Solución Propuesta (Dada la Limitación):**

Como no tenemos datos históricos de éxito, vamos a hacer lo siguiente:

1.  **Crear un Conjunto de Datos Combinado:** Simularemos asignaciones de tareas a recursos.
2.  **Ingeniería de Características:** Crearemos características relevantes para cada asignación simulada. La más importante será el **"Nivel de Coincidencia de Habilidad"**: qué tan competente es el recurso en la habilidad específica requerida por la tarea. También usaremos las otras métricas del recurso (experiencia, rendimiento, etc.).
3.  **Generar un Objetivo Sintético (Simulado):** Crearemos una columna "Éxito" artificialmente. **Es crucial entender que esto es una simulación.** En un escenario real, usarías datos históricos. Para este ejemplo, podemos basar el éxito simulado en la lógica de que una alta coincidencia de habilidad y buen rendimiento aumentan la probabilidad de éxito.
4.  **Entrenar un Modelo:** Usaremos un modelo de clasificación (como Regresión Logística, que es bueno para probabilidades) para aprender la relación entre las características y el éxito simulado.
5.  **Crear una Función de Predicción:** Esta función tomará un ID de recurso y una descripción de tarea, calculará las características relevantes y usará el modelo entrenado para predecir la probabilidad de éxito.

**Paso 2: Implementación en Python**

```python
import pandas as pd
import ast  # Para convertir el string del diccionario de habilidades en un diccionario real
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import warnings

warnings.filterwarnings('ignore', category=FutureWarning) # Ignorar avisos futuros de pandas/sklearn

# --- Carga de Datos ---
try:
    tasks_df = pd.read_csv('task_categories.csv')
    resources_df = pd.read_csv('recursos_humanos.csv')
except FileNotFoundError as e:
    print(f"Error: No se encontró el archivo {e.filename}. Asegúrate de que los CSV estén en el mismo directorio.")
    exit()

print("Datos de Tareas:")
print(tasks_df.head())
print("\nDatos de Recursos Humanos:")
print(resources_df.head())

# --- Preprocesamiento ---

# 1. Convertir el string de 'Habilidades técnicas' en un diccionario real
def parse_skills(skills_str):
    try:
        # Usar ast.literal_eval para convertir de forma segura el string a diccionario
        return ast.literal_eval(skills_str)
    except (ValueError, SyntaxError):
        # Si hay algún problema (formato incorrecto, vacío), devolver un diccionario vacío
        return {}

resources_df['Habilidades_dict'] = resources_df['Habilidades técnicas'].apply(parse_skills)

# Revisar si hubo errores en la conversión (diccionarios vacíos inesperados)
empty_skills_count = resources_df['Habilidades_dict'].apply(lambda x: len(x) == 0).sum()
if empty_skills_count > 0:
    print(f"\nAdvertencia: {empty_skills_count} filas en recursos_humanos.csv no pudieron convertir 'Habilidades técnicas' a diccionario.")

# Eliminar la columna original de string si ya no se necesita
# resources_df = resources_df.drop('Habilidades técnicas', axis=1) # Descomentar si se quiere eliminar

print("\nRecursos Humanos con Habilidades Parseadas:")
print(resources_df[['ID', 'Habilidades_dict']].head())


# --- Simulación de Asignaciones y Creación de Dataset de Entrenamiento ---

# Como no tenemos datos históricos de éxito, vamos a simular asignaciones
# y crear un dataset combinado.

# Crearemos pares (recurso, tarea) aleatorios. En un caso real, tendrías estos datos.
np.random.seed(42) # Para reproducibilidad
num_simulated_assignments = 500 # Puedes ajustar este número

simulated_data = []

for _ in range(num_simulated_assignments):
    # Elegir un recurso y una tarea al azar
    resource_row = resources_df.sample(1).iloc[0]
    task_row = tasks_df.sample(1).iloc[0]

    resource_id = resource_row['ID']
    task_description = task_row['Task Description']
    required_skill = task_row['Skill']
    resource_skills = resource_row['Habilidades_dict']

    # Calcular la característica clave: Nivel de Coincidencia de Habilidad
    # Si el recurso tiene la habilidad, usamos su nivel; si no, 0.
    skill_match_score = resource_skills.get(required_skill, 0.0)

    # Características del recurso
    experience = resource_row['Experiencia (años)']
    performance = resource_row['Rendimiento personal']
    soft_skills = resource_row['Soft skills']
    workload = resource_row['Carga de trabajo']

    # **Generación del Objetivo Sintético (¡ESTO ES SIMULADO!)**
    # Crearemos una regla simple: éxito más probable si la habilidad es buena (>5)
    # y el rendimiento es bueno (>5). Puedes hacer esto más complejo.
    # También añadimos algo de ruido para que no sea determinista.
    prob_success_simulated = 0.1 # Base
    if skill_match_score > 5: prob_success_simulated += 0.4
    if performance > 5: prob_success_simulated += 0.3
    if experience > 5: prob_success_simulated += 0.1
    if workload < 3: prob_success_simulated += 0.1 # Menor carga ayuda
    
    # Añadir ruido aleatorio y asegurar que esté entre 0 y 1
    prob_success_simulated += np.random.normal(0, 0.1) 
    prob_success_simulated = np.clip(prob_success_simulated, 0.05, 0.95) 

    # Generar éxito binario basado en esta probabilidad simulada
    success_label = 1 if np.random.rand() < prob_success_simulated else 0


    simulated_data.append({
        'Resource_ID': resource_id,
        'Task_Description': task_description,
        'Required_Skill': required_skill,
        'Skill_Match_Score': skill_match_score,
        'Experiencia': experience,
        'Rendimiento': performance,
        'Soft_Skills': soft_skills,
        'Carga_Trabajo': workload,
        'Success': success_label # ¡Objetivo simulado!
    })

training_df = pd.DataFrame(simulated_data)

print("\nDataset de Entrenamiento Simulado (primeras filas):")
print(training_df.head())
print(f"\nDistribución del Éxito Simulado:\n{training_df['Success'].value_counts(normalize=True)}")


# --- Preparación para el Modelo ---

# Seleccionar características (features) y objetivo (target)
features = ['Skill_Match_Score', 'Experiencia', 'Rendimiento', 'Soft_Skills', 'Carga_Trabajo']
target = 'Success'

X = training_df[features]
y = training_df[target]

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

# Escalar las características numéricas (importante para Regresión Logística)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test) # Usar el mismo scaler ajustado en el train set


# --- Entrenamiento del Modelo ---

# Usaremos Regresión Logística porque queremos probabilidades
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)


# --- Evaluación del Modelo ---

# Predicciones en el conjunto de prueba
y_pred = model.predict(X_test_scaled)
y_pred_proba = model.predict_proba(X_test_scaled)[:, 1] # Probabilidad de la clase 1 (Éxito)

print("\n--- Evaluación del Modelo (con datos simulados) ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"AUC Score: {roc_auc_score(y_test, y_pred_proba):.4f}") # AUC es bueno para clases desbalanceadas y evalúa probabilidades
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Ver la importancia de las características (coeficientes del modelo)
# Sólo como indicativo, ya que los datos son simulados
coef_df = pd.DataFrame(model.coef_[0], index=features, columns=['Coefficient'])
print("\nImportancia de Características (Coeficientes de Regresión Logística):")
print(coef_df.sort_values('Coefficient', ascending=False))


# --- Función de Predicción ---

def predict_task_success_probability(resource_id, task_description, model, scaler, resources_df, tasks_df):
    """
    Predice la probabilidad de éxito para una asignación específica.

    Args:
        resource_id: ID del recurso humano.
        task_description: Descripción de la tarea.
        model: El modelo de clasificación entrenado.
        scaler: El objeto StandardScaler ajustado.
        resources_df: DataFrame con la información de los recursos (con Habilidades_dict).
        tasks_df: DataFrame con la información de las tareas.

    Returns:
        float: La probabilidad estimada de éxito (entre 0 y 1), o None si no se encuentra el recurso o la tarea.
    """
    # Buscar la información del recurso
    resource_info = resources_df[resources_df['ID'] == resource_id]
    if resource_info.empty:
        print(f"Error: Recurso con ID {resource_id} no encontrado.")
        return None
    resource_info = resource_info.iloc[0]

    # Buscar la información de la tarea
    task_info = tasks_df[tasks_df['Task Description'] == task_description]
    if task_info.empty:
        # Intentar encontrar una tarea similar si la descripción exacta no está
        # (Podrías implementar lógica de búsqueda más avanzada aquí si es necesario)
        print(f"Advertencia: Tarea con descripción exacta '{task_description}' no encontrada. Buscando primera tarea con esa descripción general...")
        task_info = tasks_df[tasks_df['Task Description'].str.contains(task_description, case=False, na=False)]
        if task_info.empty:
            print(f"Error: Tarea relacionada con '{task_description}' no encontrada.")
            return None
        task_info = task_info.iloc[0] # Tomar la primera coincidencia
        print(f"Usando tarea encontrada: '{task_info['Task Description']}' con habilidad '{task_info['Skill']}'")


    required_skill = task_info['Skill']
    resource_skills = resource_info['Habilidades_dict']

    # Calcular características para la predicción
    skill_match_score = resource_skills.get(required_skill, 0.0)
    experience = resource_info['Experiencia (años)']
    performance = resource_info['Rendimiento personal']
    soft_skills = resource_info['Soft skills']
    workload = resource_info['Carga de trabajo']

    # Crear el vector de características como DataFrame para mantener el orden y nombres
    feature_vector = pd.DataFrame([[
        skill_match_score, experience, performance, soft_skills, workload
    ]], columns=features)

    # Escalar las características usando el scaler ajustado
    feature_vector_scaled = scaler.transform(feature_vector)

    # Predecir la probabilidad de éxito (clase 1)
    probability_success = model.predict_proba(feature_vector_scaled)[0, 1]

    return probability_success

# --- Ejemplo de Uso de la Función de Predicción ---

print("\n--- Ejemplo de Predicción ---")

# Ejemplo 1: Intentar asignar una tarea de API a recurso 1
resource_example_id = 1
task_example_desc = "Implement user authentication" # Esta descripción existe varias veces, la función tomará la primera

prob = predict_task_success_probability(resource_example_id, task_example_desc, model, scaler, resources_df, tasks_df)

if prob is not None:
    print(f"\nProbabilidad estimada de éxito para Recurso {resource_example_id} en Tarea '{task_example_desc}': {prob:.2%}")

# Ejemplo 2: Intentar asignar una tarea de Django a recurso 2
resource_example_id_2 = 2
task_example_desc_2 = "Manage database operations" # Requiere Django según tu CSV

prob_2 = predict_task_success_probability(resource_example_id_2, task_example_desc_2, model, scaler, resources_df, tasks_df)

if prob_2 is not None:
    print(f"Probabilidad estimada de éxito para Recurso {resource_example_id_2} en Tarea '{task_example_desc_2}': {prob_2:.2%}")

# Ejemplo 3: Tarea con habilidad que el recurso 1 tiene alta puntuación (monitoring)
# Supongamos que existe una tarea así (la añadimos para el ejemplo)
if 'monitoring' not in tasks_df['Skill'].tolist():
     # Añadir temporalmente una tarea que requiera 'monitoring' al DataFrame de tareas
     new_task = pd.DataFrame([{'Task Description': 'Setup system monitoring', 'Category': 'DevOps', 'Skill': 'monitoring'}])
     # Usar pd.concat para añadir la fila
     tasks_df = pd.concat([tasks_df, new_task], ignore_index=True)


task_example_desc_3 = "Setup system monitoring"
prob_3 = predict_task_success_probability(resource_example_id, task_example_desc_3, model, scaler, resources_df, tasks_df)

if prob_3 is not None:
    print(f"Probabilidad estimada de éxito para Recurso {resource_example_id} en Tarea '{task_example_desc_3}': {prob_3:.2%}")
```

**Explicación Detallada:**

1.  **Carga y Preprocesamiento:**
    * Se cargan los dos CSVs en DataFrames de Pandas.
    * La columna `Habilidades técnicas` es crucial. Se usa `ast.literal_eval` para convertir el string que *parece* un diccionario en un diccionario real de Python. Se manejan errores por si alguna fila tiene formato incorrecto.
2.  **Simulación de Asignaciones:**
    * **¡Este es el paso más crítico y artificial!** Como no tenemos datos históricos de `(recurso, tarea, éxito)`, generamos pares aleatorios de `(recurso, tarea)`.
    * Para cada par simulado, extraemos las características del recurso (`Experiencia`, `Rendimiento`, etc.).
    * Calculamos `Skill_Match_Score`: Buscamos la habilidad requerida por la tarea (`Skill` en `task_categories.csv`) dentro del diccionario de habilidades del recurso (`Habilidades_dict`). Si existe, tomamos su valor; si no, asumimos 0.
    * **Generamos `Success` (0 o 1):** Creamos una lógica simple (ajustable) para simular el éxito. Aquí, se basa principalmente en si el `Skill_Match_Score` y el `Rendimiento` superan un umbral, con algo de aleatoriedad añadida. **En un proyecto real, esta columna vendría de tus datos históricos.**
    * Se crea un nuevo DataFrame (`training_df`) con estas asignaciones simuladas y sus características.
3.  **Preparación del Modelo:**
    * Se definen las `features` (las columnas que usará el modelo para predecir) y el `target` (la columna `Success` que queremos predecir).
    * Se dividen los datos simulados en conjuntos de entrenamiento (`X_train`, `y_train`) y prueba (`X_test`, `y_test`) para poder evaluar el modelo en datos que no ha visto durante el entrenamiento. `stratify=y` asegura que la proporción de éxitos/fracasos sea similar en ambos conjuntos.
    * Se aplica `StandardScaler` a las características. Esto es importante para modelos como la Regresión Logística, ya que pone todas las características en una escala similar, evitando que aquellas con valores más grandes dominen el modelo injustamente.
4.  **Entrenamiento:**
    * Se instancia un modelo `LogisticRegression`. Este modelo es bueno para problemas de clasificación binaria y puede proporcionar probabilidades directamente.
    * Se entrena el modelo (`model.fit`) usando los datos de entrenamiento escalados.
5.  **Evaluación:**
    * Se usa el modelo entrenado para hacer predicciones sobre el conjunto de prueba (`X_test_scaled`).
    * Se calculan métricas como `Accuracy` (precisión general), `AUC Score` (muy útil para evaluar qué tan bien el modelo distingue entre clases y maneja probabilidades) y un `classification_report` (que incluye precisión, recall y F1-score por clase).
    * Se muestran los coeficientes del modelo. En Regresión Logística, un coeficiente positivo grande sugiere que un aumento en esa característica aumenta la probabilidad de éxito (clase 1), y viceversa para coeficientes negativos. *Recuerda que esto se basa en datos simulados.*
6.  **Función de Predicción (`predict_task_success_probability`):**
    * Esta es la función que usarías en la práctica.
    * Toma el ID del recurso y la descripción de la tarea como entrada.
    * Busca la información necesaria en los DataFrames originales (`resources_df`, `tasks_df`). Incluye un manejo básico por si la descripción exacta de la tarea no se encuentra.
    * Calcula las mismas características que se usaron para entrenar (incluyendo `Skill_Match_Score`).
    * **Importante:** Escala estas características usando el *mismo* `scaler` que se ajustó con los datos de entrenamiento.
    * Usa `model.predict_proba(feature_vector_scaled)[0, 1]` para obtener la probabilidad de la clase "1" (Éxito).
    * Devuelve esta probabilidad.
7.  **Ejemplos de Uso:** Se muestran cómo llamar a la función `predict_task_success_probability` con diferentes recursos y tareas.

**Próximos Pasos y Mejoras:**

1.  **¡Conseguir Datos Reales de Éxito!** Este es el paso más importante para que el modelo sea verdaderamente predictivo y no solo una simulación basada en reglas. Necesitas un historial de tareas asignadas y si se completaron exitosamente.
2.  **Ingeniería de Características Más Avanzada:**
    * ¿Podría la `Category` de la tarea ser útil (quizás como una característica categórica codificada)?
    * ¿Podría una métrica combinada de "afinidad" recurso-categoría ser útil?
    * ¿Interacciones entre características (ej., experiencia en *esa habilidad específica*)?
3.  **Modelos Más Complejos:** Podrías probar otros modelos como Random Forest, Gradient Boosting (XGBoost, LightGBM), o incluso redes neuronales si tienes muchos datos (reales). Estos modelos pueden capturar relaciones no lineales más complejas.
4.  **Validación Cruzada:** Para una evaluación más robusta, usa validación cruzada (ej., `cross_val_score` de scikit-learn) en lugar de una sola división train/test.
5.  **Ajuste de Hiperparámetros:** Optimiza los parámetros internos del modelo (ej., la regularización en Regresión Logística) usando técnicas como `GridSearchCV` o `RandomizedSearchCV`.
6.  **Manejo de Tareas Nuevas/Recursos Nuevos:** Considera cómo manejar situaciones donde aparece una tarea cuya habilidad requerida no estaba en los datos de entrenamiento, o un recurso nuevo.
7.  **Definición de Éxito:** Refina qué significa "éxito". ¿Es solo completado/no completado? ¿O incluye calidad, tiempo, etc.? Esto afectará cómo etiquetas tus datos históricos.
