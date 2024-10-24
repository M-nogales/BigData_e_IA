#27. **Simular lanzamiento de monedas con while**  
#    Escribe un programa que simule el lanzamiento de una moneda hasta que salga cara tres veces consecutivas utilizando un bucle while.
import random
c=0
n=0
while c<3:
    n += 1
    if random.randint(1,2) == 1:
        c += 1
        print(":)")
    else:
        print("+")
        c = 0

print("numero de bucles realizados: ",n)