import re
import pandas as pd
import numpy as np

# https://www.kaggle.com/datasets/ananaymital/us-used-cars-dataset

file_path = "data/us_cars.csv"

data = pd.read_csv(file_path)

# Crear el dataframe
df = pd.DataFrame()

# Función para extraer el número de asientos (sin la palabra 'seats') <numero de asientos> seats
def extract_seats(seat_string):
    match = re.match(r"(\d+)\s*seats?", str(seat_string))
    return int(match.group(1)) if match else np.nan

# Función para limpiar las dimensiones y eliminar la palabra "in"
def clean_size(size_string):
    # Elimina la palabra "in" y convierte las dimensiones a cm
    if isinstance(size_string, str):
        size_string = size_string.replace(" in", "")  # Eliminar " in"
        dimensions = size_string.split('x')  # Dividir por 'x'
        if len(dimensions) == 3:
            try:
                # Convertir las dimensiones a float y luego a cm
                dimensions_cm = [round(float(dim) * 2.54, 2) for dim in dimensions]
                return f"{dimensions_cm[0]}x{dimensions_cm[1]}x{dimensions_cm[2]}"
            except ValueError:
                return np.nan
    return np.nan

# Transformar y asignar columnas necesarias
df["N_ID"] = data["listing_id"]  # Usar 'listing_id' como identificador único
df["Marca"] = data["franchise_make"]  # Marca del vehículo
df["Modelo"] = data["model_name"]  # Modelo
df["Anyo"] = data["year"]  # Año del vehículo
df["Color"] = data["exterior_color"]  # Color exterior
df["Kilometros"] = data["mileage"]  # Kilometraje (puede necesitar limpieza)
df["Motor"] = data["engine_type"]  # Tipo de motor
df["Combustible"] = data["fuel_type"]  # Tipo de combustible
df["Tamaño"] = data.apply(
    lambda row: clean_size(f"{row['length']}x{row['width']}x{row['height']}")
    if not (pd.isna(row["length"]) or pd.isna(row["width"]) or pd.isna(row["height"]))
    else np.nan,
    axis=1,
)  # Limpiar y convertir dimensiones (Largo x Ancho x Altura) en cm
df["N_Ocupantes"] = data["maximum_seating"].apply(extract_seats)  # Extraer número de asientos
df["Peso"] = np.nan  # No hay peso explícito en el dataset original
df["C_Maletero"] = np.nan  # No hay capacidad en el dataset original
df["Potencia"] = data["horsepower"]  # Potencia del motor
df["Emisiones"] = np.nan  # No hay datos de emisiones de CO2 en el dataset original
df["Autonomia"] = data.apply(
    lambda row: round(float(row["fuel_tank_volume"]) * float(row["combine_fuel_economy"]), 2)
    if not (pd.isna(row["fuel_tank_volume"]) or pd.isna(row["combine_fuel_economy"]))
    else np.nan,
    axis=1,
)  # Calcular autonomía usando tanque y consumo combinado
df["Precio"] = data["price"]  # Precio del vehículo

# Filtrar 10,000 registros
df = df.head(10000)

# Exportar el nuevo dataframe a un archivo CSV para ver el resultado
output_file_path = "data/transformed_us_cars.csv"
df.to_csv(output_file_path, index=False, encoding='utf-8')

print(f"El dataframe transformado se ha guardado en: {output_file_path}")
