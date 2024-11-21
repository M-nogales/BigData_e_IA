# 10. **Análisis de Puntuaciones de Juegos**
''' Solicita al usuario las puntuaciones de un jugador en 8 rondas de un juego.
Crea una Serie con las puntuaciones y asigna números de ronda como índice.
Calcula la puntuación máxima, mínima y la diferencia entre la más alta y la más baja.
Muestra las rondas en las que la puntuación es superior a 80.
Ordena las puntuaciones de menor a mayor y muestra el ranking.
 '''

import pandas as pd

while True:
    try:
        scores = [int(input(f'Dame la puntuación de la ronda {i+1}: ')) for i in range(8)]
        break
    except ValueError:
        print('Solo se permiten números enteros')

rounds = ['Round 1', 'Round 2', 'Round 3', 'Round 4', 'Round 5', 'Round 6', 'Round 7', 'Round 8']

scores = pd.Series(scores, index=rounds, dtype='int')
print('Puntuación máxima: ', scores.max())
print('Puntuación mínima: ', scores.min())
print('Diferencia entre la puntuación más alta y la más baja: ', scores.max() - scores.min())
print('Rondas con puntuación superior a 80:\n', scores[scores > 80])
print('Ranking de puntuaciones:\n', scores.sort_values().to_string())