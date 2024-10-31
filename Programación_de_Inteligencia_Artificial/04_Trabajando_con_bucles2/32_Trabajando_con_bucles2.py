# 32. **Encontrar el número mayor en una lista**
# Encuentra el número más grande en una lista usando un bucle.

cadena = input("Dame números separados por comas: ")

nums = [int(num) for num in cadena.split(',')]

# Inicializar la variable para el número mayor
mayor = nums[0]  # Suponemos que el primer número es el mayor inicialmente

# Bucle para encontrar el número mayor
for n in nums:
    if n > mayor:
        mayor = n  # Actualizar el mayor si se encuentra uno más grande

# Mostrar el número mayor encontrado
print(f"El número mayor en la lista es: {mayor}")