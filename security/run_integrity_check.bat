@echo off
title AUDITOR DE INTEGRIDADE DE ARQUIVOS
mode con: cols=80 lines=20
color 0E
cls
echo ======================================================
echo          GERADOR DE HASH SHA-256 (AUDITORIA)
echo ======================================================
echo.
"..\.venv\Scripts\python.exe" file_hasher.py
pause