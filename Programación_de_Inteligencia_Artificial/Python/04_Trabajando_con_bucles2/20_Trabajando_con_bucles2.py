# 20. **Número primo**
# Escribe un programa que determine si un número es primo.

n = int(input("Dame un número entero: "))

if n < 2:
    print(f"{n} no es un número primo.")
else:
    es_primo = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"{n} es un número primo.")
    else:
        print(f"{n} no es un número primo.")