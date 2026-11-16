@echo off
chcp 65001 > nul
echo ========================================================
echo   PULSE TI - AUTOATUALIZACAO DO LIVRO VIVO
echo   Profissao: Analista de Redes N3 (Eduardo Pires)
echo ========================================================
echo.
python "%~dp0update_book.py"
echo.
pause
