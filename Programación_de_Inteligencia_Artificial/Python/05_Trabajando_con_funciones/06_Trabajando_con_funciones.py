# 06. **Serie de Fibonacci hasta N términos**
# Crear una función que genere la serie de Fibonacci hasta un número dado de términos.

def fibonacci(n):
    
    a = 0
    b = 1

    if n == 0:return a

    if n <= 1:return b


    for i in range(2, n+1):
        c = a + b 
        a = b
        b = c
    return c


print('fibonacci(10): ', fibonacci(2)) # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55