# 16. **Calcular la calificación**
# Dado un puntaje entre 0 y 100, imprime la calificación correspondiente usando condicionales.

nota = float(input("Dame una puntuación entre 0 y 100: "))
if 0 <= nota <= 100:
    if nota < 5:
        calificacion = "Suspenso"
    elif 5 <= nota < 7:
        calificacion = "Bien"
    elif 7 <= nota < 9:
        calificacion = "Notable"
    elif 9 <= nota < 10:
        calificacion = "Sobresaliente"
    else:
        calificacion = "Matrícula de Honor"

    print(f"La calificación correspondiente es: {calificacion}.")
else:
    print("El puntaje debe estar entre 0 y 100.")