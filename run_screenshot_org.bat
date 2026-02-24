@echo off
title ORGANIZADOR DE CAPTURAS DE TELA
mode con: cols=70 lines=15
color 0B
cls
echo ======================================================
echo           LIMPANDO E ORGANIZANDO PRINTS...
echo ======================================================
echo.
"..\.venv\Scripts\python.exe" screenshot_organizer.py
echo.
echo Operacao concluida!
pause