# 19. **Verificar si una cadena es palíndromo**
# Utilizar una función lambda para verificar si una cadena es un palíndromo (se lee igual al derecho y al revés).

palindrome = lambda x: x == x[::-1]
print('palindromo("amor a roma"): ', palindrome("amor a roma"))