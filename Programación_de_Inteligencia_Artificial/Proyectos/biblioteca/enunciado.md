# PROYECTO: Biblioteca

Se requiere crear una aplicación para la gestión de una biblioteca comarcal. La aplicación será utilizada por un único usuario, por lo que no hay que realizar módulo de acceso (login y permisos).

## Funcionalidades principales

La aplicación deberá realizar las siguientes operaciones:

### 1. Gestión de libros
Se deberá tener un registro de los libros almacenados en la biblioteca, así como realizar operaciones de alta, baja y modificación de los datos de los libros, además de un listado general de los libros.

### 2. Gestión de usuarios
Para poder acceder a los préstamos, previamente el usuario deberá estar dado de alta en el sistema. Para ello, es necesario disponer de la opción de alta, baja, modificación de usuarios, así como de la posibilidad de generar un listado con los usuarios del sistema.

### 3. Gestión de préstamos
Esta es la funcionalidad principal de la aplicación. Se debe realizar el préstamo de un libro a un usuario dado de alta, así como la propia devolución. Es importante tener en cuenta las fechas y el objeto de préstamo.

### 4. Listados de préstamos pendientes
La aplicación debe ser fácil de usar y de mantener, siendo la interacción a través de línea de comandos. Todos los datos se almacenarán en diversos ficheros en el sistema local.

## Menú principal

1. Gestión Libros
2. Gestión Usuarios
3. Registrar Préstamo
4. Registrar Devolución
5. Listados de Préstamos
6. Salir

## Proyecto Python

Se deberá utilizar como base las siguientes clases:

### Clase LIBRO
- **Atributos**:
  - `ID_libro`
  - `titulo`
  - `autor`
  - `anyo`
  - `n_pags`
  - `genero`
  - `editorial`
  - `estado`
  - `disponible`

### Clase USUARIO
- **Atributos**:
  - `id_usuario`
  - `nombre`
  - `apellidos`
  - `dni`
  - `correo_e`
  - `tlfno`
  - `dirección`
  - `edad`

### Clase PRESTAMO
- **Atributos**:
  - `id_prestamo`
  - `id_usuario`
  - `idlibro`
  - `fecha_inicio`
  - `fecha_fin`
  - `fecha_devolucion`

## Ficheros

Cada entidad deberá estar guardada en un fichero independiente en formato CSV:

- **Usuarios**: `biblioUsuarios.csv`
- **Libros**: `biblioLibros.csv`
- **Préstamos**: `biblioPrestamos.csv`

## Requisitos

Generar la aplicación en Python que realice la gestión completa de la Biblioteca, incluyendo la gestión de préstamos de los libros.

### Estructura
- Estructurar el código.
- Incluir comentarios de código.
- Gestionar los ficheros asociados.
