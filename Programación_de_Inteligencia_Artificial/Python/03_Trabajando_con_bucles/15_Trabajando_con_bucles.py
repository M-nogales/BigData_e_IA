#15. **Suma de números en un rango con for**  
#    Escribe un programa que sume todos los números en un rango dado utilizando un bucle for.

start = int(input("Dame el número de inicio del rango: "))
end = int(input("Dame el número final del rango: "))

sum = 0

for numero in range(start, end + 1):
    sum += numero 

print(f"La suma de todos los números de {start} a {end} es: {sum}")
