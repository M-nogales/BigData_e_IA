# 17. **Obtener el mayor de dos números**
# Crear una función lambda que devuelva el mayor de dos números.

bigest = lambda x, y: x if x > y else y

print('bigest(5, 3): ', bigest(5, 3))