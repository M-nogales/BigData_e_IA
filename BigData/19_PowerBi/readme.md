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
1_AV_Total_Ventas = SUM('retail_ecommerce_sales_stocking_dataset'[Total Amount])2_AV_Total_Transacciones = DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Transaction ID])
3_AV_Promedio_Venta_Transaccion = DIVIDE([1_AV_Total_Ventas], [2_AV_Total_Transacciones]) 
4_AV_Total_Clientes = DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Customer ID])
5_AV_Total_Productos_Vendidos = SUM('retail_ecommerce_sales_stocking_dataset'[Quantity])
6_AV_Ingreso_Promedio_Diario = 
VAR DiasUnicos = DISTINCTCOUNT('retail_ecommerce_sales_stocking_dataset'[Date])
RETURN DIVIDE([1_AV_Total_Ventas], DiasUnicos)
7_AV_Total_Ventas_Por_Categoria = 
SUMX(
    VALUES('retail_ecommerce_sales_stocking_dataset'[Product Category]),
    CALCULATE([1_AV_Total_Ventas])
)
8_AV_Producto_Mas_Vendido = ...  
9_AV_Valor_Promedio_Carrito = ...  
10_AV_Dia_Mayor_Ventas = ...  

### 📊 Análisis de Clientes y Comportamiento de Compra (AC)
1_AC_Clientes_Recurrentes = ...  
2_AC_Gasto_Promedio_Cliente = ...  
3_AC_Cliente_Top_Gasto = ...  
4_AC_Clientes_Una_Compra = ...  
5_AC_Promedio_Productos_Cliente = ...  
6_AC_Frecuencia_Compra_Promedio = ...  
7_AC_Pais_Mas_Compras = ...  
8_AC_Tasa_Conversion = ...  
9_AC_Categoria_Mas_Clientes_Unicos = ...  
10_AC_Carritos_Abandonados = ...  

### 🏷 Análisis de Productos (AP)
1_AP_Productos_No_Vendidos = ...  
2_AP_Precio_Promedio_Productos = ...  
3_AP_Producto_Mayor_Margen = ...  
4_AP_Promedio_Ventas_Producto = ...  
5_AP_Productos_Comprados_Juntos = ...  
6_AP_Producto_Mas_Devoluciones = ...  
7_AP_Stock_Promedio = ...  
8_AP_Producto_Mayor_Variacion_Precio = ...  
9_AP_Productos_Por_Categoria = ...  
10_AP_Productos_Mayores_Descuentos = ...  

### 📅 Análisis Temporal (AT)
1_AT_Ventas_Por_Mes = ...  
2_AT_Dia_Semana_Mas_Ventas = ...  
3_AT_Crecimiento_Ventas_Mensual = ...  
4_AT_Hora_Pico_Transacciones = ...  
5_AT_Temporada_Alta_Ventas = ...  
6_AT_Ventas_Laborables_vs_Finde = ...  
7_AT_Tasa_Crecimiento_Mensual = ...  
8_AT_Impacto_Eventos_Ventas = ...  
9_AT_Promedio_Compras_Dia_Semana = ...  
10_AT_Tendencia_Estacional = ...  

### 📦 Análisis Logístico y de Inventario (ALI)
1_ALI_Total_Stock = ...  
2_ALI_Productos_Bajo_Stock = ...  
3_ALI_Rotacion_Inventario = ...  
4_ALI_Tiempo_Promedio_Reposicion = ...  
5_ALI_Eficiencia_Cadena_Suministro = ...  
6_ALI_Pedidos_Retrasados = ...  
7_ALI_Productos_Agotados_30d = ...  
8_ALI_Categorias_Problemas_Stock = ...  
9_ALI_Stock_vs_Demanda_Historica = ...  
10_ALI_Frecuencia_Reposicion = ...  

### 🧠 Análisis Complejo y Predictivo (ACP)
1_ACP_Tasa_Conversion_Mensual = ...  
2_ACP_Prediccion_Ventas_Lineal = ...  
3_ACP_Impacto_Descuentos_Conversion = ...  
4_ACP_Segmentacion_Clientes_Leales = ...  
5_ACP_Productos_Recompra = ...  
6_ACP_Ventas_Acumuladas_Ajustadas = ...  
7_ACP_Abandono_Carrito_Por_Categoria = ...  
8_ACP_Impacto_Festivos_Ventas = ...  
9_ACP_Clientes_Potencial_Crecimiento = ...  
10_ACP_Prevision_Demanda_Productos = ...  
