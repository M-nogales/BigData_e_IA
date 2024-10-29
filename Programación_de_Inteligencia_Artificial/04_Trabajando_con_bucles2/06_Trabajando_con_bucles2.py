# 06. **Factorial de un número**
# Escribe un programa que calcule el factorial de un número.

n = int(input("Dame un número entero no negativo: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"El factorial de {n} es: {factorial}")