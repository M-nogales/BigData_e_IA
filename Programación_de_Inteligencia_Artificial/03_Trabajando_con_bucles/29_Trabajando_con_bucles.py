#29. **Comparar cadenas con while**  
#    Escribe un programa que compare dos cadenas carácter por carácter utilizando un bucle while.
string1 = input("Dame la primera cadena: ")
string2 = input("Dame la segunda cadena: ")

i = 0
equal_strings = True

if len(string1) != len(string2):
    print("Ni siquiera tienen la misma longitud")
    equal_strings = False

while equal_strings == True and  i < len(string1) and i < len(string2):
    if string1[i] != string2[i]:
        print("diferencia en el caracter: ", i," en la cadena 1 es: ",
              string1[i]," mientras que en la cadena 2 es: ",string2[i])
        equal_strings = False
    i += 1

if equal_strings:
    print("Cadenas exactamente iguales")
else:
    print("Cadenas diferentes")