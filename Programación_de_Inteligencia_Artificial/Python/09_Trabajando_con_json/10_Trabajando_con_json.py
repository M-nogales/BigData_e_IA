# 10. **Red de Superhéroes**
# Contiene superhéroes con su alias, habilidades, ciudad de origen y equipo.
# Filtrar por ciudad o equipo, agregar nuevos superhéroes, listar habilidades únicas.
'''  JSON = 
{
    "superheroes": [
        {"alias": "El Cid", "habilidades": ["esgrima", "estrategia"], "ciudad": "Burgos", "equipo": "Los Defensores"},
        {"alias": "La Dama de Plata", "habilidades": ["manipulación de metales"], "ciudad": "Toledo", "equipo": "Los Defensores"}
    ]
}
'''

import json


superheroes = {
    "superheroes": [
        {"alias": "El Cid", "habilidades": ["esgrima", "estrategia"], "ciudad": "Burgos", "equipo": "Los Defensores"},
        {"alias": "La Dama de Plata", "habilidades": ["manipulación de metales"], "ciudad": "Toledo", "equipo": "Los Defensores"}
    ]
}


def filtrar_superheroes(ciudad=None, equipo=None):
    for superheroe in superheroes['superheroes']:
        if (ciudad and superheroe['ciudad'].lower() == ciudad.lower()) or (equipo and superheroe['equipo'].lower() == equipo.lower()):
            return superheroe
    else:
        return f'No se ha encontrado ningún superhéroe de la ciudad {ciudad} y equipo {equipo}'

def agregar_superheroe(alias, habilidades, ciudad, equipo):
    nuevo_superheroe = {
        "alias": alias,
        "habilidades": habilidades,
        "ciudad": ciudad,
        "equipo": equipo
    }
    superheroes["superheroes"].append(nuevo_superheroe)
    return "Superhéroe añadido"

def habilidades_unicas():
    for superheroe in superheroes['superheroes']:
        habilidades_unicas = set(superheroe['habilidades'])
    
    return list(habilidades_unicas)

def guardar_heroes():
    with open("jsons/10_superheroes.json", "w") as archivo:
        json.dump(superheroes, archivo, indent=2)


# pereza repetirlo 10 veces/bucle
print('agregar_superheroe: ',
      agregar_superheroe("Blas de Lezo", ["estrategia", "valentía"], "Pasajes", "La Armada"))

print('filtrar_superheroes("Burgos", "Los Defensores"): ', filtrar_superheroes("Burgos", "Los Defensores"))
print('filtrar_superheroes("Burgos", "Los Defensores"): ', filtrar_superheroes( equipo = "La armada"))
print('habilidades_unicas(): ', habilidades_unicas())
guardar_heroes()
