<?php
// Configuración de conexión
$servername = "mysql";
$username = "user";
$password = "password";
$dbname = "mydb";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Crear una tabla si no existe
$sql = "CREATE TABLE IF NOT EXISTS users (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50),
    reg_date TIMESTAMP
)";

if ($conn->query($sql) === TRUE) {
    echo "Tabla 'users' verificada o creada con éxito.<br>";
} else {
    echo "Error al crear la tabla: " . $conn->error;
}

// Insertar un registro
$sql = "INSERT INTO users (name, email) VALUES ('Juan Magan', 'john@example.com',)";
if ($conn->query($sql) === TRUE) {
    echo "Nuevo registro insertado con éxito.<br>";
} else {
    echo "Error al insertar registro: " . $conn->error;
}

// Mostrar las tablas de la base de datos
$sql = "SHOW TABLES";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "Tablas en la base de datos:<br>";
    while($row = $result->fetch_assoc()) {
        echo $row['Tables_in_mydb'] . "<br>";
    }
} else {
    echo "No se encontraron tablas.";
}

// Mostrar todos los usuarios
$sql = "SELECT id, name, email FROM users";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "<br>Usuarios registrados:<br>";
    while($row = $result->fetch_assoc()) {
        echo "ID: " . $row["id"]. " - Nombre: " . $row["name"]. " - Email: " . $row["email"]. "<br>";
    }
} else {
    echo "No se encontraron usuarios.";
}

// Cerrar conexión
$conn->close();
?>
