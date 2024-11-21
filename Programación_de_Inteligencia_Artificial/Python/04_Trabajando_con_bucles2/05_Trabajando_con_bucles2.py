# 05. **Suma de los primeros N números**
# Usa un bucle para sumar los primeros N números.

n = int(input("Dame un número entero positivo: "))

suma = 0

for i in range(1, n + 1):
    suma += i

print(f"La suma de los primeros {n} números es: {suma}")