import pandas as pd
import numpy as np

# Crear dataset ficticio
data = {
    'ID_Batalla': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Nombre_Batalla': ['Abismo de Helm', 'Minas Tirith', 'Batalla de los Campos del Pelennor', 
                        'Batalla del Morannon', 'Batalla de Cuernavilla', 'Batalla de Lothlórien', 
                        'Batalla de Erebor', 'Batalla de Dale', 'Batalla de la Puerta Negra', 'Batalla de Bywater'],
    'Fecha': ['3019-03-03', '3019-03-15', '3019-03-15', '3019-03-25', '3019-03-03', 
              '3019-03-22', '3019-03-17', '3019-03-17', '3019-03-25', '03/11/3019'],  # Formato inconsistente
    'Lugar': ['Abismo de Helm', 'Minas Tirith', 'Campos del Pelennor', 'Morannon', 'Cuernavilla', 
              'Lothlórien', 'Erebor', 'Dale', 'Puerta Negra', 'Bywater'],
    'Bando': ['Comunidad del Anillo', 'Comunidad del Anillo', 'Comunidad del Anillo', 
              'Comunidad del Anillo', 'Comunidad del Anillo', 'Saurón', 'Sauron', 
              'Saruman', 'Saurón', 'Comunidad del Anillo'],  # Error tipográfico
    'Líder': ['Aragorn', 'Gandalf', 'Théoden', 'Aragorn', np.nan, np.nan, 'Sauron', 'Saruman', 'Sauron', 'Sam'],  # Valores faltantes
    'Bajas_Enemigas': [10000, 50000, -1000, 70000, 8000, 2000, 1000000, 4000, 5000, 100],  # Valor negativo y atípico
    'Bajas_Propias': [500, 2000, 3000, 4000, np.nan, 5000, 6000, 7000, 8000, 10],  # Valor faltante
    'Victoria': ['Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Tal vez', 'No', 'No', 'Sí'],  # Valor incorrecto
    'Anotaciones': ['Victoria decisiva', 'Derrota de Sauron', 'Derrota de los Nazgûl', 
                    'Destrucción del Anillo', 'Defensa exitosa', 'Ataque repelido', 
                    'Ataque repelido', 'Ataque repelido', 'Ataque repelido', 'Victoria en la Comarca']
}

df = pd.DataFrame(data)

# 1. Corrección de errores tipográficos en "Bando"
df['Bando'] = df['Bando'].replace({'Saurón': 'Sauron'})

# 2. Corrección del formato de la fecha, detectando diferentes formatos
from datetime import datetime

def parse_fecha(fecha):
    fecha = fecha.replace("/", "-")  # Reemplaza '/' por '-'
    formatos = ['%Y-%m-%d', '%m-%d-%Y', '%d-%m-%Y']  # Posibles formatos
    
    for fmt in formatos:
        try:
            return datetime.strptime(fecha, fmt).date()
        except ValueError:
            continue  # Si falla, intenta con otro formato
    
    # Devolver None si no se puede convertir y un print
    print("Error con fecha:", fecha)  
    return None

df['Fecha'] = df['Fecha'].apply(parse_fecha)

# 3. Manejo de valores faltantes en "Líder"
df['Líder'] = df['Líder'].fillna('Desconocido')

# 4. Corrección de valores negativos y atípicos en "Bajas_Enemigas"
mediana_bajas = df['Bajas_Enemigas'].median()

df['Bajas_Enemigas'] = df['Bajas_Enemigas'].abs()

# Si una cantidad de bajas es más del doble de la mediana, se reemplaza por la mediana
df.loc[df['Bajas_Enemigas'] > 2 * mediana_bajas, 'Bajas_Enemigas'] = mediana_bajas

# Si una cantidad de bajas es menos del 2.5% de la mediana, se reemplaza por la mediana
df.loc[df['Bajas_Enemigas'] < 0.025 * mediana_bajas, 'Bajas_Enemigas'] = mediana_bajas

# 5. Imputación de valores faltantes en "Bajas_Propias" con la mediana
mediana_bajas_propias = df['Bajas_Propias'].median()

df['Bajas_Propias'] = df['Bajas_Propias'].fillna(df['Bajas_Propias'].median())

df.loc[df['Bajas_Propias'] < 0.025 * mediana_bajas_propias, 'Bajas_Propias'] = mediana_bajas_propias

# 6. Normalización de valores en "Victoria"
df['Victoria'] = df['Victoria'].apply(lambda x: 'Sí' if x == 'Sí' else 'No')

print("Dataset limpio:")
print(df)