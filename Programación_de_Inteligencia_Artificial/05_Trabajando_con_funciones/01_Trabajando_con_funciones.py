# 01. **Factorial de un número**
# Escribir una función que calcule el factorial de un número dado.

def factorial(num):

    if (num == 0 or num == 1):
        return 1
    
    return num * factorial(num-1)

print('factorial(5): ', factorial(5))