# 3. **Números primos con for**  
#    Escribe un programa que determine si un número es primo utilizando un bucle for con una condición if.

num = int(input("Introduce un número: "))

es_primo = True

if num <= 1:
    es_primo = False
else:
    # Iteramos desde 2 hasta la raíz cuadrada del número
    for n in range(2, num):
        if num % n == 0: 
            es_primo = False 
            break 

# Imprimimos el resultado
if es_primo:
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")
