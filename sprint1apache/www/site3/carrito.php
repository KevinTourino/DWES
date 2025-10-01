<?php
$carrito = [
    ["Manzana", 0.50],
    ["Pan", 1.20],
    ["Leche", 0.90],
    ["Huevos", 2.00]
];

$total = 0;
?>
    <h1>Carrito de la compra</h1>

    <table border="1">
        <thead>
            <tr>
                <th>Producto</th>
                <th>Precio</th>
            </tr>
        </thead>
        <tbody>
            <?php
            foreach ($carrito as $producto) {
                echo "<tr>";
                echo "<td>" . ($producto[0]) . "</td>";
                echo "<td>" . number_format($producto[1], 2) . "€</td>";
                echo "</tr>";

                $total += $producto[1];
            }
            ?>
            <tr>
                <td><strong>TOTAL:</strong></td>
                <td><strong><?php echo number_format($total, 2); ?>€</strong></td>
            </tr>
        </tbody>
    </table>
