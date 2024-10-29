# 19. **Calculadora simple**
# Solicita dos números y una operación al usuario y realiza la operación.

n1 = float(input("Dame el primer número: "))
n2 = float(input("Dame el segundo número: "))

operacion = input("Dime el tipo de operación deseada (+, -, *, /, //): ")


if operacion == '+':
    result = n1 + n2
    print(f"{n1} + {n2} = {result}")
elif operacion == '-':
    result = n1 - n2
    print(f"{n1} - {n2} = {result}")
elif operacion == '*':
    result = n1 * n2
    print(f"{n1} * {n2} = {result}")
elif operacion == '/':
    if n2 != 0:
        result = n1 / n2
        print(f"{n1} / {n2} = {result}")
    else:
        print("Error: No se puede dividir por cero.")
elif operacion == '//':
    if n2 != 0:
        result = n1 // n2
        print(f"{n1} // {n2} = {result}")
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("elige entre +, -, *, /.")