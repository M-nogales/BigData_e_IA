import pandas as pd
import numpy as np
import random

# Parámetros
n = 300
#? notas: soft skills float a partir de valores empresariales customizados

# Carga dataset de tareas
df_tarea = pd.read_csv('Task_categories.csv')

# visualización de distintos valores
categorias = df_tarea["Category"].unique().tolist()
print("Categorías únicas:")
for i, cat in enumerate(categorias, 1):
    print(f"{i}. {cat}")

skills_list = df_tarea["Skill"].unique().tolist()
print("Skills:")
for i, skl in enumerate(skills_list, 1):
    print(f"{i}. {skl}")

# Dataset de recurso humano
def generar_habilidades():
    cantidad = min(10, len(skills_list))
    habilidades_seleccionadas = random.sample(skills_list, cantidad)
    return {hab: round(random.uniform(0, 10), 2) for hab in habilidades_seleccionadas}


recursos = []
for _ in range(n):
    recurso = {
        "ID": random.randint(1000, 9999) + n,
        "Experiencia (años)": random.randint(0, 20),
        "Rendimiento personal": round(random.uniform(0, 10), 2),
        "Soft skills": round(random.uniform(0, 10), 2),
        "Carga de trabajo": round(random.uniform(0, 10), 2),
        "Habilidades técnicas": generar_habilidades()
    }
    recursos.append(recurso)

df_humano = pd.DataFrame(recursos)

df_humano["ID"] = range(1, len(df_humano) + 1)

# Paso 1: Asignar recurso aleatorio a cada tarea
df_tarea["ID recurso asignado"] = df_tarea.apply(lambda _: random.choice(df_humano["ID"].tolist()), axis=1)

# Paso 2: Calcular porcentaje de éxito
def calcular_porcentaje_exito(tarea_row):
    recurso_id = tarea_row["ID recurso asignado"]
    herramientas = tarea_row["Skill"]

    # Obtener info del recurso asignado
    recurso = df_humano[df_humano["ID"] == recurso_id].iloc[0]
    habilidades = recurso["Habilidades técnicas"]

    # Promedio de las skills requeridas (o 0 si no tiene alguna)
    puntaje_habilidades = np.mean([habilidades.get(h, 0) for h in herramientas])

    # Componentes
    rendimiento = recurso["Rendimiento personal"] / 10
    soft_skills = recurso["Soft skills"] / 10
    carga = recurso["Carga de trabajo"] / 10
    habilidades_score = puntaje_habilidades / 10

    # Fórmula de éxito (puedes ajustar pesos)
    exito = 0.4 * habilidades_score + 0.3 * rendimiento + 0.2 * soft_skills + 0.1 * (1 - carga)
    return round(exito * 100, 2)

# Aplicar cálculo de éxito
df_tarea["éxito estimado"] = df_tarea.apply(calcular_porcentaje_exito, axis=1)

# exportar a CSV
df_tarea.to_csv('Tareas.csv', index=False)
df_humano.to_csv('Recursos_humanos.csv', index=False)

# asignación de tareas a recursos humanos

# Muestra
print("=== Recursos Humanos ===")
print(df_humano.head())
print("\n=== Tareas ===")
print(df_tarea.head())

# ENTRENAR MODELO DE MACHINE LEARNING

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np

# Paso 1: Unir tareas con recursos humanos asignados
df_completo = df_tarea.copy()
df_completo = df_completo.merge(df_humano, left_on="ID recurso asignado", right_on="ID", suffixes=("_tarea", "_recurso"))

# Paso 2: Calcular match de habilidad (solo una skill por tarea)
def calcular_match_skill(row):
    skill_requerida = row["Skill"]
    habilidades_recurso = row["Habilidades técnicas"]
    return habilidades_recurso.get(skill_requerida, 0)  # 0 si no tiene esa habilidad

df_completo["match_habilidad"] = df_completo.apply(calcular_match_skill, axis=1)

# Paso 3: Codificar variable categórica "Category"
df_encoded = pd.get_dummies(df_completo["Category"], prefix="Category", drop_first=True)

# Paso 4: Construir X (features) e y (target)
X = pd.concat([
    df_encoded,
    df_completo[[
        # "Nivel de dificultad",                  # Si la tienes
        "Rendimiento personal",
        "Soft skills",
        "Carga de trabajo",
        "match_habilidad"
    ]]
], axis=1)

y = df_completo["éxito estimado"]

# Entrenar modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predicción
y_pred = model.predict(X_test)

# Evaluación
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"✅ MSE: {mse:.2f}")
print(f"✅ RMSE: {rmse:.2f}")
print(f"✅ R² Score: {r2:.2f}")
