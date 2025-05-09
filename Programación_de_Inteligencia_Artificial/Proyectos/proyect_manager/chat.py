#! gemini: 
'''
15 RPM	Máximo de 15 solicitudes por minuto (Requests Per Minute).
1,000,000 TPM	Máximo de 1 millón de tokens por minuto (Tokens Per Minute).
1,500 RPD	Máximo de 1,500 solicitudes por día (Requests Per Day).
'''
from dotenv import load_dotenv
from google import genai
import os
import json

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")

client = genai.Client(api_key=GEMINI_KEY)

# Cargar JSON
with open("prompt.json", "r", encoding="utf-8") as f:
    task_json = f.read()

# Categorias unicas de las tareas
categories = [
    "data science",
    "backend",
    "cloud",
    "database",
    "database administration",
    "deployment",
    "devops",
    "documentation",
    "frontend",
    "project management",
    "testing",
    "ui/ux design",
    "ai/ml"
]

prompt = f"""
Generate 5 additional tasks following exactly the same structure and format of the JSON below, including keys and writing style:

{task_json}

Make sure the new tasks use varied and realistic technologies.

Valid unique categories are:

{categories}
"""

# Configuración de generación
generation_config = genai.types.GenerateContentConfig(
    temperature=0.4,
    top_p=0.95,
    top_k=40
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
    config=generation_config
)

print(response.text)

raw_text = response.text

if raw_text.startswith("```json"):
    raw_text = raw_text.replace("```json", "").replace("```", "").strip()

try:
    task_data = json.loads(raw_text)
    with open("generated_tasks.json", "w", encoding="utf-8") as f:
        json.dump(task_data, f, indent=4, ensure_ascii=False)
        print("Archivo guardado correctamente.")
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)