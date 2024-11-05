# 03. **Suma de dígitos de un número**
# Escribir una función que sume los dígitos de un número entero positivo.

def digits_sum(num):
    while nums:
        # Tomamos el último dígito, lo convertimos a entero y lo sumamos
        sum += int(nums[-1])
        # Eliminamos el último dígito del número
        nums = nums[:-1]
    return sum

print('digits_sum(1234): ', digits_sum(1234))