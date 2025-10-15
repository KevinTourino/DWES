<?php
$db = mysqli_connect('localhost', 'admin', '1234', 'mysitedb') or die('Fail');
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Detalle del Juego</title>
</head>
<body>
<?php
if (!isset($_GET['id'])) {
    die('No se ha especificado un juego');
}
$juego_id = intval($_GET['id']);
$query = 'SELECT * FROM tJuegos WHERE id='.$juego_id;
$result = mysqli_query($db, $query) or die('Query error');
if (mysqli_num_rows($result) == 0){
    die('Juego no encontrado');
}
$juego = mysqli_fetch_assoc($result);
?>
<h1><?php echo $juego['nombre']; ?></h1>
<?php if (!empty($juego['url_imagen'])): ?>
<img src="<?php echo $juego['url_imagen']; ?>" alt="<?php echo $juego['nombre']; ?>" style="max-width: 400px;">
<?php endif; ?>
<p><strong>Plataforma:</strong> <?php echo $juego['plataforma']; ?></p>
<p><strong>Año de lanzamiento:</strong> <?php echo $juego['año_lanzamiento']; ?></p>

<h3>Comentarios:</h3>
<?php
$query2 = 'SELECT * FROM tComentarios WHERE juego_id='.$juego_id.' ORDER BY fecha DESC';
$result2 = mysqli_query($db, $query2) or die('Query error');
if (mysqli_num_rows($result2) == 0){
    echo '<p>No hay comentarios todavía</p>';
}
else{
    echo '<ul>';
    while ($row = mysqli_fetch_array($result2)) {
        echo '<li>';
        echo htmlspecialchars($row['comentario']);
        
        if (!empty($row['fecha'])) {
            $fecha_formateada = date('d/m/Y H:i', strtotime($row['fecha']));
            echo ' <small>(Publicado el: ' . $fecha_formateada . ')</small>';
        }
        
        echo '</li>';
    }
    echo '</ul>';
}
mysqli_close($db);
?>

<h3>Añadir un comentario:</h3>
<form action="comment.php" method="POST">
    <textarea name="new_comment" rows="4" cols="50" placeholder="Escribe tu comentario aquí..."></textarea>
    <input type="hidden" name="juego_id" value="<?php echo $juego_id; ?>">
    <br><br>
    <input type="submit" value="Enviar comentario">
</form>
</body>
</html>