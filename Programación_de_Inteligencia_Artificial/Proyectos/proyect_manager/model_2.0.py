import pandas as pd
import ast  # Para convertir el string del diccionario de habilidades en un diccionario real
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.preprocessing import StandardScaler
import numpy as np

# --- Carga de Datos ---
try:
    tasks_df = pd.read_csv('task_categories_copy.csv')
    resources_df = pd.read_csv('recursos_humanos_copy.csv')
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

def predict_task_success_probability(resource_id, task_description, model, scaler, resources_df, tasks_df, features):
    """
    Predice la probabilidad de éxito para una asignación específica.

    Args:
        resource_id: ID del recurso humano.
        task_description: Descripción de la tarea (string).
        model: El modelo de clasificación entrenado.
        scaler: El objeto StandardScaler ajustado.
        resources_df: DataFrame con la información de los recursos (con Habilidades_dict).
        tasks_df: DataFrame con la información de las tareas.
        features (list): Lista de nombres de columnas usadas como features.


    Returns:
        float: La probabilidad estimada de éxito (entre 0 y 1), o None si no se encuentra el recurso o la tarea.
    """
    # --- Buscar información del Recurso ---
    resource_info_df = resources_df[resources_df['ID'] == resource_id]
    if resource_info_df.empty:
        print(f"Error: Recurso con ID {resource_id} no encontrado.")
        return None
    # Asegurarse de que tenemos una única fila (Series) para el recurso
    resource_info_row = resource_info_df.iloc[0]
    resource_skills = resource_info_row['Habilidades_dict']
    # Validar que resource_skills sea un diccionario
    if not isinstance(resource_skills, dict):
        print(f"Error: Las habilidades para el recurso ID {resource_id} no son un diccionario válido.")
        return None


    # --- Buscar información de la Tarea ---
    # Primero, intentar búsqueda exacta
    task_info_filtered = tasks_df[tasks_df['Task Description'] == task_description]

    if task_info_filtered.empty:
        # Si no hay exacta, intentar búsqueda parcial (contains)
        print(f"Advertencia: Tarea con descripción exacta '{task_description}' no encontrada. Buscando coincidencias parciales...")
        task_info_filtered = tasks_df[tasks_df['Task Description'].str.contains(task_description, case=False, na=False)]

        if task_info_filtered.empty:
            print(f"Error: Tarea relacionada con '{task_description}' no encontrada ni por coincidencia exacta ni parcial.")
            return None
        else:
             # Si hay coincidencias parciales, usar la primera
             print(f"Usando la primera coincidencia parcial encontrada para '{task_description}'.")

    # --- Asegurar una única fila y extraer la habilidad ---
    # Seleccionar la *primera* fila encontrada (ya sea por match exacto o parcial)
    task_info_row = task_info_filtered.iloc[0] # task_info_row es ahora una Series

    # Extraer la habilidad REQUERIDA de esta fila (debería ser un string)
    required_skill = task_info_row['Skill']

    # Validar que required_skill sea un string
    if not isinstance(required_skill, str):
        print(f"Error: La habilidad extraída para la tarea '{task_description}' no es un string ('{required_skill}').")
        # Podría indicar un problema en task_categories.csv o en la lógica de búsqueda
        return None

    print(f"Info Tarea: Descripción='{task_info_row['Task Description']}', Habilidad Requerida='{required_skill}'")
    print(f"Info Recurso: ID={resource_id}, Habilidades Dict={resource_skills}")


    # --- Calcular características para la predicción ---
    # Usar .get() en el diccionario de habilidades del recurso con la habilidad (string) requerida
    skill_match_score = resource_skills.get(required_skill, 0.0)
    experience = resource_info_row['Experiencia (años)']
    performance = resource_info_row['Rendimiento personal']
    soft_skills = resource_info_row['Soft skills']
    workload = resource_info_row['Carga de trabajo']

    # Crear el vector de características como DataFrame para mantener el orden y nombres
    # Asegúrate que 'features' (la lista de nombres de columnas) se pasa a la función
    feature_vector = pd.DataFrame([[
        skill_match_score, experience, performance, soft_skills, workload
    ]], columns=features) # Usar la lista de features pasada como argumento

    # Escalar las características usando el scaler ajustado
    feature_vector_scaled = scaler.transform(feature_vector)

    # Predecir la probabilidad de éxito (clase 1)
    probability_success = model.predict_proba(feature_vector_scaled)[0, 1]

    return probability_success

# --- Ejemplo de Uso de la Función de Predicción (MODIFICADO para pasar 'features') ---

print("\n--- Ejemplo de Predicción ---")

# Asegúrate de que 'features' esté definida en tu script principal
features = ['Skill_Match_Score', 'Experiencia', 'Rendimiento', 'Soft_Skills', 'Carga_Trabajo'] # Re-definir o asegurarse que existe

# Ejemplo 1: Intentar asignar una tarea de API a recurso 1
resource_example_id = 1
task_example_desc = "Implement user authentication"

# Pasar la lista 'features' a la función
prob = predict_task_success_probability(resource_example_id, task_example_desc, model, scaler, resources_df, tasks_df, features)

if prob is not None:
    print(f"\nProbabilidad estimada de éxito para Recurso {resource_example_id} en Tarea '{task_example_desc}': {prob:.2%}")
else:
    print(f"\nNo se pudo calcular la probabilidad para Recurso {resource_example_id} en Tarea '{task_example_desc}'.")


# Ejemplo 2: Intentar asignar una tarea de Django a recurso 2
resource_example_id_2 = 2
task_example_desc_2 = "Manage database operations" # Requiere Django según tu CSV

prob_2 = predict_task_success_probability(resource_example_id_2, task_example_desc_2, model, scaler, resources_df, tasks_df, features)

if prob_2 is not None:
    print(f"Probabilidad estimada de éxito para Recurso {resource_example_id_2} en Tarea '{task_example_desc_2}': {prob_2:.2%}")
else:
    print(f"No se pudo calcular la probabilidad para Recurso {resource_example_id_2} en Tarea '{task_example_desc_2}'.")


# Ejemplo 3: Tarea con habilidad que el recurso 1 tiene alta puntuación (monitoring)
task_example_desc_3 = "Setup system monitoring" # Asumiendo que esta tarea existe o fue añadida
prob_3 = predict_task_success_probability(resource_example_id, task_example_desc_3, model, scaler, resources_df, tasks_df, features)

if prob_3 is not None:
    print(f"Probabilidad estimada de éxito para Recurso {resource_example_id} en Tarea '{task_example_desc_3}': {prob_3:.2%}")
else:
     print(f"No se pudo calcular la probabilidad para Recurso {resource_example_id} en Tarea '{task_example_desc_3}'.")

# Ejemplo 4: Tarea Inexistente
task_example_desc_4 = "Inventar una tarea nueva ahora mismo"
prob_4 = predict_task_success_probability(resource_example_id, task_example_desc_4, model, scaler, resources_df, tasks_df, features)

if prob_4 is not None:
     print(f"Probabilidad estimada de éxito para Recurso {resource_example_id} en Tarea '{task_example_desc_4}': {prob_4:.2%}")
else:
     print(f"No se pudo calcular la probabilidad para Recurso {resource_example_id} en Tarea '{task_example_desc_4}' (Como era esperado).")