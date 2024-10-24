# 7. **Adivinar el número con while**  
#    Crea un juego en el que el usuario intente adivinar un número secreto. El programa deberá seguir solicitando al usuario que adivine hasta que lo haga correctamente.

import random

key = random.randint(1, 10)

print("Bienvenido al juego de adivinar el número!")
print("He elegido un número entre 1 y 10.")
print("Intenta adivinarlo.")

intentos = 0

while True:
    num = int(input("¿cual crees que es el número?"))
    
    intentos += 1
    
    if num < key:
        print("Demasiado bajo. Intenta de nuevo.")
    elif num > key:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        # Si la adivinanza es correcta
        print(f"¡Felicidades! Adivinaste el número secreto {key} en {intentos} intentos.")
        break