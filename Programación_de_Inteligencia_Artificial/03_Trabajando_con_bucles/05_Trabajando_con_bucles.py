#5. Palíndromo con while  
#   Escribe un programa que verifique si una palabra es un palíndromo utilizando un bucle while.

palabra = input("Dime una palabra ").lower()

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