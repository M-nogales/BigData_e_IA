# 03. **Baraja de Cartas**
# Realizar la simulación de la mezcla de una baraja de cartas estándar (52 cartas)
# y realizar el reparto de 5 cartas al azar. 
# Palos: Corazones, Diamantes, Tréboles, Picas. 
# Valores: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A.

import random

def mezclar_y_repartir_cartas():
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    baraja = [f"{valor} de {palo}" for palo in palos for valor in valores]
    
    random.shuffle(baraja)
    
    cartas_repartidas = random.sample(baraja, 5)
    
    return cartas_repartidas

mezcla = mezclar_y_repartir_cartas()

print("Cartas repartidas:")
for carta in mezcla:
    print(carta)