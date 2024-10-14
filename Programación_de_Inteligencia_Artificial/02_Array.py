texto_a_mostrar = "En un lugar de la mancha"
frutas = ["Melón","Sandía","Plátano","Melocotón"]
print(frutas)
nums = [1,2,25,234,8,-1]
print(nums)
mix = [ "Melón",1,"Sandía",2,"Peras",4]
print(mix)
nuevaLista = list(("A","b","C"))
print(nuevaLista)
alumnos = nuevaLista # list(nuevaLista)
print(alumnos)
# al editar alumnos se edita nueva lista, copiando con list(nuevaLista), no
# alumnos[0]=1
# print(alumnos)
# print(nuevaLista)
print(frutas[0::2])# jump 2
print(frutas[::-1])# reverse 
if "Plátano" in frutas: print("yes") 

if "Mango" in frutas:
    print("yes")
else:
    print("no")

nums.append("append")# final
nums.insert(0,"insert")# dado index
print(nums)

nums.remove("insert")# busca y elimina el primero
nums.pop() # elimina última del array
del nums[0] # del nums elimina todo el array
print(nums)
