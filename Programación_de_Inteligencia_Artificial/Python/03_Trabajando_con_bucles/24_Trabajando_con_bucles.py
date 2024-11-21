#24. **Número mayor y menor con for**  
#    Escribe un programa que encuentre el número mayor y el menor de una lista utilizando un bucle for.

nums = [23, 5, 12, 89, 44, 7, 15]

mayor = nums[0]
menor = nums[0]

for num in nums:

    if num > mayor:
        mayor = num

    if num < menor:
        menor = num

print(f"El número mayor en la lista es: {mayor}")
print(f"El número menor en la lista es: {menor}")
