# 24. **Sumar solo los números positivos**
# Usa un bucle para sumar solo los números positivos en una lista.

nums = input("Dame una lista de números separados por espacios: ").split()

suma_positivos = 0

for num in nums:
    try:
        num = float(num)
        if num > 0:
            suma_positivos += num
    except ValueError:
        print(f"'{num}' no es un número válido y se omitirá.")

# Imprimir el resultado
print(f"La suma de los números positivos es: {suma_positivos}")