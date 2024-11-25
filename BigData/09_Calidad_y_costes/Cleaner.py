import pandas as pd
import re

# Cargar los datos
df = pd.read_csv('datosClientes.csv')

# 1. **Eliminar registros con errores en Nombre o Dirección** (Precisión)
df = df[
    (df['Nombre'].str.len() >= 3) & 
    (df['Dirección'].str.len() >= 3) & 
    df['Nombre'].notna() & 
    df['Dirección'].notna()
]

# 2. **Eliminar registros con valores nulos en Nombre, Dirección o Correo Electrónico** (Completitud)
df = df.dropna(subset=['Nombre', 'Dirección', 'Correo Electrónico'])

# 3. **Eliminar registros con Teléfonos inválidos** (Consistencia)
regex_telephone = r'^\+34 \d{9}$'
df = df[df['Teléfono'].str.contains(regex_telephone, na=False, regex=True)]

# 4. **Eliminar registros con Correos Electrónicos inválidos** (Validez)
email_regex = r'^[a-zA-Z0-9](?:[a-zA-Z0-9._-]*[a-zA-Z0-9])?@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
df = df[df['Correo Electrónico'].apply(
    lambda x: bool(re.match(email_regex, x)) if pd.notna(x) else False
)]

# 5. **Eliminar registros con Pedidos inválidos** (Integridad)
df = df[df['Pedido Válido'] == "Válido"]

# 6. **Eliminar registros con Última Actualización mayor a 15 días** (Actualización)
df = df[df['Última Actualización (días)'] <= 15]

# 7. **Eliminar registros con Tiempo de Acceso mayor a 0.3 segundos** (Accesibilidad)
df = df[df['Tiempo Acceso (seg)'] <= 0.3]

# Mostrar el DataFrame limpio
print("Datos limpios:")
print(df)
