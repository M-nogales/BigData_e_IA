#16. **Tablas de multiplicar con for**  
#    Escribe un programa que imprima la tabla de multiplicar del 1 al 10 utilizando un bucle for.

for i in range(1, 11):
    print(f"\nTabla del {i}:")
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
