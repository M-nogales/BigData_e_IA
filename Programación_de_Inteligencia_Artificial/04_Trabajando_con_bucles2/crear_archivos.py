# Lista de títulos y descripciones para cada ejercicio
titulos = [
    "Imprimir números del 1 al 10",
    "Números pares del 1 al 100",
    "Imprimir un patrón de estrellas",
    "Imprimir un patrón invertido",
    "Suma de los primeros N números",
    "Factorial de un número",
    "Imprimir tabla de multiplicar",
    "Imprimir los primeros N números impares",
    "Serie de Fibonacci",
    "Contar dígitos de un número",
    "Par o impar",
    "Positivo, negativo o cero",
    "Comparación de dos números",
    "Determinar el mayor de tres números",
    "Año bisiesto",
    "Calcular la calificación",
    "Verificar si un carácter es una vocal",
    "Números dentro de un rango",
    "Calculadora simple",
    "Número primo",
    "Suma de números pares en un rango",
    "Imprimir números divisibles por 3 y 5",
    "Contar números positivos, negativos y ceros",
    "Sumar solo los números positivos",
    "Contar vocales y consonantes",
    "Imprimir los primeros N números primos",
    "Juego de adivinanza",
    "Calculadora de promedio",
    "Invertir una cadena",
    "Suma de dígitos",
    "Palíndromo",
    "Encontrar el número mayor en una lista",
    "Contar números primos en un rango",
    "Verificar si una lista está ordenada",
    "Números perfectos",
    "Juego del 'FizzBuzz'",
    "Generar números aleatorios hasta que sea cero",
    "Determinar el segundo número más grande en una lista",
    "Pares e impares separados",
    "Convertir números decimales a binarios"
]

descripciones = [
    "Utiliza un bucle for para imprimir los números del 1 al 10.",
    "Usa un bucle for para imprimir solo los números pares entre 1 y 100.",
    "Crea un bucle que imprima un patrón de estrellas.",
    "Crea un bucle que imprima un patrón invertido de estrellas.",
    "Usa un bucle para sumar los primeros N números.",
    "Escribe un programa que calcule el factorial de un número.",
    "Solicita un número al usuario y genera su tabla de multiplicar del 1 al 10.",
    "Escribe un programa que imprima los primeros N números impares utilizando un bucle while.",
    "Escribe un programa que imprima los primeros N términos de la serie de Fibonacci.",
    "Usa un bucle while para contar cuántos dígitos tiene un número.",
    "Escribe un programa que determine si un número es par o impar.",
    "Usa condicionales para verificar si un número es positivo, negativo o cero.",
    "Escribe un programa que compare dos números e imprima el mayor.",
    "Dado tres números, usa condicionales para determinar cuál es el mayor.",
    "Escribe un programa que determine si un año es bisiesto.",
    "Dado un puntaje entre 0 y 100, imprime la calificación correspondiente usando condicionales.",
    "Escribe un programa que verifique si un carácter ingresado es una vocal.",
    "Verifica si un número dado está dentro de un rango.",
    "Solicita dos números y una operación al usuario y realiza la operación.",
    "Escribe un programa que determine si un número es primo.",
    "Usa un bucle para sumar todos los números pares en un rango dado.",
    "Imprime los números entre 1 y 100 que sean divisibles por 3 y 5.",
    "Cuenta cuántos números son positivos, negativos o ceros en un conjunto ingresado.",
    "Usa un bucle para sumar solo los números positivos en una lista.",
    "Cuenta cuántas vocales y cuántas consonantes contiene una cadena de texto.",
    "Usa bucles y condicionales para imprimir los primeros N números primos.",
    "Crea un programa donde el usuario debe adivinar un número entre 1 y 100.",
    "Solicita números hasta que el usuario ingrese un cero y calcula el promedio.",
    "Escribe un programa que invierta una cadena ingresada por el usuario.",
    "Usa un bucle while para sumar todos los dígitos de un número.",
    "Determina si una palabra es un palíndromo.",
    "Encuentra el número más grande en una lista usando un bucle.",
    "Cuenta cuántos números son primos en un rango dado.",
    "Verifica si una lista está ordenada de manera ascendente.",
    "Encuentra todos los números perfectos entre 1 y 1000.",
    "Imprime los números del 1 al 100 con 'Fizz', 'Buzz', o 'FizzBuzz'.",
    "Genera números aleatorios entre 1 y 10 hasta que se genere un cero.",
    "Encuentra el segundo número más grande en una lista.",
    "Separa los números pares e impares en dos listas diferentes.",
    "Convierte un número decimal a binario usando un bucle."
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
