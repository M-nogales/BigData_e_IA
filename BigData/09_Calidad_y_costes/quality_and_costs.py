import pandas as pd
import re
import matplotlib.pyplot as plt

# leer datosClientes.csv
df = pd.read_csv('datosClientes.csv')

# datos iniciales sin tratar y columnas que aparecen
# ID Cliente|Nombre|Dirección|Correo Electrónico|Teléfono|
# Última Actualización (días)|Pedido Válido|Tiempo Acceso (seg)
print(df.head(20))

# este comando ya nos indica la cantidad de valores nulos en cada columna
#en este caso las columnas problematicas son Nombre, Correo, Dirección y Teléfono
print(df.info(), "\n")

accuracy = df.copy()
completeness = df.copy()
consistency = df.copy()
validity = df.copy()
integrity = df.copy()
actualization = df.copy()
accessibility = df.copy()

#! errores de exactitud
#identificar registros con errores en el campo nombre y dirección
accuracy_errors_df = accuracy[(accuracy['Nombre'].str.len() < 3) | (accuracy['Dirección'].str.len() < 3) | accuracy['Nombre'].isna() | accuracy['Dirección'].isna()]

print(accuracy_errors_df.shape[0]," registros con errores en nombre o dirección.")

#! errores de completitud
# comprobar si el nombre tiene valor nan se elimina la fila y contar cuantos datos presentan nan
completeness_errors = completeness[['Nombre', 'Dirección', 'Correo Electrónico']].isna().sum().sum()

print("Errores de completitud: ", completeness_errors)

#!errores de consistencia
# comprobar si el telefono tiene el formato correcto "+34 123456789"
regex_telephone = r'^\+34 \d{9}$'
telephone_errors = consistency[~df['Teléfono'].str.contains(regex_telephone, na=False, regex=True)].shape[0]

print(f'Errores de consistencia en teléfonos: {telephone_errors}')

#!errores de validez
# comprobar si el email tiene el formato correcto "
email_regex = r'^[a-zA-Z0-9](?:[a-zA-Z0-9._-]*[a-zA-Z0-9])?@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email_errors = validity['Correo Electrónico'].apply(lambda x: not bool(re.match(email_regex, x)) if pd.notna(x) else True).sum()

print(f'Errores de consistencia en teléfonos: {telephone_errors}')

#!integridad
#pedidos Inválidos
integrity_errors = integrity[integrity['Pedido Válido'] != "Válido"].shape[0]

print(f'Errores de integridad en pedidos: {integrity_errors}')

#!actualización
actualization_errors = actualization[actualization['Última Actualización (días)'] > 15].shape[0]

print(f'Errores de actualización: {actualization_errors}')

#!accesibilidad
accessibility_errors = accessibility[accessibility['Tiempo Acceso (seg)'] > 0.3].shape[0]

print(f'Errores de accesibilidad: {accessibility_errors}')

#!calcular costes
accuracy_cost = accuracy_errors_df.shape[0] * 1000
completeness_cost = completeness_errors * 500
consistency_cost = telephone_errors * 2000
validity_cost = email_errors * 300
integrity_cost = integrity_errors * 1500
actualization_cost = actualization_errors * 1200
accessibility_cost = accessibility_errors * 1000
total = accuracy_cost + completeness_cost + consistency_cost + validity_cost + integrity_cost + actualization_cost + accessibility_cost

print(f'\nCoste total: {total}€')

errors = [
    ('Exactitud', accuracy_errors_df.shape[0]),
    ('Completitud', completeness_errors),
    ('Consistencia', telephone_errors),
    ('Validez', email_errors),
    ('Integridad', integrity_errors),
    ('Actualización', actualization_errors),
    ('Accesibilidad', accessibility_errors)
]

# Separar los nombres de los errores y sus valores
error_names, error_values = zip(*errors)

plt.figure(figsize=(10, 6))
plt.barh(error_names, error_values, color='skyblue')
plt.xlabel('Número de Errores')
plt.title('Errores en la Calidad de Datos')
plt.show()

# Crear un gráfico de barras para los costes
costs = [
    ('Exactitud', accuracy_cost),
    ('Completitud', completeness_cost),
    ('Consistencia', consistency_cost),
    ('Validez', validity_cost),
    ('Integridad', integrity_cost),
    ('Actualización', actualization_cost),
    ('Accesibilidad', accessibility_cost)
]

# Separar los nombres de los costes y sus valores
cost_names, cost_values = zip(*costs)

plt.figure(figsize=(10, 6))
plt.barh(cost_names, cost_values, color='lightcoral')
plt.xlabel('Costo (€)')
plt.title('costes Asociados a los Errores en los Datos')
plt.show()