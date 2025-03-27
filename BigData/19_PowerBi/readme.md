# Consultas DAX en Power Bi

Estas consultas están diseñadas para analizar diferentes aspectos del comportamiento de ventas.

## Dataset Utilizado

**Archivo:** `retail_ecommerce_sales_dataset.csv`

## **Nota**
Al dataset entregado le falta el nombre del producto y el stock de cada uno

### 📌 Análisis General de Ventas (AV)

- Calcular el total de ventas en toda la base de datos.
- Determinar la cantidad total de transacciones realizadas.
- Calcular el promedio de ventas por transacción.
- Identificar el número total de clientes únicos.
- Obtener el total de productos vendidos.
- Calcular el ingreso promedio diario.
- Determinar el total de ventas por categoría de producto.
- Identificar el producto más vendido en términos de cantidad.
- Calcular el valor promedio de un carrito de compra.
- Determinar el día de mayor volumen de ventas.

### 📊 Análisis de Clientes y Comportamiento de Compra (AC)

- Contar el número de clientes recurrentes (con más de una compra).
- Calcular el gasto promedio por cliente.
- Identificar el cliente que más ha gastado en la tienda.
- Determinar el número de clientes que solo compraron una vez.
- Calcular el promedio de productos comprados por cliente.
- Determinar la frecuencia promedio de compra de los clientes.
- Identificar el país o región con más compras.
- Calcular la tasa de conversión (compras realizadas vs visitas a productos).
- Obtener la categoría de productos con más clientes únicos.
- Determinar la cantidad de carritos abandonados antes de la compra.

### 🏷 Análisis de Productos (AP)

- Obtener la lista de productos nunca vendidos.
- Calcular el precio promedio de los productos vendidos.
- Identificar el producto con mayor margen de ganancia.
- Calcular el promedio de ventas por producto.
- Determinar los productos más frecuentemente comprados juntos.
- Identificar el producto con más devoluciones.
- Calcular el stock promedio de los productos.
- Obtener el producto con la mayor variación de precios a lo largo del tiempo.
- Determinar el número de productos vendidos por categoría.
- Identificar los productos con mayores descuentos aplicados.

### 📅 Análisis Temporal (AT)

- Calcular el total de ventas por mes.
- Determinar el día de la semana con más ventas.
- Comparar el crecimiento de ventas entre diferentes meses.
- Obtener la hora del día con más transacciones.
- Calcular la temporada del año con más ventas.
- Determinar la diferencia de ventas entre días laborables y fines de semana.
- Analizar la tasa de crecimiento mensual de ingresos.
- Identificar el impacto de eventos o festividades en las ventas.
- Calcular el promedio de compras por día de la semana.
- Determinar si existe una tendencia estacional en las ventas.

### 📦 Análisis Logístico y de Inventario (ALI)

- Calcular el número total de productos en stock.
- Identificar los productos con menor inventario disponible.
- Determinar la rotación promedio de inventario por producto.
- Calcular el tiempo promedio entre reposiciones de productos.
- Analizar la eficiencia de la cadena de suministro en términos de tiempo de entrega.
- Obtener el porcentaje de pedidos con retraso en la entrega.
- Determinar el número de productos agotados en los últimos 30 días.
- Identificar las categorías con mayores problemas de disponibilidad.
- Comparar el stock actual con la demanda histórica para prever futuras compras.
- Analizar la frecuencia de pedidos de reposición de inventario por producto.

### 🧠 Análisis Complejo y Predictivo (ACP) -- Extra + 1 punto

- **Tasa de Conversión Mensual (Visitas a Compras):** Calcula la tasa de conversión de visitas a compras para cada mes, considerando solo los productos que fueron visitados y luego comprados.
- **Predicción de Ventas para el Próximo Mes (Tendencia Lineal):** Usa la regresión lineal (LINESTX) para predecir el total de ventas del próximo mes basado en tendencias pasadas.
- **Impacto de Descuentos en la Conversión de Ventas:** Mide el impacto de los descuentos en la tasa de conversión, comparando compras con y sin descuento.
- **Clientes Leales vs. Ocasionales:** Segmenta clientes en "leales" (más de 5 compras) y "ocasionales" (menos de 5 compras) según su historial de compras.
- **Productos con Mayor Tasa de Recompra:** Calcula qué productos son comprados repetidamente por los mismos clientes, midiendo la relación entre compras y clientes únicos.
- **Ventas Acumuladas Ajustadas por Crecimiento:** Calcula ventas acumuladas con ajuste de crecimiento anual basado en la tendencia histórica de ventas.
- **Análisis de Carritos Abandonados por Categoría:** Identifica la tasa de abandono de carritos para cada categoría de producto, comparando productos agregados al carrito vs. comprados.
- **Impacto de Festivos en Ventas:** Compara las ventas en días festivos frente a días normales para medir el efecto de fechas especiales en el rendimiento de la tienda.
- **Clientes con Mayor Potencial de Crecimiento:** Identifica clientes con tendencia de aumento en compras en los últimos 3 meses para enfocarse en estrategias de fidelización.
- **Previsión de Demanda por Producto:** Predice la demanda futura de productos basado en tendencias históricas utilizando análisis de regresión.

#### 📌 Entrega de Resultados

Se debe entregar:
- **Fichero Power BI** con todas las consultas implementadas.
- **Documento en Markdown** con todas las consultas DAX realizadas.

#### Formato de las Consultas DAX

Cada consulta DAX debe tener un nombre definido bajo el siguiente formato:

```
Número_Apartado_Nombre = ...
```

## Resultado


### 📌 Análisis General de Ventas (AV)

```
1_AV_Total_Ventas = SUM('retail_ecommerce_sales_stocking_dataset'[Total Amount])
```

```2_AV_Total_Transacciones = DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Transaction ID])
```

```
3_AV_Promedio_Venta_Transaccion = DIVIDE([1_AV_Total_Ventas], [2_AV_Total_Transacciones]) 
```
```
4_AV_Total_Clientes = DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Customer ID])
```

```
5_AV_Total_Productos_Vendidos = SUM('retail_ecommerce_sales_stocking_dataset'[Quantity])
```

```
6_AV_Ingreso_Promedio_Diario = 
VAR DiasUnicos = DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Date])
RETURN DIVIDE([1_AV_Total_Ventas], DiasUnicos)
```

```
7_AV_Total_Ventas_Por_Categoria = 
SUMX(
    VALUES('retail_ecommerce_sales_stocking_dataset'[Product Category]),
    CALCULATE([1_AV_Total_Ventas])
)
```

```
8_AV_Producto_Mas_Vendido = 

TOPN(
    1, 
    ALL('retail_ecommerce_sales_stocking_dataset'[Product]), 
    SUM('Global Superstore'[Sales]), 
    DESC
)
```

```
9_AV_Valor_Promedio_Carrito = DIVIDE([1_AV_Total_Ventas], [4_AV_Total_Clientes])
```

```
10_AV_Dia_Mayor_Ventas = TOPN(
        1, 
        ALL('retail_ecommerce_sales_stocking_dataset'[Date]), 
        CALCULATE(SUM('retail_ecommerce_sales_stocking_dataset'[Total Amount])), 
        DESC
    )
```

### 📊 Análisis de Clientes y Comportamiento de Compra (AC)

```
1_AC_Clientes_Recurrentes = 
CALCULATE(
    DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Customer ID]), 
    FILTER(
        VALUES('retail_ecommerce_sales_stocking_dataset'[Customer ID]), 
        CALCULATE(COUNT('retail_ecommerce_sales_stocking_dataset'[Transaction ID])) > 1
    )

)
```
```
2_AC_Gasto_Promedio_Cliente = DIVIDE([1_AV_Total_Ventas], [4_AV_Total_Clientes])
```
```
3_AC_Cliente_Top_Gasto = TOPN(
        1, 
        ALL('retail_ecommerce_sales_stocking_dataset'[Customer ID]), 
        CALCULATE(SUM('retail_ecommerce_sales_stocking_dataset'[Total Amount])), 
        DESC
    )
```

```
//todos los clientes han comprado por lo que el resultado es (En blanco)
4_AC_Clientes_Una_Compra = 
CALCULATE(
    DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Customer ID]), 
    FILTER(
        VALUES('retail_ecommerce_sales_stocking_dataset'[Customer ID]), 
        CALCULATE(COUNT('retail_ecommerce_sales_stocking_dataset'[Transaction ID])) = 1
    )
)
```

```
5_AC_Promedio_Productos_Cliente = 
DIVIDE(
    SUM('retail_ecommerce_sales_stocking_dataset'[Quantity]), 
    DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Customer ID]), 
    0
)
```

```
// el resultado siempre será 1 devido al dataset dado
-= 8_AC_Tasa_Conversion = 
DIVIDE(
    DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Customer ID]), 
    DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Transaction ID]), 
    0
)
```

```
9_AC_Categoria_Mas_Clientes_Unicos  = 
    TOPN(
        1, 
        ALL('retail_ecommerce_sales_stocking_dataset'[Product Category]), 
        CALCULATE(DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Customer ID])), 
        DESC
    )
```

### 🏷 Análisis de Productos (AP)

```
1_AP_Productos_No_Vendidos = 
CALCULATE(
    DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Product]), 
    FILTER(
        VALUES('retail_ecommerce_sales_stocking_dataset'[Product]), 
        CALCULATE(SUM('retail_ecommerce_sales_stocking_dataset'[stock])) = 0
    )
)
```

```
2_AP_Precio_Promedio_Productos = 
AVERAGE('retail_ecommerce_sales_stocking_dataset'[Price per Unit])
```

*3_AP_Producto_Mayor_Margen = ...*
3_AP_Producto_Mayor_Margen = 
    TOPN(
        1, 
        ALL('retail_ecommerce_sales_stocking_dataset'[Product]), 
        CALCULATE(AVERAGE('retail_ecommerce_sales_stocking_dataset'[Profit Margin])), // aka calc margin
        DESC
    )

```
4_AP_Promedio_Ventas_Producto = 
DIVIDE(
    SUM('retail_ecommerce_sales_stocking_dataset'[Total Amount]), 
    DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Product]), 
    0
)
```

```
7_AP_Stock_Promedio = 
AVERAGE('retail_ecommerce_sales_stocking_dataset'[Stock])
```

```
8_AP_Producto_Mayor_Variacion_Precio = 
    TOPN(
        1, 
        ALL('retail_ecommerce_sales_stocking_dataset'[Product]), 
        CALCULATE(MAX('retail_ecommerce_sales_stocking_dataset'[Price per Unit]) - MIN('retail_ecommerce_sales_stocking_dataset'[Price per Unit])), 
        DESC
    )
```

```
9_AP_Productos_Por_Categoria = 
COUNTROWS(
    DISTINCT('retail_ecommerce_sales_stocking_dataset'[Product])
)
```

### 📅 Análisis Temporal (AT)
```
1_AT_Ventas_Por_Mes = 
TOTALMTD(
    SUM('retail_ecommerce_sales_stocking_dataset'[Total Amount]),
    'retail_ecommerce_sales_stocking_dataset'[date]
)
```

```
2_AT_Dia_Semana_Mas_Ventas = 
VAR DMaxVentas = 
MAXX(
    VALUES('retail_ecommerce_sales_stocking_dataset'[dia]),
     [1_AV_Total_Ventas]
     )
RETURN
    CALCULATE(
        FIRSTNONBLANK('retail_ecommerce_sales_stocking_dataset'[dia], 1),
        FILTER(
            VALUES('retail_ecommerce_sales_stocking_dataset'[dia]),
            [1_AV_Total_Ventas] = DMaxVentas
        )
    )
```
```
3_AT_Crecimiento_Ventas_Mensual = 
VAR VentasMesAnterior = 
    CALCULATE(
        TOTALMTD(SUM('retail_ecommerce_sales_stocking_dataset'[Quantity]), 
        'retail_ecommerce_sales_stocking_dataset'[Date]),
        DATEADD('retail_ecommerce_sales_stocking_dataset'[Date], -1, MONTH)
    )
VAR VentasMesActual = 
    TOTALMTD(SUM('retail_ecommerce_sales_stocking_dataset'[Quantity]), 
    'retail_ecommerce_sales_stocking_dataset'[Date])
RETURN
    DIVIDE(VentasMesActual - VentasMesAnterior, VentasMesAnterior, 0)
```


```
5_AT_Temporada_Alta_Ventas = 
TOPN(
        1,
        ALL('retail_ecommerce_sales_stocking_dataset'[Date]),
        CALCULATE(SUM('retail_ecommerce_sales_stocking_dataset'[Total Amount])),
        DESC
    )
```

```
6_AT_Ventas_Laborables_vs_Finde = 
VAR weekday_sales = CALCULATE([1_AV_Total_Ventas], 'retail_ecommerce_sales_stocking_dataset'[dia] <= 5)
VAR weekend_sales = CALCULATE([1_AV_Total_Ventas], 'retail_ecommerce_sales_stocking_dataset'[dia] > 5)
RETURN
    "Laborables: " & FORMAT(weekday_sales, "#,##0") & 
    " | Fin semana: " & FORMAT(weekend_sales, "#,##0") &
    " | Diferencia: " & FORMAT(weekday_sales - weekend_sales, "#,##0") &
    " (" & IF(weekend_sales > 0, 
              FORMAT((weekday_sales/weekend_sales)-1, "0%"), 
              "N/A") & ")"
```

```
7_AT_Tasa_Crecimiento_Mensual = 
VAR VentasMesAnterior = 
    CALCULATE(
        TOTALMTD(SUM('retail_ecommerce_sales_stocking_dataset'[Total Amount]), 'retail_ecommerce_sales_stocking_dataset'[Date]),
        DATEADD('retail_ecommerce_sales_stocking_dataset'[Date], -1, MONTH)
    )
RETURN
    DIVIDE([1_AT_Ventas_Por_Mes] - VentasMesAnterior, VentasMesAnterior, 0)
```

```
8_AT_Impacto_Eventos_Ventas = [Media ventas Semana Santa] - [Media de ventas]
```

```
9_AT_Promedio_Compras_Por_Dia_Semana = 
AVERAGEX(
    SUMMARIZE(
        'retail_ecommerce_sales_stocking_dataset',
        'retail_ecommerce_sales_stocking_dataset'[Date],
        "CantidadDiaria", SUM('retail_ecommerce_sales_stocking_dataset'[Quantity])
    ),
    [CantidadDiaria]
)
```

*10_AT_Tendencia_Estacional = ...*
```
Media de ventas = AVERAGE('retail_ecommerce_sales_stocking_dataset'[Quantity])

Media ventas Semana Santa = 
VAR Fecha_Inicio_SemanaSanta = DATE(2023, 4, 2)  // Ejemplo: Domingo de Ramos 2023
VAR Fecha_Fin_SemanaSanta = DATE(2023, 4, 9)    // Ejemplo: Domingo de Resurrección 2023
VAR VentasSemanaSanta = 
    CALCULATE(
        SUM('retail_ecommerce_sales_stocking_dataset'[Quantity]),
        DATESBETWEEN(
            'retail_ecommerce_sales_stocking_dataset'[Date],
            Fecha_Inicio_SemanaSanta,
            Fecha_Fin_SemanaSanta
        )
    )
VAR DiasSemanaSanta = 
    DATEDIFF(Fecha_Inicio_SemanaSanta, Fecha_Fin_SemanaSanta, DAY) + 1
RETURN
    DIVIDE(VentasSemanaSanta, DiasSemanaSanta)
```

### 📦 Análisis Logístico y de Inventario (ALI)
```
1_ALI_Total_Stock = SUM('retail_ecommerce_sales_stocking_dataset'[Stock])
```

```
2_ALI_Productos_Bajo_Stock = 
VAR RankedProducts = 
    ADDCOLUMNS(
        VALUES('retail_ecommerce_sales_stocking_dataset'[Product]),
        "StockTotal", CALCULATE(SUM('retail_ecommerce_sales_stocking_dataset'[Stock])),
        "Rank", RANKX(ALL('retail_ecommerce_sales_stocking_dataset'[Product]), CALCULATE(SUM('retail_ecommerce_sales_stocking_dataset'[Stock])),, ASC)
    )

VAR MinStockProducts = FILTER(RankedProducts, [Rank] = 1)

RETURN
    CONCATENATEX(MinStockProducts, 'retail_ecommerce_sales_stocking_dataset'[Product], ", ")
 ```

 ```
8_ALI_Categorias_Problemas_Stock = 
VAR RankedCategories = 
    ADDCOLUMNS(
        VALUES('retail_ecommerce_sales_stocking_dataset'[Product Category]),
        "StockTotal", CALCULATE(SUM('retail_ecommerce_sales_stocking_dataset'[Stock])),
        "Rank", RANKX(ALL('retail_ecommerce_sales_stocking_dataset'[Product Category]), CALCULATE(SUM('retail_ecommerce_sales_stocking_dataset'[Stock])),, ASC)
    )

VAR MinStockCategories = FILTER(RankedCategories, [Rank] = 1)

RETURN
    CONCATENATEX(MinStockCategories, 'retail_ecommerce_sales_stocking_dataset'[Product Category], ", ")
```

### 🧠 Análisis Complejo y Predictivo (ACP)
```
Pendiente = 
VAR N = COUNTROWS('retail_ecommerce_sales_stocking_dataset')  -- Número de puntos
VAR FechaMinima = MIN('retail_ecommerce_sales_stocking_dataset'[Date])  -- La fecha más antigua en los datos
VAR SumaX = SUMX('retail_ecommerce_sales_stocking_dataset', DATEDIFF(FechaMinima, 'retail_ecommerce_sales_stocking_dataset'[Date], MONTH))  -- Suma de X (número de meses desde la fecha mínima)
VAR SumaY = SUMX('retail_ecommerce_sales_stocking_dataset', 'retail_ecommerce_sales_stocking_dataset'[Total Amount])  -- Suma de Y (total de ventas)
VAR SumaXY = SUMX('retail_ecommerce_sales_stocking_dataset', DATEDIFF(FechaMinima, 'retail_ecommerce_sales_stocking_dataset'[Date], MONTH) * 'retail_ecommerce_sales_stocking_dataset'[Total Amount])  -- Suma de X*Y
VAR SumaX2 = SUMX('retail_ecommerce_sales_stocking_dataset', DATEDIFF(FechaMinima, 'retail_ecommerce_sales_stocking_dataset'[Date], MONTH) ^ 2)  -- Suma de X^2

RETURN
    (N * SumaXY - SumaX * SumaY) / (N * SumaX2 - SumaX ^ 2)
```

```
Interseccion = 
VAR N = COUNTROWS('retail_ecommerce_sales_stocking_dataset')  -- Número de puntos
VAR FechaMinima = MIN('retail_ecommerce_sales_stocking_dataset'[Date])  -- La fecha más antigua en los datos
VAR SumaX = SUMX('retail_ecommerce_sales_stocking_dataset', DATEDIFF(FechaMinima, 'retail_ecommerce_sales_stocking_dataset'[Date], MONTH))  -- Suma de X
VAR SumaY = SUMX('retail_ecommerce_sales_stocking_dataset', 'retail_ecommerce_sales_stocking_dataset'[Total Amount])  -- Suma de Y (total de ventas)
VAR Pendiente = [Pendiente]  -- Pendiente calculada previamente

RETURN
    (SumaY - Pendiente * SumaX) / N
```

```
2_ACP_Prediccion_Ventas_Lineal = 
VAR UltimoMes = DATEDIFF(MINX(ALL('retail_ecommerce_sales_stocking_dataset'), 'retail_ecommerce_sales_stocking_dataset'[Date]), MAX('retail_ecommerce_sales_stocking_dataset'[Date]), MONTH) + 1
VAR Pendiente = [Pendiente]  -- Pendiente calculada previamente
VAR Interseccion = [Interseccion]  -- Intersección calculada previamente

RETURN
    (UltimoMes * Pendiente) + Interseccion
```