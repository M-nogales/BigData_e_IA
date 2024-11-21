# 14. **Determinar el mayor de tres números**
# Dado tres números, usa condicionales para determinar cuál es el mayor.

n1 = float(input("Dame el primer número: "))
n2 = float(input("Dame el segundo número: "))
n3 = float(input("Dame el tercer número: "))

# Determinar el mayor de los tres números
if n1 >= n2 and n1 >= n3:
    print(f"{n1} es el número mayor.")
elif n2 >= n1 and n2 >= n3:
    print(f"{n2} es el número mayor.")
else:
    print(f"{n3} es el número mayor.")