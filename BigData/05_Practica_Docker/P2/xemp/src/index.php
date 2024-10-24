<?php
// Parámetros de conexión a la base de datos
$host = 'mysql'; // Nombre del servicio MySQL en Docker Compose
$db   = 'mydb';
$user = 'user';
$pass = 'userpass';
$charset = 'utf8mb4';

// DSN (Data Source Name) para la conexión
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    // Conectar a la base de datos usando PDO
    $pdo = new PDO($dsn, $user, $pass, $options);
    echo "Conexión exitosa a la base de datos.<br>";
} catch (\PDOException $e) {
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

// Crear la tabla 'usuarios' si no existe
$createTableQuery = "
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL
    )
";

$pdo->exec($createTableQuery);
echo "Tabla 'usuarios' verificada o creada correctamente.<br>";

// Si el formulario ha sido enviado, insertamos los datos en la tabla
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nombre = $_POST['nombre'] ?? '';
    $email = $_POST['email'] ?? '';

    if (!empty($nombre) && !empty($email)) {
        $stmt = $pdo->prepare('INSERT INTO usuarios (nombre, email) VALUES (?, ?)');
        $stmt->execute([$nombre, $email]);
        echo "Datos insertados correctamente.<br>";
    } else {
        echo "Por favor, completa todos los campos.<br>";
    }
}

// Consultar los datos existentes
$stmt = $pdo->query('SELECT * FROM usuarios');
$usuarios = $stmt->fetchAll();

?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Usuario</title>
</head>
<body>
    <h1>Insertar Usuario</h1>
    <form action="index.php" method="post">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <input type="submit" value="Enviar">
    </form>

    <h2>Usuarios Registrados</h2>
    <ul>
        <?php foreach ($usuarios as $usuario): ?>
            <li><?php echo htmlspecialchars($usuario['nombre']) . " - " . htmlspecialchars($usuario['email']); ?></li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
