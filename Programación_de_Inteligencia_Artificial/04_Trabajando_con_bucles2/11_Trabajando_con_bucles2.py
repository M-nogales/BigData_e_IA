# 11. **Par o impar**
# Escribe un programa que determine si un número es par o impar.

n = int(input("Dame un número entero: "))

if n % 2 == 0:
    print(f"{n} es un número par.")
else:
    print(f"{n} es un número impar.")