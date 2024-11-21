#13. **Palabras que empiezan con una letra con for**  
#    Escribe un programa que recorra una lista de palabras y cuente cuántas empiezan con una letra específica utilizando un bucle for.

palabras = ["manzana", "melón", "pera", "mango", "fresa", "mandarina"]

letra = input("Dame letra inicial para buscar: ").lower()

counter = 0

for palabra in palabras:

    if palabra.startswith(letra):
        counter += 1

print(f"Hay {counter} palabra(s) que empiezan con la letra '{letra}'.")
