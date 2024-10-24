#9. **Serie de Fibonacci con for**  
#   Escribe un programa que genere los primeros N números de la serie de Fibonacci utilizando un bucle for.

#! fibonacci de  10 = 55

f = 10
result = [0] * f

if f > 0:
    result[0] = 1  # F(0) = 1
if f > 1:
    result[1] = 1  # F(1) = 1

for n in range(2,f):

    result[n] = result[n-1] + result[n-2]

    print(" n: ", n, 'result: ', result)

else:
    print('result final: ', result)

# recursividad

    def fibonacci_recursivo(n):
        if n<=1:
            return 1
        else:
             return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
        

for n in range(0,f):
    print("iteración del bucle: ",n, "result",fibonacci_recursivo(n))