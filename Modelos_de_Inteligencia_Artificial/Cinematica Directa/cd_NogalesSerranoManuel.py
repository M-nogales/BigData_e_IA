import numpy as np

def dh_matrix(theta, d, a, alpha):
    """
    Calcula la matriz de transformación homogénea utilizando los parámetros DH.
    """
    theta = np.radians(theta)
    alpha = np.radians(alpha)
    
    return np.array([
        [np.cos(theta), -np.sin(theta) * np.cos(alpha), np.sin(theta) * np.sin(alpha), a * np.cos(theta)],
        [np.sin(theta), np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a * np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

def forward_kinematics(theta1, theta2, l1, l2):
    """
    Calcula la posición final del efector final del brazo de 2DOF.
    """
    A1 = dh_matrix(theta1, 0, l1, 0)
    A2 = dh_matrix(theta2, 0, l2, 0)
    
    T = np.dot(A1, A2)  # Transformación total
    x, y = T[0, 3], T[1, 3]  # Posición del efector final
    return x, y

# Parámetros del brazo robótico
l1 = 5  # Longitud del primer eslabón
l2 = 3  # Longitud del segundo eslabón

# Ejemplos de configuración angular y posiciones resultantes
configurations = [(0, 0), (45, 30), (90, -45), (180, 90)]

for theta1, theta2 in configurations:
    x, y = forward_kinematics(theta1, theta2, l1, l2)
    print(f"Theta1: {theta1}°, Theta2: {theta2}° → Posición: (x={x:.2f}, y={y:.2f})")
