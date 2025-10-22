<?php
ob_start();

$db = mysqli_connect('localhost', 'admin', '1234', 'mysitedb') or die('Error de conexión a la base de datos');

//Verifica el método http
if ($_SERVER['REQUEST_METHOD'] != 'POST') {
    header('Location: register.html');
    exit;
}

//Recepción y validación de datos del formulario
$email = isset($_POST['email']) ? trim($_POST['email']) : '';
$password = isset($_POST['password']) ? $_POST['password'] : '';
$password_confirm = isset($_POST['password_confirm']) ? $_POST['password_confirm'] : '';
$error = '';


//Validación de campos
if (empty($email) || empty($password) || empty($password_confirm)) {
    $error = 'Todos los campos son obligatorios';
}
elseif ($password !== $password_confirm) {
    $error = 'Las contraseñas no coinciden';
}

//Comprobar si el email esta en la base de datos
else {
    $query = "SELECT id FROM tUsuarios WHERE email = '" . mysqli_real_escape_string($db, $email) . "'";
    $result = mysqli_query($db, $query);
    if (mysqli_num_rows($result) > 0) {
        $error = 'El correo electrónico ya está registrado';
    }
}

if (!empty($error)) {
    mysqli_close($db);
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Error en el registro</title>
</head>
<body>
    <h1>Error en el registro</h1>
    <p style="color: red;"><?php echo htmlspecialchars($error); ?></p>
    <a href="register.html">Volver al formulario de registro</a>
</body>
</html>
<?php
    exit;
}

//Registrar usuario
$password_hashed = password_hash($password, PASSWORD_DEFAULT);
$query = "INSERT INTO tUsuarios (email, contraseña) VALUES ('" .
         mysqli_real_escape_string($db, $email) . "', '" .
         mysqli_real_escape_string($db, $password_hashed) . "')";

//Insertar al usuario
if (mysqli_query($db, $query)) {
    mysqli_close($db);
    ob_end_clean();
    header('Location: main.php');
    exit;
} else {
    mysqli_close($db);
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Error en el registro</title>
</head>
<body>
    <h1>Error en el registro</h1>
    <p style="color: red;">Ha ocurrido un error al registrar el usuario.</p>
    <p>Error: <?php echo mysqli_error($db); ?></p>
    <a href="register.html">Volver al formulario de registro</a>
</body>
</html>
<?php
    exit;
}
?>