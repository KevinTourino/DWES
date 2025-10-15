<?php
$db = mysqli_connect('localhost', 'admin', '1234', 'mysitedb') or die('Fail');

if (!isset($_POST['new_comment']) || !isset($_POST['juego_id'])) {
    die('Datos incompletos');
}

$comentario = $_POST['new_comment'];
$juego_id = intval($_POST['juego_id']);

if (trim($comentario) == '') {
    die('El comentario no puede estar vacío. <a href="detail.php?id='.$juego_id.'">Volver</a>');
}


$query = "INSERT INTO tComentarios (comentario, juego_id, usuario_id) VALUES ('".$comentario."', ".$juego_id.", 1)";
$result = mysqli_query($db, $query) or die('Error al insertar comentario');

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
<a href="detail.php?id=<?php echo $juego_id; ?>">Volver al juego</a>
</body>
</html>