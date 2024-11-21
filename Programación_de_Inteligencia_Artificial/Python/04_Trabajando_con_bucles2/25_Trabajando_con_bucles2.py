# 25. **Contar vocales y consonantes**
# Cuenta cuántas vocales y cuántas consonantes contiene una cadena de texto.

texto = input("Dame una cadena de texto: ").lower()

abecedario="abcdefghijklmnopqrstuvwxyz"
vocales = "aeiou"
contador_vocales = 0
contador_consonantes = 0

for caracter in texto:
    if caracter in abecedario:
        if caracter in vocales:
            contador_vocales += 1
        else:
            contador_consonantes += 1

print(f"Vocales: {contador_vocales}")
print(f"Consonantes: {contador_consonantes}")