# 22. **Imprimir números divisibles por 3 y 5**
# Imprime los números entre 1 y 100 que sean divisibles por 3 y 5.

print("Números divisibles por 3 y 5 desde el 1 al 100:")
for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print(numero)