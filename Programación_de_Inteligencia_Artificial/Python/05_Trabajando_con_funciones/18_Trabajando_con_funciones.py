# 18. **Filtrar números pares en una lista**
# Usa una función lambda con filter() para obtener sólo los números pares de una lista.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pairs = list(filter(lambda x: x % 2 == 0, nums))
print('pares: ', pairs)