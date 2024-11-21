# 31. **Palíndromo**
# Determina si una palabra es un palíndromo.

palabra = input("Dame una palabra").lower()

inicio = 1
fin = len(palabra) - 1
palindromo = True

while inicio < fin:
    if palabra[inicio] != palabra[fin]:
        palindromo = False
        print("No es palindromo")
        break
    
    inicio += 1
    fin -= 1
else:
    if palindromo : print("Es palindromo")