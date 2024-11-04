colecciones: continente | pais
pais con todo, transformar fecha

trainers.json
types.json
professors.json
gyms.json

villains.json
regions_data.json
pokemons_data.json
moves_data.json

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **07_Extrac_pokemon_data/**: Carpeta que contiene los scripts de Python encargados de extraer y procesar datos de la PokéAPI.
  - `add_cuantity_trainers.py`: Añade la cantidad total de entrenadores al archivo `trainers.json`.
  - `extrac_poke_api_url.py`: Extrae URLs y nombres de todos los Pokémon desde la PokéAPI y los guarda en `pokemons_api_url.json`.
  - `extrac_moves_api_url.py`: Obtiene las URLs y nombres de todos los movimientos desde la PokéAPI y los almacena en `moves_api_url.json`.
  - `cleaning_trainers.py`: Limpia y organiza los datos de entrenadores, relacionándolos con sus respectivas generaciones.
  - `insert_mongo.py`: Inserta datos de archivos JSON en una base de datos MongoDB.
  - `get_villains_from_trainers.py`: Filtra los entrenadores que son villanos y guarda esta información en `villains.json`.
  - `extrac_region_api_url.py`: Extrae URLs y nombres de todas las regiones desde la PokéAPI.
  - `get_all_region_data.py`: Obtiene datos detallados de cada región utilizando las URLs extraídas.
  - `get_all_pokemon_data.py`: Recopila información completa de cada Pokémon desde las URLs obtenidas.
  - `get_all_moves_data.py`: Recupera detalles de cada movimiento desde las URLs proporcionadas.

- **data/**: Carpeta que almacena los archivos JSON con la información procesada.
  - `trainers.json`: Información de los entrenadores.
  - `types.json`: Tipos de Pokémon y sus debilidades.
  - `professors.json`: Información sobre los profesores de cada región.
  - `gyms.json`: Detalles de los gimnasios y sus líderes.
  - `villains.json`: Lista de entrenadores que son villanos.
  - `regions_data.json`: Datos detallados de cada región.
  - `pokemons_data.json`: Información completa de cada Pokémon.
  - `moves_data.json`: Detalles de cada movimiento.

- **README.md**: Archivo de documentación que describe el proyecto y su estructura.

## Descripción de los archivos

- **extrac_poke_api_url.py**

  Extrae URLs y nombres de todos los Pokémon desde la PokéAPI y los guarda en `pokemons_api_url.json`.

- **extrac_moves_api_url.py**

  Obtiene las URLs y nombres de todos los movimientos desde la PokéAPI y los almacena en `moves_api_url.json`.

- **extrac_region_api_url.py**

  Extrae las URLs y nombres de todas las regiones desde la PokéAPI y los guarda en `regions_api_url.json`.

- **get_villains_from_trainers.py**

  Filtra los entrenadores que son villanos y guarda esta información en `villains.json`.

- **get_all_region_data.py**

  Obtiene datos detallados de cada región utilizando las URLs extraídas y los almacena en `regions_data.json`.

- **get_all_pokemon_data.py**

  Recopila información completa de cada Pokémon desde las URLs obtenidas y guarda los datos en `pokemons_data.json`.

- **get_all_moves_data.py**

  Recupera detalles de cada movimiento desde las URLs proporcionadas y almacena la información en `moves_data.json`.