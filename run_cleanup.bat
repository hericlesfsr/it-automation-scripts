@echo off
title Python System Cleaner - IT Automation Tool
cls

:: Check for Administrative Privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [ STATUS ] Running with Admin Privileges. Full scan authorized.
) else (
    echo [ WARNING ] Non-Admin execution detected.
    echo System-level folders will be skipped due to restricted access.
    echo -----------------------------------------------------------
)

echo Starting Python Maintenance Script...
echo.

:: Execute the python script
python system_cleaner.py

echo.
echo -----------------------------------------------------------
echo Maintenance Process Completed.
pause