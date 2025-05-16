import pandas as pd
import random

# Cargar datasets
rrhh = pd.read_csv('datasets/Extended_Employee_Performance_and_Productivity_Data.csv')
tareas = pd.read_csv('tareas.csv')

# Lista de skills únicas
skills = tareas['Skill'].unique()

# Crear habilidades técnicas por empleado
employee_skills = {}

for emp_id in rrhh['Employee_ID']:
    num_skills = random.randint(1, len(skills))  # Número aleatorio de skills por empleado
    selected_skills = random.sample(list(skills), num_skills)
    skill_scores = {skill: round(random.uniform(0.5, 10.0), 2) for skill in selected_skills}
    employee_skills[emp_id] = skill_scores

# Mostrar resultado
print(employee_skills)

# Cargar datasets
rrhh = pd.read_csv('datasets/Extended_Employee_Performance_and_Productivity_Data.csv')
tareas = pd.read_csv('tareas.csv')

# Lista de skills únicas
skills = tareas['Skill'].unique()

# Crear habilidades técnicas por empleado
employee_skills = {}

for emp_id in rrhh['Employee_ID']:
    num_skills = random.randint(1, len(skills))  # Número aleatorio de skills por empleado
    selected_skills = random.sample(list(skills), num_skills)
    skill_scores = {skill: round(random.uniform(0.5, 10.0), 2) for skill in selected_skills}
    employee_skills[emp_id] = skill_scores

# Añadir columna al DataFrame
rrhh['technical_abilities'] = rrhh['Employee_ID'].map(employee_skills)

# Guardar en nuevo archivo
rrhh.to_csv('datasets/RRHH.csv', index=False)

print("Archivo 'datasets/RRHH.csv' guardado con la nueva columna 'technical_abilities'.")

#--- TEST WITH JSON ---

import pandas as pd
import random
import json

# Cargar datasets
rrhh = pd.read_csv('datasets/Extended_Employee_Performance_and_Productivity_Data.csv')
tareas = pd.read_json('generated_tasks copy.json')

# Lista de skills únicas
skills = tareas['Skill'].unique()

# Crear habilidades técnicas por empleado
employee_skills = {}

for emp_id in rrhh['Employee_ID']:
    num_skills = random.randint(1, len(skills))  # Número aleatorio de skills por empleado
    selected_skills = random.sample(list(skills), num_skills)
    skill_scores = {skill: round(random.uniform(0.5, 10.0), 2) for skill in selected_skills}
    employee_skills[emp_id] = skill_scores

# Añadir columna al DataFrame
rrhh['technical_abilities'] = rrhh['Employee_ID'].map(employee_skills)

# Guardar en nuevo archivo
# rrhh.to_csv('datasets/RRHH.csv', index=False)

print("Archivo 'datasets/RRHH.csv' guardado con la nueva columna 'technical_abilities'.")
