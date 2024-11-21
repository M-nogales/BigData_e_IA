# 12. **Positivo, negativo o cero**
# Usa condicionales para verificar si un número es positivo, negativo o cero.

n = float(input("Dame un número: "))

if n > 0:
    print(f"{n} es un número positivo.")
elif n < 0:
    print(f"{n} es un número negativo.")
else:
    print("El número es cero.")