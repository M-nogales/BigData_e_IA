# Documentacion

# Resumen de cada modulo

# Books.py

Este script de Python define la clase `Book` con atributos: título, autor, año, número de páginas, género, editorial, estado, disponibilidad y cantidad.
Además, de lo siguiente metodos:

- `_crear_id_libro`: Genera un nuevo ID para un libro.
- `añadir_libro`: Añade un nuevo libro a la base de datos.
- `borrar_libro`: Elimina un libro de la base de datos por su ID.
- `modificar_libro`: Modifica los detalles de un libro existente.
- `buscar_libro`: Busca un libro por su ID y muestra sus detalles.
- `listar_libros`: Lista todos los libros en la base de datos.
- `aumentar_disminuir_cantidad`: Aumenta o disminuye la cantidad de un libro específico.

## Loans.py

Este script de Python define una clase `Loan` con atributos: ID del préstamo, ID del libro, ID del usuario, fecha de inicio del préstamo, fecha de finalización y estado del préstamo.
Además, de lo siguiente metodos:

- `crear_prestamo`: Crea un nuevo préstamo y lo añade a la base de datos.
- `finalizar_prestamo`: Marca un préstamo como finalizado.
- `buscar_prestamo`: Busca un préstamo por su ID y muestra sus detalles.
- `listar_prestamos`: Lista todos los préstamos en la base de datos.
- `prestamos_activos`: Lista todos los préstamos que están actualmente activos.

## Users.py

Este script de Python define la clase `User` con atributos: nombre, edad, DNI, correo electrónico, teléfono y dirección.
Además, proporciona los siguientes métodos:

- `crear_id_usuario`: Genera un nuevo ID para un usuario.
- `añadir_usuario`: Añade un nuevo usuario a la base de datos.
- `borrar_usuario`: Elimina un usuario de la base de datos por su ID.
- `modificar_usuario`: Modifica los detalles de un usuario existente.
- `buscar_usuario`: Busca un usuario por su ID y muestra sus detalles.
- `listar_usuarios`: Lista todos los usuarios en la base de datos.## validations.py
## submenus.py

Este script contiene los bucles y llamadas a validaciones de todas las opciones del proyecto

## validations.py

Este script contiene las validaciones de todos los inputs del proyecto

# Como iniciarlo correctamente
Para inicializar este proyecto correctamente unicamente tendremos que ejecutar el file ``main.py`` estando nuestra `terminal dentro de la carpeta biblioteca`
