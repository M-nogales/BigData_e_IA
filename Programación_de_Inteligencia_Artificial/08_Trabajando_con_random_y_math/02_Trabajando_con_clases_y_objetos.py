# 02. **La Ruleta**
# Simular el funcionamiento de la ruleta.
#  La ruleta tiene 36 números (del 1 al 36) y un número especial, el 0 (Gana la banca).
#  Realizar la simulación del giro de la ruleta y mostrar el número resultante.

import random

def girar_ruleta():
    numeros_ruleta = list(range(0, 37))
    
    resultado = random.choice(numeros_ruleta)
    
    return resultado
    


resultado = girar_ruleta()
    
if resultado == 0:
    print("La bola ha caido en el: 0, gana la banca")
else:
    print(f"La bola ha caido en el: {resultado}")