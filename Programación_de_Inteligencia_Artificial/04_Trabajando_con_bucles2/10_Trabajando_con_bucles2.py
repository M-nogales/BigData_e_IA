# 10. **Contar dígitos de un número**
# Usa un bucle while para contar cuántos dígitos tiene un número.

n = int(input("Dame un número entero y te diré su cantidad de digitos: "))

contador = 0

if n == 0:
    contador = 1
else:
    n = abs(n)
    while n > 0:
        n //= 10
        contador += 1

print(f"La cantidad de dígitos es: {contador}")