<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

require('fpdf.php');

//Obtener parámetros GET
$name = isset($_GET['name']) ? $_GET['name'] : 'Nombre';
$surname = isset($_GET['surname']) ? $_GET['surname'] : 'Apellido';

//Validar que no estén vacíos
if (empty(trim($name)) || empty(trim($surname))) {
    die('Error: Se requieren los parámetros name y surname');
}

// Crear instancia de FPDF
$pdf = new FPDF('L', 'mm', 'A4');
$pdf->AddPage();


//Borde
$bordePath = __DIR__ . '/imagenes/borde1.png';
if (file_exists($bordePath)) {
    $pdf->Image($bordePath, -10, -15, 320, 240);
}

//Fondo
$pdf->SetFillColor(245, 245, 220);
$pdf->Rect(10, 10, 278, 192, 'F');

//Sello
$selloPath = __DIR__ . '/imagenes/sello.png';
if (file_exists($selloPath)) {
    $pdf->Image($selloPath, 30, 35, 40);
}

//Titulo
$pdf->SetFont('Arial', 'B', 40);
$pdf->SetTextColor(25, 25, 112);
$pdf->SetXY(20, 40);
$pdf->Cell(257, 20, 'DIPLOMA DE HONOR', 0, 1, 'C');

//DAW
$pdf->SetFont('Arial', 'I', 18);
$pdf->SetTextColor(105, 105, 105);
$pdf->SetXY(20, 65);
$pdf->Cell(257, 10, 'Desarrollo Web en Entorno Servidor', 0, 1, 'C');

//Linea decorativa
$pdf->SetDrawColor(184, 134, 11);
$pdf->SetLineWidth(0.5);
$pdf->Line(80, 80, 217, 80);

//Texto
$pdf->SetFont('Arial', '', 14);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(20, 90);
$pdf->MultiCell(257, 8, 'Se otorga el presente diploma a:', 0, 'C');

//Nombre
$pdf->SetFont('Times', 'BI', 32);
$pdf->SetTextColor(139, 0, 0);
$pdf->SetXY(20, 105);
$fullName = $name . ' ' . $surname;
$pdf->Cell(257, 15, iconv('UTF-8', 'ISO-8859-1', $fullName), 0, 1, 'C');

//Linea decorativa bajo el nombre
$pdf->SetDrawColor(0, 0, 0);
$pdf->SetLineWidth(0.3);
$pdf->Line(70, 122, 227, 122);

//Texto
$pdf->SetFont('Arial', '', 12);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(20, 130);
$reconocimiento = 'Por haber completado satisfactoriamente el curso de Desarrollo Web en Entorno Servidor, ' .
                  'demostrando excelencia académica, dedicación y habilidades sobresalientes en ' .
                  'programación PHP, gestión de bases de datos y desarrollo de aplicaciones web dinámicas.';
$pdf->MultiCell(257, 6, iconv('UTF-8', 'ISO-8859-1', $reconocimiento), 0, 'C');

//Fecha del diploma
$pdf->SetFont('Arial', 'I', 11);
$pdf->SetTextColor(70, 70, 70);
$pdf->SetXY(20, 155);

// Fecha en español
$meses = ['enero','febrero','marzo','abril','mayo','junio',
          'julio','agosto','septiembre','octubre','noviembre','diciembre'];
$fecha = date('d') . ' de ' . $meses[date('n')-1] . ' de ' . date('Y');

$pdf->Cell(257, 8, 'Fecha de expedicion: ' . iconv('UTF-8', 'ISO-8859-1', $fecha), 0, 1, 'C');

//Firmas
$pdf->SetFont('Arial', 'B', 11);
$pdf->SetTextColor(0, 0, 0);

// Firma izquierda
$pdf->SetXY(50, 170);
$pdf->Cell(60, 5, '_______________________', 0, 1, 'C');
$pdf->SetXY(50, 176);
$pdf->SetFont('Arial', '', 9);
$pdf->Cell(60, 5, 'Director del Programa', 0, 1, 'C');

// Firma derecha
$pdf->SetXY(187, 170);
$pdf->SetFont('Arial', 'B', 11);
$pdf->Cell(60, 5, '_______________________', 0, 1, 'C');
$pdf->SetXY(187, 176);
$pdf->SetFont('Arial', '', 9);
$pdf->Cell(60, 5, 'Coordinador Academico', 0, 1, 'C');

//Salida
$pdf->Output();
?>
