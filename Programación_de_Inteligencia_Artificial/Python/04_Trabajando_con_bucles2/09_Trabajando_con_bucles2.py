# 09. **Serie de Fibonacci**
# Escribe un programa que imprima los primeros N términos de la serie de Fibonacci.

n = int(input("Dime cuántos términos de la serie de Fibonacci deseas imprimir: "))

a = 0
b = 1

print("Serie de Fibonacci:")
print(a)
if n > 1:
    print(b)


for i in range(2, n+1):
    c = a + b 
    print(c)
    a = b
    b = c