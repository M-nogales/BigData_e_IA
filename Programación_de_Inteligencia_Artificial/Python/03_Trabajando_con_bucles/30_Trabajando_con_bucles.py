#30. **Contador de intentos con else en while**  
#    Escribe un programa que intente adivinar un número ingresado por el usuario y use un bucle while. Si no logra adivinar después de 5 intentos, muestra un mensaje en el bloque else.

import random

num = int(input("Dame un número del 1 al 10: "))

intento = 0

# Iniciar el bucle while para adivinar el número
while intento < 5:
    num_random = random.randint(1, 10)

    print(f"Intento #{intento + 1}: Adivino que el número es {num_random}.")
    
    intento += 1
    
    if num_random == num:
        print("¡He adivinado el número!")
        break
else:
    print("No he logrado adivinar tu número en 5 intentos. ¡Inténtalo de nuevo!")
