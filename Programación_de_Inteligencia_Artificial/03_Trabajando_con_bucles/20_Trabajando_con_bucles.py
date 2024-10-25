#20. **Comparación de listas con for**  
#    Escribe un programa que compare dos listas y cuente cuántos elementos coinciden utilizando un bucle for.

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

counter = 0

#! evita el doble bucle for
for num in lista1:
    
    if num in lista2:
        counter += 1

print(f"Número de elementos que coinciden: {counter}")
