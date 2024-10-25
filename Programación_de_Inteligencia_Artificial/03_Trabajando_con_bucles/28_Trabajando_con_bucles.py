#28. **Dibujar un cuadrado con for**  
#    Escribe un programa que dibuje un cuadrado de asteriscos de tamaño N utilizando bucles for.

# Solicitamos al usuario que ingrese el tamaño del cuadrado
tamaño = int(input("Dame el tamaño del cuadrado: "))

for i in range(tamaño):
    for j in range(tamaño):
        print('*', end=' ')
    print()
