<?php
    session_start();
    ob_start();

    // Verificar que el usuario está logueado
    if (!isset($_SESSION['user_id'])) {
        header('Location: login.html');
        exit;
    }

    // Conectar a la base de datos
    $db = mysqli_connect('localhost', 'admin', '1234', 'mysitedb') or die('Error de conexión a la base de datos');

    // Verificar que se han enviado los datos del formulario
    if ($_SERVER['REQUEST_METHOD'] != 'POST') {
        header('Location: changepassword.html');
        exit;
    }

    // Obtener los datos del formulario
    $current_password = isset($_POST['current_password']) ? trim($_POST['current_password']) : '';
    $new_password = isset($_POST['new_password']) ? trim($_POST['new_password']) : '';
    $confirm_password = isset($_POST['confirm_password']) ? trim($_POST['confirm_password']) : '';

    // Variable para almacenar errores
    $error = '';

    // Comprobar que no hay campos vacíos
    if (empty($current_password) || empty($new_password) || empty($confirm_password)) {
        $error = 'Todos los campos son obligatorios';
    }
    // Comprobar que las nuevas contraseñas coinciden
    elseif ($new_password !== $confirm_password) {
        $error = 'Las nuevas contraseñas no coinciden';
    }
    // Comprobar que las nuevas contraseñas coinciden con la antigua
    elseif ($current_password === $confirm_password && $current_password === $confirm_password) {
        $error = 'Las nuevas contraseñas coinciden con la antigua contraseña';
    }
    // Verificar que la contraseña actual es correcta
    else {
        $user_id = intval($_SESSION['user_id']);
        $query = "SELECT contraseña FROM tUsuarios WHERE id = " . $user_id;
        $result = mysqli_query($db, $query);
        
        if (mysqli_num_rows($result) == 0) {
            $error = 'Usuario no encontrado';
        }
        else {
            $user = mysqli_fetch_assoc($result);
            
            if (!password_verify($current_password, $user['contraseña'])) {
                $error = 'La contraseña actual es incorrecta';
            }
        }
    }

    // Si hay algún error, mostrarlo
    if (!empty($error)) {
        mysqli_close($db);
        ?>
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Error al cambiar contraseña</title>
        </head>
        <body>
            <h1>Error al cambiar contraseña</h1>
            <p style="color: red;"><?php echo htmlspecialchars($error); ?></p>
            <a href="changepassword.html">Volver al formulario</a>
        </body>
        </html>
        <?php
        exit;
    }

    // Si no hay errores, actualizar la contraseña
    $new_password_hashed = password_hash($new_password, PASSWORD_DEFAULT);
    $user_id = intval($_SESSION['user_id']);

    $query = "UPDATE tUsuarios SET contraseña = '" . mysqli_real_escape_string($db, $new_password_hashed) . "' WHERE id = " . $user_id;

    if (mysqli_query($db, $query)) {
        mysqli_close($db);
        ?>
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Contraseña cambiada</title>
        </head>
        <body>
            <h1>¡Contraseña cambiada exitosamente!</h1>
            <p>Tu contraseña ha sido actualizada correctamente.</p>
            <a href="main.php">Volver a la página principal</a>
        </body>
        </html>
        <?php
        exit;
    } else {
        mysqli_close($db);
        ?>
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Error al cambiar contraseña</title>
        </head>
        <body>
            <h1>Error al cambiar contraseña</h1>
            <p style="color: red;">Ha ocurrido un error al actualizar la contraseña. Por favor, inténtalo de nuevo.</p>
            <a href="changepassword.html">Volver al formulario</a>
        </body>
        </html>
        <?php
        exit;
    }
?>