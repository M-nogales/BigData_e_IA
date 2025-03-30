import numpy as np
import random

def inverse_kinematics(x, y, l1, l2):
    """
    Calcula los ángulos de las articulaciones de un brazo robótico de 2 DOF
    utilizando cinemática inversa.
    """
    d = np.sqrt(x**2 + y**2)  # Distancia al objetivo
    
    # Verificación de si el objetivo es alcanzable
    if d > (l1 + l2):
        raise ValueError("Posición fuera del alcance del brazo")
    
    # Ley del coseno para calcular theta2
    cos_theta2 = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    theta2 = np.arccos(np.clip(cos_theta2, -1, 1))  # Clipping para evitar errores numéricos
    
    # Ley del coseno para calcular theta1
    k1 = l1 + l2 * np.cos(theta2)
    k2 = l2 * np.sin(theta2)
    theta1 = np.arctan2(y, x) - np.arctan2(k2, k1)
    
    return np.degrees(theta1), np.degrees(theta2)

# Parámetros del brazo robótico
l1, l2 = 5, 3  # Longitudes de los eslabones

# Generar 10 posiciones aleatorias dentro del área alcanzable del brazo
random.seed(42)
positions = [(random.uniform(-8, 8), random.uniform(-8, 8)) for _ in range(10)]

# Calcular los ángulos para cada posición
results = []
for x, y in positions:
    try:
        theta1, theta2 = inverse_kinematics(x, y, l1, l2)
        results.append((x, y, theta1, theta2))
    except ValueError:
        results.append((x, y, "Fuera de alcance", "Fuera de alcance"))

# Imprimir resultados en formato tabla
print("\nPosición (x, y) | Theta1 (°) | Theta2 (°)")
print("-" * 40)
for x, y, t1, t2 in results:
    print(f"({x:.2f}, {y:.2f}) | {t1} | {t2}")
