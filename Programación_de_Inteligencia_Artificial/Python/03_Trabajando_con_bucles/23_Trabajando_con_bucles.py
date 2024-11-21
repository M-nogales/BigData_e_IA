#23. **Números perfectos con for**  
#    Escribe un programa que verifique si un número es perfecto (igual a la suma de sus divisores) utilizando un bucle for.

num = int(input("Dame un número para verificar si es perfecto: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")
