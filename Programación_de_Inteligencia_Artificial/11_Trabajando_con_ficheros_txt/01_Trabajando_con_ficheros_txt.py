#Tomando como base el fichero el_quijote.txt adjunto en la tarea, realizar las siguientesoperaciones;
'''
    1. Contabilizar las palabras que aparecen en el fichero
    2. Indicar cuántas veces aparece la palabra “Capítulo” en el documento.
    Se debe ignorar el formato de escritura (mayúsculas, minúsculas o ambas)
    3. Crear un fichero .txt por capítulo indicado en el documento. (Capitulo_XX.txt)
    4. Contabilizar cuántas veces aparece la palabra Dulcinea, Quijote y Sancho.
    5. Generar un listado con las 10 palabras que más veces aparecen en el documento.
    6. Generar un índice de las palabras que más veces aparece y la primera línea en la que aparece.
    7. Calcular la longitud media de las palabras contenidas en el fichero.
    8. Mostrar las 5 frases más largas del documento.
'''
import re

# 1. Contabilizar las palabras que aparecen en el fichero

def contar_palabras(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        words = content.split()
        return f'El quijote contiene {len(words)} palabras'
    
print(contar_palabras("el_quijote.txt"))

# 2. Indicar cuántas veces aparece la palabra “Capítulo” en el documento.

def contar_palabra(file, word: str):

    pattern = rf"{word.lower()} \d+"

    with open(file, "r", encoding="utf-8") as f:
        
        content = f.read().lower()
        # Contar todas las coincidencias del patrón en el texto
        matches = re.findall(pattern, content)
        return f'se han encontrado {len(matches)} {word}'

print(contar_palabra("el_quijote.txt", "CAPÍTULO"))

# 3. Crear un fichero .txt por capítulo indicado en el documento. (Capitulo_XX.txt)

def crear_ficheros_por_capitulo(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    chapter_num = 1
    actual_pos = 0

    while True:
        # Encontramos el inicio del próximo capítulo
        # var[num:] para obtener array apartir del elemento 25
        # re.IGNORECASE para ignorar mayúsculas y minúsculas
        match = re.search(r"CAPÍTULO \d+", content[actual_pos:], re.IGNORECASE)
        
        if not match:
            # Si no encontramos otro capítulo, salimos del bucle
            break

        # Calculamos el índice de inicio del capítulo actual
        chapter_start = match.start() + actual_pos
        # Buscamos el siguiente capítulo para delimitar el contenido
        next_chapter = re.search(r"CAPÍTULO \d+", content[chapter_start + 1:], re.IGNORECASE)
        if next_chapter:
            # Si encontramos el siguiente capítulo, delimitamos el final del actual
            end = chapter_start + 1 + next_chapter.start()
        else:
            # Si no hay siguiente capítulo, tomamos hasta el final del documento
            end = len(content)

        # Extraemos el contenido del capítulo
        chapter_content = content[chapter_start:end].strip()

        # Comparamos la primera línea del capítulo actual con la primera línea del siguiente
        next_chapter_content = content[end:end+1000] 
        next_chapter_line = next_chapter_content.split("\n")[0].strip()

        # Comparamos las primeras líneas
        first_line_chapter = chapter_content.split("\n")[0].strip()

        if first_line_chapter == next_chapter_line:
            # Si son iguales, es probable que estemos ante un capítulo repetido
            print(f"Capítulo {chapter_num} repetido, omitido.")
            chapter_num -= 1
        else:
            # Guardamos el capítulo en un archivo nuevo
            with open(f"resultados/Capitulo_{chapter_num}.txt", "w", encoding="utf-8") as chapter:
                chapter.write(chapter_content)

        # Actualizamos la posición y el número de capítulo
        actual_pos = end
        chapter_num += 1

    return f'Se han creado {chapter_num - 1} ficheros'

print(crear_ficheros_por_capitulo("el_quijote.txt"))

# 4. Contabilizar cuántas veces aparece la palabra Dulcinea, Quijote y Sancho.

def contar_palabras(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read().lower()
        dulcinea = len(re.findall(r"dulcinea", content))
        quijote = len(re.findall(r"quijote", content))
        sancho = len(re.findall(r"sancho", content))
        return f'Dulcinea: {dulcinea}, Quijote: {quijote}, Sancho: {sancho}'

print(contar_palabras("el_quijote.txt"))

# 5. Generar un listado con las 10 palabras que más veces aparecen en el documento.

def obtener_top_10_palabras(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Convertir todo el texto a minúsculas para que la comparación de palabras no sea sensible a mayúsculas/minúsculas
    content = content.lower()

    # Eliminar caracteres no alfabéticos (como puntuaciones y saltos de línea)
    # Utilizamos una expresión regular para conservar solo letras y espacios
    content = re.sub(r'[^a-záéíóúüñ\s]', '', content)

    # Dividir el texto en palabras
    words = content.split()

    # Crear un diccionario para contar las ocurrencias de cada palabra
    words_counter = {}
    for word in words:
        if word in words_counter:
            words_counter[word] += 1
        else:
            words_counter[word] = 1

    # Ordenar el diccionario por el valor (número de ocurrencias) de mayor a menor
    ordered_words = sorted(words_counter.items(), key=lambda x: x[1], reverse=True)
    # Tomar las 10 palabras más comunes
    top_10 = ordered_words[:10]

    # Imprimir las 10 palabras más frecuentes
    for word, num in top_10:
        print(f"{word}: {num}")

    return top_10

print(obtener_top_10_palabras("el_quijote.txt"))

# 6. Generar un índice de las palabras que más veces aparece y la primera línea en la que aparece.

def obtener_indice(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Convertir todo el texto a minúsculas para que la comparación de palabras no sea sensible a mayúsculas/minúsculas
    content = content.lower()

    # Eliminar caracteres no alfabéticos (como puntuaciones y saltos de línea)
    # Utilizamos una expresión regular para conservar solo letras y espacios
    content = re.sub(r'[^a-záéíóúüñ\s]', '', content)

    # Dividir el texto en palabras
    palabras = content.split()

    # Crear un diccionario para contar las ocurrencias de cada palabra
    palabra_count = {}
    for palabra in palabras:
        if palabra in palabra_count:
            palabra_count[palabra] += 1
        else:
            palabra_count[palabra] = 1

    # Ordenar el diccionario por el valor (número de ocurrencias) de mayor a menor
    palabras_ordenadas = sorted(palabra_count.items(), key=lambda x: x[1], reverse=True)

    # Tomar las 10 palabras más comunes
    top_10 = palabras_ordenadas[:10]

    # Crear un diccionario para almacenar la primera línea en la que aparece cada palabra
    first_line = {}
    for palabra, _ in top_10:
        # Buscar la primera línea en la que aparece la palabra
        first_line[palabra] = None
        # dividimos el texto en líneas y buscamos la palabra en cada línea
        for i, line in enumerate(content.split("\n")):
            if palabra in line.split():
                first_line[palabra] = i + 1
                break

    # Imprimir el índice
    for palabra, count in top_10:
        print(f"{palabra}: {count} (Primera línea: {first_line[palabra]})")

    return top_10, first_line

obtener_indice("el_quijote.txt")

# 7. Calcular la longitud media de las palabras contenidas en el fichero.

def longitud_media_palabras(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Convertir todo el texto a minúsculas para que la comparación de palabras no sea sensible a mayúsculas/minúsculas
    content = content.lower()

    # Eliminar caracteres no alfabéticos (como puntuaciones y saltos de línea)
    # Utilizamos una expresión regular para conservar solo letras y espacios
    content = re.sub(r'[^a-záéíóúüñ\s]', '', content)

    # Dividir el texto en palabras
    words = content.split()

    # Calcular la longitud total de todas las palabras
    total_length = sum(len(word) for word in words)

    # Calcular la longitud media
    media = total_length / len(words)

    return media

print(longitud_media_palabras("el_quijote.txt"))

# 8. Mostrar las 5 frases más largas del documento.
#! entendiendo como frase a un conjunto de palabras separadas por un punto, signo de interrogación o exclamación.

def frases_mas_largas(file, n=5):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Dividir el texto en frases
    phrases = re.split(r"[.!?]", content)

    # Eliminar frases vacías
    phrases = [phrase.strip() for phrase in phrases if phrase.strip()]

    # Ordenar las frases por longitud de mayor a menor
    orded_phrases = sorted(phrases, key=len, reverse=True)

    # Tomar las n frases más largas
    long_phrases = orded_phrases[:n]

    # Imprimir las frases
    for i, phrase in enumerate(long_phrases, start=1):
        print(f"{i}. {phrase}")

    return long_phrases

print(frases_mas_largas("el_quijote.txt", n=5))