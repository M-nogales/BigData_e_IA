#10. **Conteo de vocales con for**  
#    Escribe un programa que cuente cuántas vocales hay en una palabra dada utilizando un bucle for y una condición if.

palabra = input("Dame una palabra: ")

vocales = "aeiouAEIOU"
counter = 0

for letra in palabra:
    
    if letra in vocales:
        counter += 1

print(f"La palabra '{palabra}' tiene {counter} vocal(es).")
