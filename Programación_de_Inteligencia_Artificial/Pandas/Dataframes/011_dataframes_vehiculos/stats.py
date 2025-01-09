import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt

# Ruta del archivo CSV
file_path = "data/transformed_us_cars.csv"

# Leer el archivo CSV
data = pd.read_csv(file_path, encoding='utf-8')

# Comprobación del tamaño de los datos
print(f"Total de registros cargados: {len(data)}")
print("Primeras filas del dataset:")
print(data.head())  # Muestra las primeras filas

# Verificación de tipos de datos
print("\nTipos de datos de cada columna:")
print(data.dtypes)

# Comprobación de valores nulos
print("\nNúmero de valores nulos en cada columna:")
print(data.isnull().sum())

# Reemplazo de valores nulos si es necesario
# 1. Rellenar los valores nulos en la columna 'Precio' con la media
data['Precio'] = data['Precio'].fillna(data['Precio'].mean())

# 2. Eliminar las filas donde la columna 'make_name' (marca del vehículo) sea NaN
data = data.dropna(subset=['Marca'])

# Verificación final después de limpiar nulos
print("\nValores nulos después de limpieza:")
print(data.isnull().sum())


mean_price = data['Precio'].mean()
mean_km = data['Kilometros'].mean()
median_price = data['Precio'].median()
std_price = data['Precio'].std()
min_price = data['Precio'].min()
max_price = data['Precio'].max()

# DataFrame con estadísticas extra
additional_stats = pd.DataFrame({
    'Media de precio': [mean_price],
    'Media de kilometros': [mean_km],
    'Mediana de precio': [median_price],
    'Desviación estándar de precio': [std_price],
    'Mínimo de precio': [min_price],
    'Máximo de precio': [max_price]
})

statistics = data.describe()

# Concatenar los extra con el DataFrame original de estadísticas
statistics = pd.concat([statistics, additional_stats], axis=1)

statistics.to_csv('data/stats.csv', index=True)

# Mostrar el análisis estadístico
print("\nAnálisis estadístico:")
print(statistics)

# Graficar la distribución del precio de los vehículos
plt.figure(figsize=(10, 6))
plt.hist(data['Precio'].dropna(), bins=50, color='blue', edgecolor='black', alpha=0.7)
plt.title('Distribución del Precio de los Vehículos')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Graficar la distribución de los kilómetros
plt.figure(figsize=(10, 6))
plt.hist(data['Kilometros'].dropna(), bins=50, color='green', edgecolor='black', alpha=0.7)
plt.title('Distribución de Kilómetros de los Vehículos')
plt.xlabel('Kilómetros')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Graficar la relación entre precio y kilometraje
plt.figure(figsize=(10, 6))
plt.scatter(data['Kilometros'], data['Precio'], color='red', alpha=0.5)
plt.title('Relación entre Precio y Kilómetros')
plt.xlabel('Kilómetros')
plt.ylabel('Precio')
plt.grid(True)
plt.show()


# Filtrar vehículos por marca, modelo, año, precio o color
filtered_vehicles = data[(data['Marca'] == 'Toyota') & (data['Anyo'] >= 2015) & (data['Precio'] < 20000)]

# Mostrar los primeros registros filtrados
print("\nVehículos filtrados (Marca: Toyota, Año >= 2015, Precio < 20000):")
print(filtered_vehicles.head())

filtered_vehicles.to_csv("data/filtered_vehicles.csv", index=False, encoding='utf-8')


# Ordenar vehículos por precio de menor a mayor
sorted_by_price = data.sort_values(by='Precio', ascending=True)

sorted_by_year = data.sort_values(by='Anyo', ascending=False)

print("\nVehículos ordenados por precio (de menor a mayor):")
print(sorted_by_price.head())

sorted_by_price.to_csv("data/sorted_by_price.csv", index=False, encoding='utf-8')
sorted_by_year.to_csv("data/sorted_by_year.csv", index=False, encoding='utf-8')


# Cálculo de la depreciación basada en el año del vehículo
# Suponemos que la depreciación es un 15% anual
current_datetime = datetime.now()
current_year = current_datetime.year
data['Depreciacion'] = data['Anyo'].apply(lambda x: (current_year - x) * 0.15)

print("\nVehículos con la columna de depreciación añadida:")
print(data[['Marca','Modelo','Anyo', 'Precio', 'Depreciacion']].head())

data.to_csv("data/vehicles_with_depreciation.csv", index=False, encoding='utf-8')