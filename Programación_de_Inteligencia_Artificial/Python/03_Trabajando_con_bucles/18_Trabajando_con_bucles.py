#18. **Calcular promedio con for**  
#    Escribe un programa que calcule el promedio de una lista de números utilizando un bucle for.

nums = [10, 20, 30, 40, 50]

sum = 0

for num in nums:
    sum += num

result = sum / len(nums)

print(f"El promedio de la lista es: {result}")
