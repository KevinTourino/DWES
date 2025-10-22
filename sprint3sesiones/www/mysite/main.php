<?php
session_start();
$db = mysqli_connect('localhost', 'admin', '1234', 'mysitedb') or die('Fail');
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Lista de Juegos</title>
</head>
<body>
    <h1>Catálogo de Juegos</h1>

    <?php if (isset($_SESSION['user_id'])): ?>
        <p>Bienvenido, <?php echo htmlspecialchars($_SESSION['email']); ?> | <a href="logout.php">Cerrar sesión</a></p>
    <?php else: ?>
        <p><a href="login.html">Iniciar sesión</a></p>
    <?php endif; ?>
    
    <div class="juegos-grid">
    <?php
    // Lanzar una consulta
    $query = 'SELECT * FROM tJuegos';
    $result = mysqli_query($db, $query) or die('Query error');
    
    if (mysqli_num_rows($result) == 0) {
        echo '<p>No hay juegos disponibles en la base de datos.</p>';
    } else {
        while ($row = mysqli_fetch_array($result)) {
            echo '<div class="juego-card">';
            

            if (!empty($row['url_imagen'])) {
                echo '<img src="' . htmlspecialchars($row['url_imagen']) . '" alt="' . htmlspecialchars($row['nombre']) . '">';
            } else {
                echo '<div class="no-imagen">Sin imagen</div>';
            }
            

            echo '<h3>' . htmlspecialchars($row['nombre']) . '</h3>';
            echo '<p><strong>Plataforma:</strong> ' . htmlspecialchars($row['plataforma']) . '</p>';
            echo '<p><strong>Año:</strong> ' . htmlspecialchars($row['año_lanzamiento']) . '</p>';
            
            echo '<a href="detail.php?id=' . $row['id'] . '">Ver detalles</a>';
            
            echo '</div>';
        }
    }
    
    mysqli_close($db);
    ?>
    </div>
</body>
</html>
