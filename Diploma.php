<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

require('fpdf.php');

// Obtener parámetros GET
$name = isset($_GET['name']) ? $_GET['name'] : 'Nombre';
$surname = isset($_GET['surname']) ? $_GET['surname'] : 'Apellido';

// Validar que no estén vacíos
if (empty(trim($name)) || empty(trim($surname))) {
    die('Error: Se requieren los parámetros name y surname');
}

// Crear instancia de FPDF
$pdf = new FPDF('L', 'mm', 'A4'); // Horizontal, mm, A4
$pdf->AddPage();

// ===== FONDO CON COLOR DE RESPALDO =====
$pdf->SetFillColor(245, 245, 220); // Beige claro (por si no carga el borde)
$pdf->Rect(0, 0, 297, 210, 'F');

// ===== MARCO DECORATIVO (borde.png) =====
$bordePath = __DIR__ . '/imagenes/borde.png';
if (file_exists($bordePath)) {
    $pdf->Image($bordePath, 0, 0, 297, 210);
}

// ===== IMAGEN 1: SELLO SUPERIOR IZQUIERDA =====
$selloPath = __DIR__ . '/imagenes/sello.png';
if (file_exists($selloPath)) {
    $pdf->Image($selloPath, 25, 25, 40); // x=25, y=25, ancho=40
}

// ===== CELDA 1: TÍTULO PRINCIPAL =====
$pdf->SetFont('Arial', 'B', 40);
$pdf->SetTextColor(25, 25, 112);
$pdf->SetXY(20, 40);
$pdf->Cell(257, 20, 'DIPLOMA DE HONOR', 0, 1, 'C');

// ===== CELDA 2: SUBTÍTULO =====
$pdf->SetFont('Arial', 'I', 18);
$pdf->SetTextColor(105, 105, 105);
$pdf->SetXY(20, 65);
$pdf->Cell(257, 10, 'Desarrollo Web en Entorno Servidor', 0, 1, 'C');

// ===== LÍNEA DECORATIVA =====
$pdf->SetDrawColor(184, 134, 11);
$pdf->SetLineWidth(0.5);
$pdf->Line(80, 80, 217, 80);

// ===== CELDA 3: TEXTO CERTIFICACIÓN =====
$pdf->SetFont('Arial', '', 14);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(20, 90);
$pdf->MultiCell(257, 8, 'Se otorga el presente diploma a:', 0, 'C');

// ===== CELDA 4: NOMBRE COMPLETO DEL ESTUDIANTE =====
$pdf->SetFont('Times', 'BI', 32);
$pdf->SetTextColor(139, 0, 0);
$pdf->SetXY(20, 105);
$fullName = $name . ' ' . $surname;
$pdf->Cell(257, 15, iconv('UTF-8', 'ISO-8859-1', $fullName), 0, 1, 'C');

// ===== LÍNEA BAJO EL NOMBRE =====
$pdf->SetDrawColor(0, 0, 0);
$pdf->SetLineWidth(0.3);
$pdf->Line(70, 122, 227, 122);

// ===== CELDA 5: TEXTO DE RECONOCIMIENTO =====
$pdf->SetFont('Arial', '', 12);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(20, 130);
$reconocimiento = 'Por haber completado satisfactoriamente el curso de Desarrollo Web en Entorno Servidor, ' .
                  'demostrando excelencia académica, dedicación y habilidades sobresalientes en ' .
                  'programación PHP, gestión de bases de datos y desarrollo de aplicaciones web dinámicas.';
$pdf->MultiCell(257, 6, iconv('UTF-8', 'ISO-8859-1', $reconocimiento), 0, 'C');

// ===== FECHA DEL DIPLOMA =====
$pdf->SetFont('Arial', 'I', 11);
$pdf->SetTextColor(70, 70, 70);
$pdf->SetXY(20, 155);

// Fecha en español usando array de meses (compatible con cualquier PHP)
$meses = ['enero','febrero','marzo','abril','mayo','junio',
          'julio','agosto','septiembre','octubre','noviembre','diciembre'];
$fecha = date('d') . ' de ' . $meses[date('n')-1] . ' de ' . date('Y');

$pdf->Cell(257, 8, 'Fecha de expedición: ' . iconv('UTF-8', 'ISO-8859-1', $fecha), 0, 1, 'C');

// ===== FIRMAS =====
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
$pdf->Cell(60, 5, 'Coordinador Académico', 0, 1, 'C');

// ===== SALIDA =====
$pdf->Output();
?>
