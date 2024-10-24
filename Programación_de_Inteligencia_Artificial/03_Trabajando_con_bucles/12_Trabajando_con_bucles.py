#12. **Mínimo común múltiplo (MCM) con while**  
#    Escribe un programa que encuentre el MCM de dos números utilizando un bucle while.

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

n1 = 15
n2 = 48

resultado = mcm(n1, n2)
print('resultado: ', resultado)
