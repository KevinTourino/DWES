<?php
ob_start();

// Conectar a la base de datos
$db = mysqli_connect('localhost', 'admin', '1234', 'mysitedb') or die('Error de conexión a la base de datos');

// Verificar que se han enviado los datos del formulario
if ($_SERVER['REQUEST_METHOD'] != 'POST') {
    header('Location: login.html');
    exit;
}

// Obtener los datos del formulario
$email = isset($_POST['email']) ? trim($_POST['email']) : '';
$password = isset($_POST['password']) ? $_POST['password'] : '';

$error = '';

//Comprobar que no hay campos vacíos
if (empty($email) || empty($password)) {
    $error = 'Todos los campos son obligatorios';
}
else {
    // Buscar el usuario en la base de datos
    $query = "SELECT id, email, contraseña FROM tUsuarios WHERE email = '" . mysqli_real_escape_string($db, $email) . "'";
    $result = mysqli_query($db, $query);
    
    if (mysqli_num_rows($result) == 0) {
        $error = 'El correo electrónico no está registrado';
    }
    else {
        // El usuario existe, verificar la contraseña
        $user = mysqli_fetch_assoc($result);
        
        if (!password_verify($password, $user['contraseña'])) {
            $error = 'La contraseña es incorrecta';
        }
        else {
            mysqli_close($db);
            ob_end_clean();
            header('Location: main.php');
            exit;
        }
    }
}

mysqli_close($db);
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Error de inicio de sesión</title>
</head>
<body>
    <h1>Error de inicio de sesión</h1>
    <p style="color: red;"><?php echo htmlspecialchars($error); ?></p>
    <a href="login.html">Volver al formulario de inicio de sesión</a>
</body>
</html>
