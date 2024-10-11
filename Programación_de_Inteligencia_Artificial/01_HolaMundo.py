print("Hola mundo")
var = "Hola que tal"
len(var)
type(var)
# a=int(input("Dame un valor"))
# b=int(input("Dame un segundo valor"))
# print(a+b)
# suma = int(a) + int(b)
# print("suma por var: "+str(suma))
mult = 6*5
print("mult (int) var: "+str(mult))
multfloat = 6.5*5
print("mult (float) var: "+str(multfloat))
div=9 / 3
print("div 9/3 (float)"+str(div))
divnormal= 10/3
print(divnormal)
divint= 10//3
print(divint)
modu = 10%3 # modulo entero
modufloat = 10%3 # modulo float
expo = 2**2 # exponente entero
expofloat = 2**2.0 # exponente float
x = 5
x//5 # no guardado en memoria
print(x)
x//=5 # guardado en memoria
print(x)
print(y:=10) #impreso y asignado
type(y)
print (y)
10 == "10"
# == compara el valor del dato no el tipo
# is / is not compara valor y tipo en js es ===
w="Hola Mundo"
wa="test2"
print( w+ " " +wa)
print( w,"-",wa)
print(w[2])
print("------------------------")
for z in w:
    print(z)

print("------------------------")

for z in w[::-1]:
    print(z)

print("------------------------")
print(w[1:4])
print(w[1:1])
print(w[1:])
print(w[:])
print(w[:7])
print(w[-6:-1])
print(w[1:7:2])# :inicio:final:paso/saltos
print(w[0:len(w):2])
print(w[0:-6]) # en caso de +,- el - pasa a +
print(w[-1:6]) # en caso de -,+ no funciona 
print(w[::-1])

print("------------------------")
c1 = "HOLA"
c2 = "mundo"
c3 = "HOLA MUNDO"
print(c1*5 + c2)
print(c1 in c3)
print(c2 in c3)
min(c3) # menor en ascii en este caso espacio
max(c3) # mayor en ascii 'U'
print(c3.lower())
print(c3.title()) # primera de cada palabra en mayus
print(c3.split(" "))

