# 39. **Pares e impares separados**
# Separa los números pares e impares en dos listas diferentes.


def separar_pares_impares(lista):
    pares = []
    impares = []

    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    return pares, impares

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar_pares_impares(nums)

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")