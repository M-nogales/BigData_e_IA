#21. **Suma condicional de números con while**  
#    Escribe un programa que sume números ingresados por el usuario hasta que ingrese un número negativo utilizando un bucle while.

sum = 0

while True:
    
    num = int(input("Dame un número (Un número negativo temina el programa): "))
    
    if num < 0:
        break

    sum += num

print(f"La suma total de los números dados es: {sum}")
