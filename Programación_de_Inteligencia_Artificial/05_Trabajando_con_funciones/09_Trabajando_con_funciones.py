# 09. **Ordenar lista de menor a mayor**
# Crear una función que ordene una lista de números de menor a mayor sin usar el método sort().

# lo que pides a chatgpt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# lo que te llega:

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            # Si el elemento actual es mayor que el siguiente, intercambiarlos
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print('bubble_sort([64, 34, 25, 12, 22, 11, 11, 90]): ',
bubble_sort([64, 34, 25, 12, 22, 11, 11, 90])) # [11, 12, 22, 25, 34, 64, 90]