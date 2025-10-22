<?php
session_start(); // Iniciar sesión

$db = mysqli_connect('localhost', 'admin', '1234', 'mysitedb') or die('Fail');

if (!isset($_POST['new_comment']) || !isset($_POST['juego_id'])) {
    die('Datos incompletos');
}

$comentario = trim($_POST['new_comment']);
$juego_id = intval($_POST['juego_id']);

if ($comentario === '') {
    die('El comentario no puede estar vacío. <a href="detail.php?id='.$juego_id.'">Volver</a>');
}

// Escapar el comentario
$comentario_escaped = mysqli_real_escape_string($db, $comentario);

// Determinar el usuario_id
$usuario_id = isset($_SESSION['user_id']) ? intval($_SESSION['user_id']) : null;

// Construir la consulta
if (is_null($usuario_id)) {
    $query = "INSERT INTO tComentarios (comentario, juego_id, usuario_id) VALUES ('$comentario_escaped', $juego_id, NULL)";
} else {
    $query = "INSERT INTO tComentarios (comentario, juego_id, usuario_id) VALUES ('$comentario_escaped', $juego_id, $usuario_id)";
}

$result = mysqli_query($db, $query) or die('Error al insertar comentario: ' . mysqli_error($db));
$nuevo_id = mysqli_insert_id($db);
mysqli_close($db);
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Comentario añadido</title>
</head>
<body>
    <h2>Comentario añadido correctamente</h2>
    <p>Tu comentario ha sido añadido con el ID: <?php echo $nuevo_id; ?></p>
    <?php if (!is_null($usuario_id)): ?>
        <p>Comentario añadido como: <?php echo htmlspecialchars($_SESSION['email']); ?></p>
    <?php else: ?>
        <p>Comentario añadido como usuario anónimo</p>
    <?php endif; ?>
    <a href="detail.php?id=<?php echo $juego_id; ?>">Volver al juego</a>
</body>
</html>
