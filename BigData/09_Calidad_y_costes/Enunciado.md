# Evaluación de la Calidad de Datos y Análisis del Impacto Económico

## Objetivo
Implementar un análisis exhaustivo de la calidad de datos en un archivo CSV que contiene información de clientes. El análisis se enfocará en:
1. Identificar errores en distintas métricas de calidad.
2. Calcular el impacto económico asociado a cada métrica.
3. Representar los resultados visualmente mediante un gráfico de barras.

---

## Descripción del Archivo de Datos
El archivo `datosClientes.csv` contiene 1000 registros con información sobre clientes, incluyendo los siguientes campos:
- **Nombre**
- **Dirección**
- **Correo Electrónico**
- **Teléfono**
- **Pedido Válido** (valores posibles: "Válido" o "Inválido")
- **Última Actualización** (días)
- **Tiempo Acceso** (seg)

Este archivo presenta problemas de calidad que afectan la precisión y la eficiencia operativa.

---

## Métricas de Calidad Evaluadas
Se analizarán las siguientes métricas:

1. **Exactitud**:
   - Identificación de registros con errores en campos esenciales como **nombre** y **dirección**.
   - **Costo asociado**: 1000 €/error.

2. **Completitud**:
   - Detección de registros con datos faltantes en campos críticos (**nombre**, **dirección**, **correo electrónico**).
   - **Costo asociado**: 500 €/error.

3. **Consistencia**:
   - Verificación de que los números de teléfono cumplen con el formato estándar `+34 #########`.
   - **Costo asociado**: 2000 €/error.

4. **Validez**:
   - Validación de que los correos electrónicos tienen un formato correcto (e.g., `usuario@dominio.com`).
   - **Costo asociado**: 300 €/error.

5. **Integridad**:
   - Identificación de **pedidos** marcados como inválidos.
   - **Costo asociado**: 1500 €/error.

6. **Actualización**:
   - Detección de registros que no se han actualizado en más de 15 días.
   - **Costo asociado**: 1200 €/error.

7. **Accesibilidad**:
   - Identificación de registros con tiempos de acceso superiores a 0.3 segundos.
   - **Costo asociado**: 1000 €/error.

---

## Tareas a Realizar

### 1. Carga de Datos
- Leer el archivo `datosClientes.csv` usando la librería **Pandas**.

### 2. Análisis de Métricas de Calidad
- Implementar funciones y condiciones para detectar errores en cada métrica.
- Generar subconjuntos del DataFrame para identificar los registros problemáticos.

### 3. Cálculo del Impacto Económico
- Asignar costes específicos a los errores detectados en cada métrica.
- Calcular el coste total derivado de los problemas de calidad de datos.

### 4. Visualización de Resultados
- Crear un **gráfico de barras** que muestre el coste económico asociado a cada métrica.
- Personalizar el gráfico para facilitar la interpretación de los resultados.

---

## Reglas de Validación

### Teléfono
- Formato requerido: `+34 #########`.

### Correo Electrónico
- Formato estándar: `usuario@dominio.com`.

---

## Costes Asociados por Métrica

| **Métrica**       | **Costo por Error (€)** |
|--------------------|-------------------------|
| Exactitud          | 1000                   |
| Completitud        | 500                    |
| Consistencia       | 2000                   |
| Validez            | 300                    |
| Integridad         | 1500                   |
| Actualización      | 1200                   |
| Accesibilidad      | 1000                   |

---

## Entregables

### 1. Formato Markdown
- Documento en formato `Markdown.md` con la descripción completa de la práctica.

### 2. Código Python
- Un script **bien documentado** que implemente las tareas descritas.
- Uso de **comentarios** para explicar las validaciones realizadas.

### 3. Reporte de Resultados
- Resumen del impacto económico total.
- Detalle del coste asociado a cada métrica.

### 4. Visualización
- **Gráfico de barras** que muestre el impacto económico por métrica.

---

## Criterios de Evaluación

1. **Correcta implementación** de las validaciones.
2. **Precisión** en los cálculos de costes asociados.
3. **Claridad y personalización** del gráfico de barras.
4. **Documentación y limpieza** del código.
