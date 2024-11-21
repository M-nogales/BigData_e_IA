# 34. **Verificar si una lista está ordenada**
# Verifica si una lista está ordenada de manera ascendente.

cadena = input("Dime números separados por comas: ")

nums = [int(num) for num in cadena.split(',')]

ordenada = True

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        ordenada = False
        break

# Mostrar el resultado
if ordenada:
    print("La lista está ordenada de manera ascendente.")
else:
    print("La lista NO está ordenada de manera ascendente.")