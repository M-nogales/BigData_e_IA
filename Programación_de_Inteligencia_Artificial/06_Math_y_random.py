import math
import random as r

raiz = math.sqrt(5)
print('raiz de 5: ', raiz)

potencia = math.pow(2,5)
print('potencia 2^5: ', potencia)

factorial = math.factorial(5)
print('factorial 5: ', factorial)

pepi = math.pi
print('pepi: ', pepi)

e = math.e
print('e: ', e)

rendondear_alza = math.ceil(2.3456)
print('rendondear_alza: ', rendondear_alza)

rendondear_baja = math.floor(2.3456)
print('rendondear_baja: ', rendondear_baja)

absolute = math.fabs(-54)
print('absolute: ', absolute)

print("-----------------------------------")

aleatorio = r.random()
print('aleatorio: ', aleatorio)

aleatorio_1_10 = r.randint(1,10)
print('aleatorio_1_10: ', aleatorio_1_10)

decimal = r.uniform(1,10)
print('decimal: ', decimal)

colores = ["rojo","amarillo","azul"]
print('color aleatorio: ', r.choice(colores))

nums = [0,1,2,3,4,5,6,7]
r.shuffle(nums)
print('nums: ', nums)

print('r.sample(nums): ', r.sample(nums,3))