<?php
// Pengaturan Database
// Untuk LOKAL (localhost)
if ($_SERVER['HTTP_HOST'] == 'localhost' || $_SERVER['HTTP_HOST'] == '127.0.0.1') {
    define('DB_HOST', 'localhost');
    define('DB_USER', 'uxsf55g0_intantoko');
    define('DB_PASS', '300706tan');
    define('DB_NAME', 'uxsf55g0_toko_intan');
} 
// Untuk PRODUCTION (hosting)
else {
    define('DB_HOST', 'localhost');
    define('DB_USER', 'GANTI_DENGAN_USERNAME_DB');  // Ganti nanti di hosting
    define('DB_PASS', 'GANTI_DENGAN_PASSWORD_DB');  // Ganti nanti di hosting
    define('DB_NAME', 'GANTI_DENGAN_NAMA_DB');      // Ganti nanti di hosting
}

// Membuat koneksi
try {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    // Cek koneksi
    if ($conn->connect_error) {
        die("Koneksi gagal: " . $conn->connect_error);
    }
    
    // Set charset UTF-8 agar support bahasa Indonesia
    $conn->set_charset("utf8mb4");
    
} catch (Exception $e) {
    die("Error: " . $e->getMessage());
}
?>
