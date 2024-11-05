# 08. **Contador de vocales en una cadena**
# Generar una función que cuente cuántas vocales hay en una cadena.

def vocals_sum(text):
    vocals = "aeiouáéíóú"
    counter = 0

    for character in text:
        if character in vocals:
            counter += 1

    return counter

text = input("Dame una cadena de texto: ").lower()
vocals_sum(text)