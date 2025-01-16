'''
Escribir un programa que pregunte al usuario por las ventas de un rango de años y
muestre por pantalla un diagrama de líneas con la evolución de las ventas.
'''
import matplotlib.pyplot as plt

years=[]
sales=[]

while True:
    year = input("Introduce un año (haz entre para terminar):")
    if year == "":
        break
    years.append(year)
    sale = input("Introduce las ventas de ese año: ")
    sales.append(sale)

plt.plot(years, sales)
plt.title("Evolución de las ventas")
plt.ylabel("Ventas")
plt.xlabel("Años")
plt.show()