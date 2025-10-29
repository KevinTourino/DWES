<?php
error_reporting(E_ERROR | E_PARSE);
ini_set('display_errors', 0);

require('fpdf.php');

// Obtener parámetros GET
$name = isset($_GET['name']) ? $_GET['name'] : 'Nombre';
$surname = isset($_GET['surname']) ? $_GET['surname'] : 'Apellido';

// Validar que no estén vacíos
if (empty(trim($name)) || empty(trim($surname))) {
    die('Error: Se requieren los parámetros name y surname');
}

// Crear instancia de FPDF
$pdf = new FPDF('L', 'mm', 'A4'); // Landscape (horizontal), milímetros, tamaño A4
$pdf->AddPage();

// ===== FONDO CON COLOR =====
$pdf->SetFillColor(245, 245, 220); // Color beige claro
$pdf->Rect(0, 0, 297, 210, 'F');


// ===== IMAGEN 1: SELLO SUPERIOR =====
if (file_exists('imagenes/sello.png')) {
    $pdf->Image('imagenes/sello.png', 125, 20, 40); // x, y, ancho
}

// ===== CELDA 1: TÍTULO PRINCIPAL =====
$pdf->SetFont('Arial', 'B', 40);
$pdf->SetTextColor(25, 25, 112); // Azul oscuro
$pdf->SetXY(20, 40);
$pdf->Cell(257, 20, 'DIPLOMA DE HONOR', 0, 1, 'C');

// ===== CELDA 2: SUBTÍTULO =====
$pdf->SetFont('Arial', 'I', 18);
$pdf->SetTextColor(105, 105, 105); // Gris
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

// ===== CELDA 4: NOMBRE COMPLETO DEL ESTUDIANTE (DESTACADO) =====
$pdf->SetFont('Times', 'BI', 32);
$pdf->SetTextColor(139, 0, 0); // Rojo oscuro
$pdf->SetXY(20, 105);
$fullName = $name . ' ' . $surname;
$pdf->Cell(257, 15, utf8_decode($fullName), 0, 1, 'C');

// ===== LÍNEA BAJO EL NOMBRE =====
$pdf->SetDrawColor(0, 0, 0);
$pdf->SetLineWidth(0.3);
$pdf->Line(70, 122, 227, 122);

// ===== CELDA 5: TEXTO DE RECONOCIMIENTO =====
$pdf->SetFont('Arial', '', 12);
$pdf->SetTextColor(0, 0, 0);
$pdf->SetXY(20, 130);
$reconocimiento = 'Por haber completado satisfactoriamente el curso de Desarrollo Web en Entorno Servidor, ' .
                  'demostrando excelencia academica, dedicacion y habilidades sobresalientes en ' .
                  'programacion PHP, gestion de bases de datos y desarrollo de aplicaciones web dinamicas.';
$pdf->MultiCell(257, 6, utf8_decode($reconocimiento), 0, 'C');

// ===== FECHA DEL DIPLOMA =====
$pdf->SetFont('Arial', 'I', 11);
$pdf->SetTextColor(70, 70, 70);
$pdf->SetXY(20, 155);
// Configurar locale para español (si está disponible)
setlocale(LC_TIME, 'es_ES.UTF-8', 'es_ES', 'Spanish_Spain');
$fecha = strftime('%d de %B de %Y');
// Si strftime no funciona, usar alternativa
if (empty($fecha)) {
    $meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 
              'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
    $fecha = date('d') . ' de ' . $meses[date('n')-1] . ' de ' . date('Y');
}
$pdf->Cell(257, 8, 'Fecha de expedicion: ' . utf8_decode($fecha), 0, 1, 'C');

// ===== IMAGEN 2: SELLO/FIRMA (si existe) =====
// Descomenta y ajusta si tienes una imagen
// if (file_exists('images/sello.png')) {
//     $pdf->Image('images/sello.png', 230, 165, 30);
// }

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
$pdf->Cell(60, 5, 'Coordinador Academico', 0, 1, 'C');

$pdf->Output();
?>