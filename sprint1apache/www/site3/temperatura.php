    <h1>Conversor de Temperaturas</h1>

    <form method="post" action="">
        <label for="cantidad">Cantidad:</label>
        <input type="number" name="cantidad" id="cantidad"><br><br>

        <input type="radio" name="conversion" value="c_to_f" id="c_to_f">
        <label for="c_to_f">Celsius → Fahrenheit</label><br>

        <input type="radio" name="conversion" value="f_to_c" id="f_to_c">
        <label for="f_to_c">Fahrenheit → Celsius</label><br><br>

        <input type="submit" value="Convertir">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $cantidad = $_POST['cantidad'];
        $conversion = $_POST['conversion'];

        if (is_numeric($cantidad)) {
            if ($conversion == 'c_to_f') {
                // Celsius a Fahrenheit
                $resultado = ($cantidad * 9/5) + 32;
                echo "<p>$cantidad &deg;C = " . round($resultado, 2) . " &deg;F</p>";
            } elseif ($conversion == 'f_to_c') {
                // Fahrenheit a Celsius
                $resultado = ($cantidad - 32) * 5/9;
                echo "<p>$cantidad &deg;F = " . round($resultado, 2) . " &deg;C</p>";
            } else {
                echo "<p style='color:red;'>Conversión no válida.</p>";
            }
        } else {
            echo "<p style='color:red;'>Por favor, introduce una cantidad numérica válida.</p>";
        }
    }
    ?>
