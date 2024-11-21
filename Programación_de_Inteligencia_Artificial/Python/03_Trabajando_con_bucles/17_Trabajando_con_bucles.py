#17. **Potencia de un número con for**  
#    Escribe un programa que calcule la potencia de un número dado utilizando un bucle for.

base = int(input("Dame la base: "))
exp = int(input("Dame el exponente: "))

result = 1

#lo mas facil para hacer un for de 1 numero es un for vacio
# a menos que haya entendido mál el ejercicio

for _ in range(exp):
    result *= base  

print(f"{base} elevado a la potencia de {exp} es: {result}")
