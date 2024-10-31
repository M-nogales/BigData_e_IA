# 30. **Suma de dígitos**
# Usa un bucle while para sumar todos los dígitos de un número.

num = input("Dame un número para sumar sus dígitos: ")

sum = 0
i = 0

while i < len(num):
    sum += int(num[i])
    i += 1

print(f"La suma de los dígitos es: {sum}")