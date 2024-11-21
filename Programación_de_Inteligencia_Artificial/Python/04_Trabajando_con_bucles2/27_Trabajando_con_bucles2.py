# 27. **Juego de adivinanza**
# Crea un programa donde el usuario debe adivinar un número entre 1 y 100.

import random

num_secret = random.randint(1, 100)

intento = None

print("¡Adivina el número entre 1 y 100!")

while intento != num_secret:
    intento = int(input("Dime un número: "))

    if intento < num_secret:
        print("El número es mayor. Intenta de nuevo.")
    elif intento > num_secret:
        print("El número es menor. Intenta de nuevo.")
    else:
        print("¡Felicidades! Adivinaste el número.")