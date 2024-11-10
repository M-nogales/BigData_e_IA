# 32. **Encontrar el número mayor en una lista**
# Encuentra el número más grande en una lista usando un bucle.

cadena = input("Dame números separados por comas: ")

nums = [int(num) for num in cadena.split(',')]

mayor = nums[0]

for n in nums:
    if n > mayor:
        mayor = n

print(f"El número mayor en la lista es: {mayor}")