#2 Factorial
# Escribe un programa que calcule el factorial de un número dado utilizando un bucle while.
# !5 = 120
num = 5
n = 0
while n<=num:
    print("num",num)
    print("n",n)
    if n == 0 or n == 1:
        result = 1
    else:
        result = n * result
        print(result)
    
    n += 1