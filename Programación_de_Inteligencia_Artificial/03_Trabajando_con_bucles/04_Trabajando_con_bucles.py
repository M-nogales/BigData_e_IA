# 4. **Buscar en lista con else en un for**  
#    Escribe un programa que busque un número en una lista utilizando un bucle for, y si no lo encuentra, muestra un mensaje en el bloque else.

# Lista de números
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Pedimos al usuario que introduzca el número a buscar
search = int(input("Introduce un número a buscar en la lista: "))

# Usamos un bucle for para buscar el número en la lista
for n in nums:
    if n == search:  # Si encontramos el número
        print(f"{search} se encuentra en la lista.")
        break
else:
    print(f"{search} no se encuentra en la lista.")
