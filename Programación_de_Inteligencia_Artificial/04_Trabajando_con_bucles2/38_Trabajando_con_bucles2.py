# 38. **Determinar el segundo número más grande en una lista**
# Encuentra el segundo número más grande en una lista.

def segundo_mas_grande(lista):
    lista_unica = list(set(lista))
    
    if len(lista_unica) < 2:
        return None
    
    lista_unica.sort(reverse=True)
    
    return lista_unica[1]

nums = [3, 5, 1, 4, 5, 2, 8, 8]
resultado = segundo_mas_grande(nums)

if resultado is not None:
    print(f"El segundo número más grande es: {resultado}")
else:
    print("No hay suficientes números únicos para determinar el segundo más grande.")

#opción clasica sin "" metodos
def segundo_mas_grande2(lista):
    # tenemos que usar un número infinito negativo para evitar que de error en caso
    # de que el segundo más pequeño sea 0
    primer_mas_grande = segundo_mas_grande = float('-inf')
    
    for numero in lista:
        if numero > primer_mas_grande:
            segundo_mas_grande = primer_mas_grande
            primer_mas_grande = numero 
        elif primer_mas_grande > numero > segundo_mas_grande:
            segundo_mas_grande = numero

    return segundo_mas_grande if segundo_mas_grande != float('-inf') else None
