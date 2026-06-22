@echo off
echo ================================================
echo   BUILD FRONTEND UNTUK UPLOAD KE cPANEL
echo ================================================
echo.

cd /d "%~dp0frontend"

echo [1/2] Install dependencies...
call npm install
if %errorlevel% neq 0 (
    echo ERROR: npm install gagal!
    pause
    exit /b 1
)

echo.
echo [2/2] Build production...
call npm run build
if %errorlevel% neq 0 (
    echo ERROR: npm build gagal!
    pause
    exit /b 1
)

echo.
echo ================================================
echo   BUILD BERHASIL!
echo.
echo   Langkah selanjutnya:
echo   1. Buka folder: frontend\dist
echo   2. Upload SEMUA ISI folder dist ke
echo      public_html di cPanel kamu
echo   3. Pastikan file .htaccess ikut ter-upload
echo ================================================
echo.
explorer "%~dp0frontend\dist"
pause
