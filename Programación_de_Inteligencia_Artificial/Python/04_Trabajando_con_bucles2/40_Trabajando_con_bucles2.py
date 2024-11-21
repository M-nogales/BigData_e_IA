# 40. **Convertir números decimales a binarios**
# Convierte un número decimal a binario usando un bucle.

def decimal_a_binario(num):
    # Separar la parte entera y la parte decimal
    parte_entera = int(num)
    parte_fraccionaria = num - parte_entera
    
    # Convertir parte entera a binario
    if parte_entera == 0:
        binario_entero = "0"
    else:
        binario_entero = ""
        while parte_entera > 0:
            residuo = parte_entera % 2
            binario_entero = str(residuo) + binario_entero
            parte_entera = parte_entera // 2
    
    # Convertir parte decimal a binario
    binario_fraccionario = ""
    while parte_fraccionaria > 0:

        parte_fraccionaria *= 2
        bit = int(parte_fraccionaria)  # Toma la parte entera

        binario_fraccionario += str(bit)
        parte_fraccionaria -= bit  # Eliminar la parte entera
    
    if binario_fraccionario:
        return f"{binario_entero}.{binario_fraccionario}"
    else:
        return binario_entero

numero_decimal = float(input("Introduce un número decimal (puedes usar . o ,): ").replace(',', '.'))
resultado_binario = decimal_a_binario(numero_decimal)
print(f"El número decimal {numero_decimal} en binario es: {resultado_binario}")
