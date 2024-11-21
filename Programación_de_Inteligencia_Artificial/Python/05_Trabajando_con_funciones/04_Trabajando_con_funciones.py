# 04. **Conversión de Celsius a Fahrenheit**
# Crear una función que convierta temperaturas de grados Celsius a Fahrenheit.





def celsius_to_fahrenheit(temperature):
    # return(celsius * 9/5) + 32 # mejor damos valores unicos  
    for celsius in temperature:
        return(celsius * 9/5) + 32  

print("Celsius\tFahrenheit")
print("----------------------")

print("0\t", celsius_to_fahrenheit([0]))
print("1\t", celsius_to_fahrenheit([15]))
print("2\t", celsius_to_fahrenheit([22]))
print("3\t", celsius_to_fahrenheit([33]))
print("4\t", celsius_to_fahrenheit([45]))
