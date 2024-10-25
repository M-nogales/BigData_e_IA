#19. **Contar letras y dígitos con for**  
#    Escribe un programa que cuente cuántas letras y cuántos dígitos hay en una cadena utilizando un bucle for.

string = input("Dame una cadena con números y letras: ")

char_counter = 0
num_counter = 0

for char in string:
    
    if char.isalpha():
        char_counter += 1
    
    elif char.isdigit():
        num_counter += 1

print(f"En la cadena ingresada hay {char_counter} letra(s) y {num_counter} dígito(s).")
