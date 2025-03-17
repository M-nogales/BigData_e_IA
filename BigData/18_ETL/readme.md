# Fases de exploración recomendadas para un análisis de ventas

## 1. Exploración inicial del dataset

**Pregunta:** ¿Cuántas filas y columnas tiene el dataset? ¿Qué tipo de información contiene cada columna?
- Identificar las columnas y describir brevemente qué tipo de datos contienen (por ejemplo, segmento, país, producto, etc.).

## 2. Análisis descriptivo

**Pregunta:** ¿Cuáles son los valores estadísticos básicos (media, mediana, desviación estándar) para las columnas numéricas como "Units Sold", "Manufacturing Price", "Sale Price", "Gross Sales", "Discounts", "Sales", "COGS", y "Profit"?

- Calcular estas métricas para las columnas numéricas e interpretar los resultados.

## 3. Segmentación por categorías

**Pregunta:** ¿Cómo se distribuyen las ventas por segmento (Government, Midmarket, Channel Partners, etc.)? ¿Qué segmento tiene el mayor volumen de ventas?

- Agrupar los datos por segmento y calcular el total de ventas para cada uno. Luego, visualizar estos datos en un gráfico.

## 4. Análisis por país

**Pregunta:** ¿Qué país tiene el mayor volumen de ventas? ¿Y el menor?

- Agrupar los datos por país y calcular el total de ventas para cada uno. Luego, identificar el país con mayores y menores ventas.

## 5. Análisis temporal

**Pregunta:** ¿Cómo han evolucionado las ventas a lo largo del tiempo? ¿Hay algún mes o año en particular que destaque?

- Agrupar los datos por mes y año, y calcular las ventas totales para cada período. Luego, visualizar estos datos en un gráfico para observar tendencias.

## 6. Análisis de productos

**Pregunta:** ¿Qué producto tiene el mayor margen de beneficio? ¿Y el menor?

- Calcular el margen de beneficio para cada producto e identificar cuál tiene el mayor y menor margen.

## 7. Análisis de descuentos

**Pregunta:** ¿Cómo afectan los descuentos a las ventas y al beneficio? ¿Hay alguna relación entre el nivel de descuento y el volumen de ventas?

- Relación entre los descuentos y las ventas, e identificar si los descuentos más altos están asociados con mayores ventas o mayores beneficios.

## 8. Análisis de correlación

**Pregunta:** ¿Existe alguna correlación entre las diferentes variables numéricas, como "Units Sold", "Sale Price", y "Profit"?

- Calcular la matriz de correlación entre las variables numéricas e interpretar los resultados.

## 9. Visualización de datos

**Pregunta:** ¿Cómo podemos visualizar mejor la distribución de las ventas por producto y por país?

- Crear gráficos de dispersión, mapas de calor, o gráficos de barras apiladas para visualizar la distribución de las ventas por producto y por país.


# Resultados
## 1 Exploración inicial del dataset
```python
# Load the Excel file
file_path = "Financial_Sample.xlsx"  # Update with the correct file path
df = pd.read_excel(file_path)

# Display the first few rows
print(df.head())
print(df.info())
print(df.describe())
```

## 2 Análisis descriptivo
```python
print(df.describe())
```

## 3 Segmentación por Categorías
```python
# Group by Segment and sum the Sales
sales_by_segment = df.groupby('Segment')['Sales'].sum()

# Plot
plt.figure(figsize=(8, 5))
sales_by_segment.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Segment')
plt.xlabel('Segment')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

## 4 Análisis por país
```python
# Group by Country and sum the Sales
sales_by_country = df.groupby('Country')['Sales'].sum()

# Plot
plt.figure(figsize=(8, 5))
sales_by_country.plot(kind='bar', color='lightgreen')
plt.title('Total Sales by Country')
plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

## 5 Análisis temporal
```python
# Monthly Profit Trends by Year
plt.figure(figsize=(12, 6))
for year in df["Year"].unique():
    monthly_data = df[df["Year"] == year].groupby("Month Number")["Profit"].sum()
    plt.plot(monthly_data.index, monthly_data.values, marker="o", linestyle="-", label=str(year))

plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Monthly Profit Trends by Year")
plt.xticks(ticks=range(1, 13), labels=df["Month Name"].unique(), rotation=45)
plt.legend(title="Year")
plt.grid(True)
plt.show()
```

## 6 Análisis de productos
```python
# Group by Product and sum the Sales
sales_by_product = df.groupby('Product')['Sales'].sum()

# Plot
plt.figure(figsize=(8, 5))
sales_by_product.plot(kind='bar', color='orange')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

## 7 Análisis de descuentos
```python
# Group by Discount Band and sum the Sales
sales_by_discount = df.groupby('Discount Band')['Sales'].sum()

# Plot
plt.figure(figsize=(8, 5))
sales_by_discount.plot(kind='bar', color='purple')
plt.title('Total Sales by Discount Band')
plt.xlabel('Discount Band')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```
## 8 Análisis de correlación

## 9 Visualización de datos
```python
# Group by Product and sum the Sales
sales_by_product = df.groupby('Product')['Sales'].sum()

# Plot
plt.figure(figsize=(8, 5))
sales_by_product.plot(kind='bar', color='orange')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Group by Country and sum the Sales
sales_by_country = df.groupby('Country')['Sales'].sum()

# Plot
plt.figure(figsize=(8, 5))
sales_by_country.plot(kind='bar', color='lightgreen')
plt.title('Total Sales by Country')
plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

## 10. Conclusiones y recomendaciones

### Hallazgos clave:
- El segmento con mayores ventas es **Government**, seguido de **Small Business**.
- Los paises con mayores ventas son **Estados Unidos** y **Canada**, mientras que **México** tiene las ventas más bajas.
- Los meses de **septiembre y noviembre** tienen las ventas más altas.
- Existe una **correlación positiva fuerte** entre **Units Sold** y **Profit**, lo que sugiere que vender más unidades aumenta los beneficios.
- Los **descuentos altos** están asociados con **menores beneficios**, lo que indica que podrían no ser efectivos para aumentar la rentabilidad.

### Recomendaciones:
- **Enfocar esfuerzos de marketing** en el segmento **Government**, ya que es el que genera mayores ventas.
- Realizar **campañas específicas en México** para aumentar las ventas en ese mercado.