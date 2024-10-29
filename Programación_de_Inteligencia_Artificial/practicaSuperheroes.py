import json

with open("superheroe_spain.json","r") as fichero_lectura:
    data = json.load(fichero_lectura)
    
print('data: ', data["superheroes_espanoles"])

resumen_heroes=[]
for superhero in data['superheroes_espanoles']:
    heroes={
        'nombre_real': superhero['nombre_real'],
        'alias': superhero['alias'],
        'ciudad': superhero['ciudad']
    }
    resumen_heroes.append(heroes)

print('resumen_heroes: ', resumen_heroes)
nuevos_heroes = [
    {
        "nombre_real": "Sofia Ruiz",
        "alias": "La Cazadora",
        "ciudad": "Madrid"
    },
    {
        "nombre_real": "Juan",
        "alias": "El Magán",
        "ciudad": "Magallanes"
    },
        {
        "nombre_real": "Carlos Montolla",
        "alias": "El grande",
        "ciudad": "Madrid city"
    },
            {
        "nombre_real": "José Mota",
        "alias": "El hombre la vara",
        "ciudad": "Vara de Rey"
    }
]

for nuevo_heroe in nuevos_heroes: resumen_heroes.append(nuevo_heroe)


print('resumen_heroes: ', resumen_heroes)

with open("superheroe_spain_version_ManuelNogalesSerrano.json","w") as fichero:
    json.dump(resumen_heroes,fichero,indent=4)