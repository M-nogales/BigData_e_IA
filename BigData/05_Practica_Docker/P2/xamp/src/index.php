<?php
// Configuración de la conexión a la base de datos
$servername = "mysql"; // Nombre del servicio del contenedor MySQL
$username = "user";
$password = "userpass";
$dbname = "mydb";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Comprobar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
echo "Conexión exitosa a la base de datos.<br>";

// Crear la tabla 'usuarios' si no existe
$createTable = "CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
)";
if ($conn->query($createTable) === TRUE) {
    echo "Tabla 'usuarios' creada o ya existe.<br>";
} else {
    echo "Error al crear la tabla: " . $conn->error;
}

// Insertar datos en la tabla si está vacía
$checkData = "SELECT COUNT(*) as count FROM usuarios";
$result = $conn->query($checkData);
$row = $result->fetch_assoc();

if ($row['count'] == 0) {
    $insertData = "INSERT INTO usuarios (nombre) VALUES ('Alice'), ('Bob'), ('Charlie')";
    if ($conn->query($insertData) === TRUE) {
        echo "Datos insertados en la tabla 'usuarios'.<br>";
    } else {
        echo "Error al insertar datos: " . $conn->error;
    }
}

// Realizar una consulta para seleccionar todos los registros de la tabla 'usuarios'
$sql = "SELECT * FROM usuarios";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Salida de los datos de cada fila
    while($row = $result->fetch_assoc()) {
        echo "ID: " . $row["id"] . " - Nombre: " . $row["nombre"] . "<br>";
    }
} else {
    echo "0 resultados";
}

// Cerrar conexión
$conn->close();
?>
