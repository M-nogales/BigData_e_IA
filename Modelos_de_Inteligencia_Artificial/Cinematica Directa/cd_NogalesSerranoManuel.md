# Ejecución del código y resultados

## Capturas de pantalla y comentarios

resultados de la ejecución del código en Python para distintos valores de los ángulos del brazo robótico:

### Configuración 1: (θ1 = 0°, θ2 = 0°)
**Salida:** Posición: (x=8.00, y=0.00)

### Configuración 2: (θ1 = 45°, θ2 = 30°)
**Salida:** Posición: (x=4.31, y=6.43)

### Configuración 3: (θ1 = 90°, θ2 = -45°)
**Salida:** Posición: (x=2.12, y=7.12)

### Configuración 4: (θ1 = 180°, θ2 = 90°)
**Salida:** Posición: (x=-5.00, y=-3.00)

---

# Explicación: ¿Qué es una matriz de transformación homogénea?

Una matriz de transformación homogénea es una matriz 4 x 4  que se usa en robótica y gráficos computacionales para representar rotaciones y traslaciones en un espacio tridimensional de manera compacta. Su estructura general es:

<!-- lo de abajo en LateX queda mejor -->
<!-- \[
T = \begin{bmatrix} R & t \\ 0 & 1 \end{bmatrix}
\] -->

|Columna 1|Columna 2|
|---------|---------|
|  ( R )  |  ( t )  |
|  ( 0 )  |  ( 1 )  |

Donde:
- ( R ) es una submatriz ( 3 x 3 ) que representa la rotación.
- ( t ) es un vector ( 3 x 1 ) que representa la traslación.
- La última fila permite mantener la estructura homogénea y facilitar las operaciones matemáticas.

En el contexto de la cinemática directa, estas matrices se encadenan para obtener la posición final del efector del robot mediante la multiplicación sucesiva de las matrices de transformación de cada eslabón.