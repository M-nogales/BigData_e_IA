# 07. **Imprimir tabla de multiplicar**
# Solicita un número al usuario y genera su tabla de multiplicar del 1 al 10.

numero = int(input("Dame un número conocer su tabla de multiplicar: "))

print(f"Tabla de multiplicar de {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
