# 01. **Tirada de Dados**
# Simular el lanzamiento de dos dados de seis caras 
# y mostrar el resultado de cada dado y la suma total.

import random

def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma_total = dado1 + dado2
    
    return dado1, dado2, suma_total

dado1,dado2,suma_total = tirar_dados()

print(f"Primer dado: {dado1}")
print(f"Segundo dado: {dado2}")
print(f"Suma total: {suma_total}")