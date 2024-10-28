#26. **Imprimir pirámide de números con for**  
#    Escribe un programa que imprima una pirámide de números utilizando bucles for.
#todo

altura = int(input("Ingresa la altura de la pirámide: "))

for i in range(1, altura + 1):
    print('x' * (altura - i),end='')
    for j in range(1,i + 1):
        print(j, end=' ')
    
    print()

if altura%2 != 0:
    mitad = altura//2
    cantidad = altura//2
    print(cantidad + 1)
    for i in range(1, altura + 1):

        if i > ((mitad + 1)):
            print('x' * (i - (mitad + 1) ), end='')

        else:
            print('x' * ((mitad + 1) - i), end='')


        for j in range(1,i + 1):

            if i > ((mitad + 1)):
                print((i - j), end=' ')
            else:
                print(j, end=' ')

        print()

# 1 xxxxx
# 2 xxxx
# 3 xxx
# 4 xx 
# 5 x
# 6 
# 7 x
# 8 xx
# 9 xxx
# 10 xxxx
# 11 xxxxx