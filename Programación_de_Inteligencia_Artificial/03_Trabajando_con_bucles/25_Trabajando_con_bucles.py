#25. **Cifrar una cadena con for**  
#    Escribe un programa que cifre una cadena desplazando cada letra una posición en el alfabeto utilizando un bucle for.
abecedario = "abcdefghijklmnopqrstuvwxyz"

palabra = input("dime una palabra a cifrar ").lower()

result = []

for letra in palabra:
    posicion = abecedario.index(letra)

    if posicion == len(abecedario) - 1:
        posicion = 0
    else:
        posicion += 1

    result.append(abecedario[posicion])

result_final = "".join(result)
print('palabra cifrada: ', result_final)