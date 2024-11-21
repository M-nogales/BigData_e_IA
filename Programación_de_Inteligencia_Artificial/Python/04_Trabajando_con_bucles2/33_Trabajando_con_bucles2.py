# 33. **Contar números primos en un rango**
# Cuenta cuántos números son primos en un rango dado.

def es_primo(num):
    if num <= 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True

min = int(input("Dame valor minimo del rango: "))
max = int(input("Dame el valor máximo del rango: "))

contador_primos = 0

for numero in range(min, max + 1):
    if es_primo(numero):
        contador_primos += 1

print(f"La cantidad de números primos en el rango de {min} a {max} es: {contador_primos}")