# Calidad de los Datos en la Tierra Media

## Contexto
Eres un archivista de la Biblioteca de Minas Tirith, encargado de mantener y analizar los registros de las batallas y eventos ocurridos durante la Guerra del Anillo. Recientemente, se ha recibido un dataset con información sobre las batallas, los participantes, las bajas y otros detalles relevantes. Sin embargo, el dataset contiene múltiples problemas de calidad que deben ser resueltos antes de poder utilizarlo para el análisis estratégico.

## Dataset: Batallas de la Guerra del Anillo
El dataset contiene las siguientes columnas:

- **ID_Batalla**: Identificador único de la batalla.  
- **Nombre_Batalla**: Nombre de la batalla (ejemplo: "La Batalla del Abismo de Helm").  
- **Fecha**: Fecha en la que ocurrió la batalla (en formato `YYYY-MM-DD`).  
- **Lugar**: Lugar donde se llevó a cabo la batalla (ejemplo: "Abismo de Helm", "Minas Tirith").  
- **Bando**: Bando principal involucrado (ejemplo: "Comunidad del Anillo", "Sauron", "Saruman").  
- **Líder**: Líder del bando (ejemplo: "Aragorn", "Sauron", "Saruman").  
- **Bajas_Enemigas**: Número de bajas enemigas reportadas.  
- **Bajas_Propias**: Número de bajas propias reportadas.  
- **Victoria**: Indica si el bando ganó la batalla (valores: "Sí", "No").  
- **Anotaciones**: Notas adicionales sobre la batalla.  

## Problemas de Calidad en el Dataset
- **Valores faltantes**: Algunas celdas están vacías en columnas críticas como `Bajas_Enemigas`, `Bajas_Propias` y `Líder`.  
- **Inconsistencias**: Hay errores tipográficos en la columna `Bando` (ejemplo: "Sauron" escrito como "Saurón").  
- **Valores atípicos**: Algunas batallas tienen un número de bajas extremadamente alto o bajo en comparación con el resto.  
- **Errores de formato**: La columna `Fecha` contiene fechas en formatos inconsistentes (ejemplo: "3019-03-15" vs "15/03/3019").  

## Reglas de negocio
- La columna `Victoria` solo puede contener los valores "Sí" o "No".  
- La columna `Bajas_Enemigas` y `Bajas_Propias` no pueden ser negativas.  
- La columna `Lugar` debe contener solo lugares conocidos de la Tierra Media.  

## Instrucciones para los archivistas
1. Identifica los problemas de calidad en el dataset.  
2. Aplica las técnicas de limpieza de datos para corregir los problemas:  
   - Valores faltantes.  
   - Inconsistencias y errores tipográficos.  
   - Valores atípicos.  
   - Errores de formato.  
   - Reglas de negocio.  
3. Documenta los cambios realizados y justifica las decisiones tomadas.  

---

## Código en Python para visualizar el dataset con problemas de calidad

```python
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

# Mostrar dataset con problemas de calidad
print("Dataset con problemas de calidad:")
print(df)
```

# Informe de calidad

## 1. Corrección de errores tipográficos en la columna **"Bando"**

### Cambio realizado
- El valor `'Saurón'` se corrigió a `'Sauron'` para garantizar la uniformidad en los valores.

```python
df['Bando'] = df['Bando'].replace({'Saurón': 'Sauron'})
```

## 2. Corrección del formato de la columna **"Fecha"**

### Cambio realizado
- Se estandarizó el formato de las fechas, que originalmente tenía varios estilos, a un único formato consistente (`YYYY-MM-DD`). Los valores con formato inconsistente, como `'03/11/3019'`, fueron convertidos correctamente a `3019-03-11`.

```python
def parse_fecha(fecha):
    fecha = fecha.replace("/", "-")  # Reemplaza '/' por '-'
    formatos = ['%Y-%m-%d', '%m-%d-%Y', '%d-%m-%Y']  # Posibles formatos
    for fmt in formatos:
        try:
            return datetime.strptime(fecha, fmt).date()
        except ValueError:
            continue  # Si falla, intenta con otro formato
    return None
df['Fecha'] = df['Fecha'].apply(parse_fecha)
```

## 3. Manejo de valores faltantes en la columna **"Líder"**

### Cambio realizado
- Los valores faltantes en la columna `Líder` fueron reemplazados por la palabra `'Desconocido'`.

```python
df['Líder'] = df['Líder'].fillna('Desconocido')
```
### Justificación
Los valores faltantes en la columna Líder pueden generar dificultades al analizar quién fue el líder en ciertas batallas. En lugar de dejar estos valores vacíos, se reemplazaron por ``Desconocido``.

Aquí tienes el markdown actualizado con las modificaciones solicitadas:

## 4. Corrección de valores negativos y atípicos en la columna **"Bajas_Enemigas"**

### Cambio realizado
- Los valores negativos fueron convertidos a positivos utilizando la función `abs()`.
- Los valores excesivamente altos (más del doble de la mediana) fueron reemplazados por el valor medio de la columna.
- Los valores extremadamente bajos (menos del 2.5% de la mediana) también fueron reemplazados por la mediana para evitar distorsiones.

```python
mediana_bajas = df['Bajas_Enemigas'].median()  # Calculamos la mediana
df['Bajas_Enemigas'] = df['Bajas_Enemigas'].abs()  # Convierte los valores negativos en positivos

# Si una cantidad de bajas es más del doble de la mediana, se reemplaza por la mediana
df.loc[df['Bajas_Enemigas'] > 2 * mediana_bajas, 'Bajas_Enemigas'] = mediana_bajas

# Si una cantidad de bajas es menos del 2.5% de la mediana, se reemplaza por la mediana
df.loc[df['Bajas_Enemigas'] < 0.025 * mediana_bajas, 'Bajas_Enemigas'] = mediana_bajas
```

### Justificación
Los valores negativos en la columna de **Bajas_Enemigas** no tienen sentido, ya que las bajas no pueden ser un número negativo. Además, algunos valores eran excesivamente altos y podrían ser errores tipográficos o registros atípicos. Para evitar que estos valores extremos afectaran el análisis, se reemplazaron por el valor de la mediana de la columna.

## 5. Imputación de valores faltantes en la columna **"Bajas_Propias"**

### Cambio realizado
- Los valores faltantes en la columna `Bajas_Propias` fueron reemplazados por la mediana de la columna.
- Los valores extremadamente bajos (menos del 2.5% de la mediana) también fueron reemplazados por la mediana para evitar distorsiones.

```python
mediana_bajas_propias = df['Bajas_Propias'].median()

# Imputación de valores faltantes
df['Bajas_Propias'] = df['Bajas_Propias'].fillna(df['Bajas_Propias'].median())

# Si una cantidad de bajas es menos del 2.5% de la mediana, se reemplaza por la mediana
df.loc[df['Bajas_Propias'] < 0.025 * mediana_bajas_propias, 'Bajas_Propias'] = mediana_bajas_propias
```

### Justificación
En este caso, Los valores extremadamente bajos fueron corregidos de forma similar a las bajas enemigas, ya que podrían ser errores de captura o registros anómalos. De este modo, se mantiene la integridad del análisis.

## 6. Normalización de los valores en la columna **"Victoria"**
### Cambio realizado
- Los valores en la columna `Victoria` fueron normalizados a `'Sí'` o `'No'`. Si el valor original era `'Sí'`, se mantuvo igual; en cualquier otro caso (por ejemplo, `'Tal vez'`), se reemplazó por `'No'`.

```python
df['Victoria'] = df['Victoria'].apply(lambda x: 'Sí' if x == 'Sí' else 'No')
```