# 36. **Juego del 'FizzBuzz'**
# Imprime los números del 1 al 100 con 'Fizz', 'Buzz', o 'FizzBuzz'.

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)