#22. **Encontrar múltiplos con for**  
#    Escribe un programa que encuentre todos los múltiplos de un número en un rango dado utilizando un bucle for.

num = int(input("Dame el número para encontrar sus múltiplos: "))
start = int(input("Dame el inicio del rango: "))
end = int(input("Dame el final del rango: "))

multiplos = []

for i in range(start, end + 1):

    if i % num == 0:
        multiplos.append(i)

print(f"Los múltiplos de {num} en el rango de {start} a {end} son: {multiplos}")
