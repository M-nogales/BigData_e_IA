# 37. **Generar números aleatorios hasta que sea cero**
# Genera números aleatorios entre 1 y 10 hasta que se genere un cero.

import random

num = random.randint(0, 10)
counter = 0
while num != 0:
    print(num)
    counter += 1
    num = random.randint(0, 10)

print("Se ha tardado:",counter," comprobaciones")