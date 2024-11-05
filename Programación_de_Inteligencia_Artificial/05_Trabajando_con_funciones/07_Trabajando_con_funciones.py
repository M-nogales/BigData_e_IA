# 07. **Máximo Común Divisor (MCD)**
# Escribir una función que encuentre el MCD de dos números usando el algoritmo de Euclides.

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print('mcd(24, 36): ', mcd(24, 36)) # 12