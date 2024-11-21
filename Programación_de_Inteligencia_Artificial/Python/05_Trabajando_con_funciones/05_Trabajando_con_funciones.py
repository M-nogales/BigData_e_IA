# 05. **Suma de elementos en una lista**
# Escribir una función que reciba una lista y devuelva la suma de sus elementos.

def list_sum (list):
    sum = 0
    for i in list:
        sum += i
    return sum

print('list_sum([1, 2, 3, 4, 5]): ', list_sum([1, 2, 3, 4, 5]))