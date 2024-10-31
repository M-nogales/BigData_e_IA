# 28. **Calculadora de promedio**
# Solicita números hasta que el usuario ingrese un cero y calcula el promedio.

sum = 0
counter = 0

print("Dame números para calcular el promedio. Escribe 0 para terminar.")

while True:
    num = float(input("Dame un número: "))
    
    if num == 0:
        break

    sum += num
    counter += 1

if counter > 0:
    promedio = sum / counter
    print(f"El promedio es: {promedio}")
else:
    print("No has puesto ningún dato.")