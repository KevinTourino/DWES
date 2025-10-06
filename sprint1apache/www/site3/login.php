    <h1>Login</h1>

    <form method="post" action="">
        <label for="text">Usuario:</label>
        <input type="text" name="user" id="user"><br><br>

        <label for="contraseña">Contraseña:</label>
        <input type="text" name="contraseña" id="contraseña"><br><br>

        <input type="submit" value="Login">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $user = $_POST['user'];
        $contraseña = $_POST['contraseña'];

        if ($user == null || $contraseña == null) {
            if ($user == null){
                echo "<p style='color:red;'>Por favor, introduce un usuario.</p>";
            }
            else{
                echo "<p style='color:red;'>Por favor, introduce una contraseña.</p>";
            }
            
        } else {
            if ($user == "admin" && $contraseña == 1234){
                echo "<p style='color:green;'>Acceso concedido..</p>";
            }
            else {
                echo "<p style='color:red;'>Acceso denegado.</p>";
            }


        }
    }
    ?>