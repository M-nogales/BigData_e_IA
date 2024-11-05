# 02. **Número primo**
# Crear una función que determine si un número es primo.

def es_primo(num):
    if num <= 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True

print('es_primo(7): ', es_primo(7))