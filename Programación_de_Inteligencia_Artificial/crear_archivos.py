# Lista de títulos y descripciones para cada ejercicio
titulos = [

]

descripciones = [
]

# Crear archivos con el formato requerido
for i in range(40):
    numero = f'{i + 1:02}'  # Formato de número de dos dígitos
    titulo = titulos[i]
    descripcion = descripciones[i]
    
    # Formato del contenido del archivo
    contenido = f"# {numero}. **{titulo}**\n# {descripcion}\n"
    
    # Nombre del archivo
    nombre_archivo = f"{numero}_Trabajando_con_bucles2.py"
    
    # Crear el archivo y escribir el contenido
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)

print("Archivos creados con éxito.")
