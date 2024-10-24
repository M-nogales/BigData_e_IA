# 6. **Sumar dígitos de un número con while**  
#    Escribe un programa que sume los dígitos de un número utilizando un bucle while.

nums = input("Introduce un número: ")

sum = 0

while nums:
    # Tomamos el último dígito, lo convertimos a entero y lo sumamos
    sum += int(nums[-1])
    # Eliminamos el último dígito del número
    nums = nums[:-1]

print("La suma de los dígitos es:", sum)
