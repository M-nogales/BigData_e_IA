# 18. **Números dentro de un rango**
# Verifica si un número dado está dentro de un rango.

n = float(input("Dame un número: "))

min = 1
max = 100

if min <= n <= max:
    print(f"{n} está dentro del rango de {min} a {max}.")
else:
    print(f"{n} está fuera del rango de {min} a {max}.")
