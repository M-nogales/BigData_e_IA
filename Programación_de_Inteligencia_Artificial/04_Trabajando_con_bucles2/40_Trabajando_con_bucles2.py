# 40. **Convertir números decimales a binarios**
# Convierte un número decimal a binario usando un bucle.

def decimal_a_binario(numero):
    if numero == 0:
        return "0"  # Caso especial para el cero
    
    binario = ""  # Cadena para almacenar el resultado en binario

    while numero > 0:
        residuo = numero % 2  # Obtener el residuo (0 o 1)
        binario = str(residuo) + binario  # Concatenar el residuo al principio de la cadena
        numero //= 2  # Dividir el número por 2 (usar división entera)

    return binario  # Retornar la representación en binario

# Ejemplo de uso
numero_decimal = int(input("Ingresa un número decimal: "))
resultado = decimal_a_binario(numero_decimal)
print(f"El número decimal {numero_decimal} en binario es: {resultado}")