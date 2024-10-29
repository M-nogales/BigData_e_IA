#26. **Imprimir pirámide de números con for**  
#    Escribe un programa que imprima una pirámide de números utilizando bucles for.

altura = int(input("Dame la altura de la pirámide: "))

for i in range(1, altura + 1):
    print(' ' * (altura - i),end='')
    for j in range(1,i + 1):
        print(j, end=' ')
    
    print()

if altura % 2 != 0:
    mitad = altura // 2  # Calculamos la mitad de la altura

    for i in range(1, altura + 1):
        
        espacios = abs(mitad - i)  # Cantidad de espacios para centrar el rombo

        if i < mitad + 1:
        # Imprimir los espacios para centrar el rombo
            print(' ' * (espacios+2), end='')
        else:
            print(' ' * espacios, end='')

        # Imprimir los números
        if i <= mitad + 1:  # Parte superior del rombo (incluyendo la línea central)
            for j in range(1, i + 1):
                print(j, end=' ')
        else:
            for j in range(1, altura - i + 2):
                print(j, end=' ')

        print()
else:
    print("introduce un número impar para ver el rombo")
