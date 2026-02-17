@echo off
title SYSTEM RESOURCE DASHBOARD - v1.0
mode con: cols=60 lines=15
color 0A
cls
echo ============================================
echo    INICIANDO MONITORAMENTO DE PERFORMANCE   
echo ============================================
python resource_monitor.py
pause