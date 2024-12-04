# 01. **Filtra a los alumnos que tienen 20 años o más y muestra sus notas finales.**
''' Filtra a los alumnos que tienen 20 años o más y muestra sus notas finales.'''

#leer datos_alumnos.xlsx
import pandas as pd


df = pd.read_excel("results/datos_alumnos.xlsx")
#para simplificar el ejercicio y no repetir lo que ya realicé con las serializaciones,
# voy a asumir que el tercer trimestres es la media de los trimestres

df["Programación Final"] = df["Programación T1"] + df["Programación T2"] + df["Programación T3"] / 3
df["Base de Datos Final"] = df["Base de Datos T1"] + df["Base de Datos T2"] + df["Base de Datos T3"] / 3
df["Lenguajes Final"] = df["Lenguajes T1"] + df["Lenguajes T2"] + df["Lenguajes T3"] / 3
df["Sistemas Final"] = df["Sistemas T1"] + df["Sistemas T2"] + df["Sistemas T3"] / 3
df["Entornos Final"] = df["Entornos T1"] + df["Entornos T2"] + df["Entornos T3"] / 3
print(df[df["Edad"] >= 20][["Programación Final", "Base de Datos Final", "Lenguajes Final", "Sistemas Final", "Entornos Final"]]) 
print("----------------------------------------------")
print(df[df["Edad"] >= 20])
#exportar a excel
df.to_excel("results/01_datos_alumnos.xlsx", index=False)