# 13. **Comparación de dos números**
# Escribe un programa que compare dos números e imprima el mayor.

n1 = float(input("Dame el primer número: "))
n2 = float(input("Dame el segundo número: "))

if n1 > n2:
    print(f"{n1} es el número mayor.")
elif n2 > n1:
    print(f"{n2} es el número mayor.")
else:
    print("Ambos números son iguales.")