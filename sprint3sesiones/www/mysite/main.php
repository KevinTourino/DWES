<?php
session_start();
$db = mysqli_connect('localhost', 'admin', '1234', 'mysitedb') or die('Fail');
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Lista de Juegos</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        padding: 20px;
    }

    h1 {
        text-align: center;
        color: #333;
    }

    .juegos-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 20px;
        margin-top: 30px;
    }

    .juego-card {
        background-color: #fff;
        margin-bottom: 20px;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        opacity: 0;
        animation: fadeIn 0.8s forwards;
    }

    .juego-card:hover {
        transform: scale(1.10);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }

    .juego-card img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 6px;
    }

    .no-imagen {
        width: 100%;
        height: 150px;
        background-color: #ccc;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 6px;
        font-style: italic;
        color: #555;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            filter: blur(4px);
        }
        to {
            opacity: 1;
            filter: blur(0);
        }
    }

    a {
        text-decoration: none;
        color: #007BFF;
    }

    a:hover {
        text-decoration: underline;
    }

    p {
        margin: 5px 0;
    }

    user-actions {
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
</head>
<body>
    <h1>Catálogo de Juegos</h1>

    <?php if (isset($_SESSION['user_id'])): ?>
        <div class="user-actions">
            <p>Bienvenido, <?php echo htmlspecialchars($_SESSION['email']); ?></p>
            <a href="logout.php">Cerrar sesión</a> |
            <a href="changepassword.html">Cambiar contraseña</a>
        </div>
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
