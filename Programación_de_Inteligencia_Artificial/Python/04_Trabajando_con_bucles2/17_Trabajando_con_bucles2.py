# 17. **Verificar si un carácter es una vocal**
# Escribe un programa que verifique si un carácter ingresado es una vocal.

caracter = input("Dame un carácter para verificar si es vocal: ")

if len(caracter) == 1:
    caracter = caracter.lower()
    
    if caracter in 'aeiou':
        print(f"{caracter} es una vocal.")
    else:
        print(f"{caracter} no es una vocal.")
else:
    print("Por favor, dame solo un carácter.")