# 05. **BlackJack**
# Simular la versión básica del juego del BlackJack.
# Repartir cartas al azar hasta que el jugador decida plantarse o supere 21.

import random

# Crear la baraja de cartas
def crear_baraja():
    baraja = []
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    for valor in valores:
        for palo in palos:
            baraja.append((valor, palo))
    random.shuffle(baraja)
    return baraja

# Obtener el valor de una carta
def valor_carta(carta):
    valor = carta[0]
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11  # Tratamos el As inicialmente como 11
    else:
        return int(valor)

# Calcular el total de una mano
def calcular_total(mano):
    total = 0
    ases = 0
    for carta in mano:
        total += valor_carta(carta)
        if carta[0] == 'A':
            ases += 1
    # Si el total pasa de 21 y hay un As, cambia el valor de As de 11 a 1
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total


# Jugar
print("¡Bienvenido al juego de BlackJack!")

baraja = crear_baraja()
mano_jugador = []

# Repartir dos cartas iniciales
mano_jugador.append(baraja.pop())
mano_jugador.append(baraja.pop())

while True:
    total_jugador = calcular_total(mano_jugador)
    print(f"\nTus cartas: {mano_jugador} | Total: {total_jugador}")
    
    if total_jugador > 21:
        print("¡Te has pasado de 21! Has perdido.")
        break
    
    decision = input("¿Quieres pedir otra carta? (s/n): ").lower()
    
    if decision == 's':
        mano_jugador.append(baraja.pop())
    elif decision == 'n':
        print(f"Te plantas con un total de: {total_jugador}")
        break
    else:
        print("Opción no válida. Por favor, elige 's' o 'n'.")
