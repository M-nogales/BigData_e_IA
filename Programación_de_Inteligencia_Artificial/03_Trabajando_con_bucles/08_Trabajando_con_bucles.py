# 8. **Conversión de temperaturas con for**  
#    Escribe un programa que convierta un rango de temperaturas de Celsius a Fahrenheit utilizando un bucle for.

temperaturas_celsius = [0,10,20,30,40,50,60,70,80,90,100]

# tabla made in chat
print("Celsius\tFahrenheit")
print("----------------------")

for celsius in temperaturas_celsius:
    fahrenheit = (celsius * 9/5) + 32  
    print(f"{celsius}\t{fahrenheit:.2f}")