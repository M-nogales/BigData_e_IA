# 26. **Imprimir los primeros N números primos**
# Usa bucles y condicionales para imprimir los primeros N números primos.

N = int(input("Dime la cantidad de números primos que deseas ver: "))

contador_primos = 0
num = 2


def es_primo(num):
    if num <= 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True

if es_primo(num):
    print(f"{num} es primo.")
else:
    print(f"{num} no es primo.")