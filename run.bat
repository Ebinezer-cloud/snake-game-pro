@echo off
title Snake Game Pro

cd /d "%~dp0"

py -3.11 -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Failed to install requirements.
    pause
    exit /b
)

py -3.11 main.py

pause
