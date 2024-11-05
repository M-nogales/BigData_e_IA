# 13. **Distancia recorrida en kilómetros según pasos**
# Crear una función que calcule la distancia aproximada recorrida dado un número de pasos, asumiendo una longitud media de paso de 0.78 metros, y convierta los pasos a kilómetros.

def calc_distance(steps):
    one_step_distance = 0.78
    distance_meters = steps * one_step_distance
    distance_kilometers = distance_meters / 1000
    return distance_kilometers

print('calc_distance(10000): ', calc_distance(10000)) # 7.8
