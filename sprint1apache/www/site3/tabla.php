<?php
$numero = 7;
?>
    <h1>Tabla de multiplicar del <?php echo $numero; ?></h1>
    <table border="1">
        <thead>
            <tr>
                <th>Multiplicación</th>
                <th>Resultado</th>
            </tr>
        </thead>
        <tbody>
            <?php
            for ($i = 1; $i <= 10; $i++) {
                echo "<tr>";
                echo "<td>$numero x $i</td>";
                echo "<td>" . ($numero * $i) . "</td>";
                echo "</tr>";
            }
            ?>
        </tbody>
    </table>
</body>
</html>
