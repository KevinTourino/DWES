<?php
function calcular_imc($peso, $altura) {
    if ($altura == 0) {
        return null;
    }
    if ($peso == 0){
        return null;
    }
    return $peso / ($altura * $altura);
}

$peso = isset($_GET['peso']) ? floatval($_GET['peso']) : null;
$altura = isset($_GET['altura']) ? floatval($_GET['altura']) : null;
?>
    <h1>Calculadora de IMC</h1>

    <?php 
    if ($peso === null || $altura === null) {
        echo "Por favor, proporciona los parámetros peso y altura en la URL." . "<br>";
        echo "Ejemplo: ?peso=70&altura=1.75";
    } else {
        $imc = calcular_imc($peso, $altura);
        if ($imc === null) {
            echo "Valores inválida.";
        } else {
            echo "Tu IMC es: " . round($imc, 2);
            if ($imc < 18.5) {
                echo "<br>" . "Tienes un IMC: Bajo en peso";
            } elseif ($imc >= 18.5 && $imc <= 24.9) {
                echo "<br>" . "Tienes un IMC: Normal";
            } else {
                echo "<br>" . "Tienes un IMC: Sobrepeso";
            }
        }
    }
    ?>
