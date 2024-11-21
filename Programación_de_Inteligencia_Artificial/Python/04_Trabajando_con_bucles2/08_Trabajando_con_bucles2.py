# 08. **Imprimir los primeros N números impares**
# Escribe un programa que imprima los primeros N números impares utilizando un bucle while.

n = int(input("Dime cuántos números impares deseas imprimir: "))

contador = 0
numero_impar = 1

while contador < n:
    print(numero_impar)
    numero_impar += 2
    contador += 1