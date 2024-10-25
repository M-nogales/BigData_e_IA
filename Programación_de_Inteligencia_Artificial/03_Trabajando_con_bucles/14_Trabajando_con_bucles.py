#14. **Buscar máximo en una lista con for**  
#    Escribe un programa que busque el número más grande en una lista utilizando un bucle for.

nums = [3, 15, 7, 23, 42, 8, 16]

max = nums[0]

for num in nums:
    if num > max:
        max = num

print(f"El número más grande en la lista es: {max}")
