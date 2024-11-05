# 04. **Número de la Ruleta**
# La computadora debe girar la ruleta y el jugador debe adivinar el número.
#  El programa debe indicar si el usuario ha acertado o no con el número.

import random

def juego_ruleta():
    numeros_ruleta = list(range(0, 37))
    
    return random.choice(numeros_ruleta)
    

apuesta = int(input("Adivina el número de la ruleta! (0-36): "))

resultado = juego_ruleta()

print(f"El número girado es: {resultado}")

if apuesta == resultado:
    print("¡Felicidades! Has acertado el número.")
else:
    print("Lo siento, no has acertado. Intenta de nuevo.")
