# 21. **Suma de números pares en un rango**
# Usa un bucle para sumar todos los números pares en un rango dado.

bottom = int(input("Dime el límite inferior del rango: "))
top = int(input("Dime el límite superior del rango: "))

suma_pares = 0

for n in range(bottom, top + 1):
    if n % 2 == 0:
        suma_pares += n

print(f"La suma de los números pares entre {bottom} y {top} es: {suma_pares}.")