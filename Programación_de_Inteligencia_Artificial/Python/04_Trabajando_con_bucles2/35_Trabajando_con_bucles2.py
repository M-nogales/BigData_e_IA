# 35. **Números perfectos**
# Encuentra todos los números perfectos entre 1 y 1000.

def es_numero_perfecto(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

print("Números perfectos entre 1 y 1000:")
for num in range(1, 1001):
    if es_numero_perfecto(num):
        print(num)