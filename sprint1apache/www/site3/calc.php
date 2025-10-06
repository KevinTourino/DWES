    <h1>Calculadora</h1>

    <form method="post" action="">
        <label for="num1">Número 1:</label>
        <input type="number" name="num1" id="num1"><br><br>

        <label for="num2">Número 2:</label>
        <input type="number" name="num2" id="num2"><br><br>

        <label for="operacion">Operación:</label>
        <select name="operacion" id="operacion">
            <option value="suma">Suma</option>
            <option value="resta">Resta</option>
            <option value="multiplicacion">Multiplicación</option>
            <option value="division">División</option>
        </select><br><br>

        <input type="submit" value="Calcular">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $num1 = $_POST['num1'];
        $num2 = $_POST['num2'];
        $operacion = $_POST['operacion'];

        if (is_numeric($num1) && is_numeric($num2)) {
            switch ($operacion) {
                case 'suma':
                    $resultado = $num1 + $num2;
                    echo "<p>$num1" . " + " . "$num2 = " . round($resultado, 2) . "</p>";
                    break;
                case 'resta':
                    $resultado = $num1 - $num2;
                    echo "<p>$num1" . " - " . "$num2 = " . round($resultado, 2) . "</p>";
                    break;
                case 'multiplicacion':
                    $resultado = $num1 * $num2;
                    echo "<p>$num1" . " * " . "$num2 = " . round($resultado, 2) . "</p>";
                    break;
                case 'division':
                    if ($num2 != 0) {
                        $resultado = $num1 / $num2;
                        echo "<p>$num1" . " / " . "$num2 = " . round($resultado, 2) . "</p>";
                    } else {
                        echo "<p style='color:red;'>No se puede dividir entre cero.</p>";
                        exit;
                    }
                    break;
                default:
                    echo "<p style='color:red;'>Operación no válida.</p>";
                    exit;
            }

            
        } else {
            echo "<p style='color:red;'>Por favor, introduce números válidos.</p>";
        }
    }
    ?>

