@echo off
echo ========================================
echo Agent Tool - Windows Build Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Building installer...
python build_installer.py

echo.
echo ========================================
echo Build process complete!
echo ========================================
echo.
echo Check the 'dist' folder for the output files:
echo - AgentTool.exe (standalone executable)
echo - AgentTool_Setup_1.0.0.exe (installer, if Inno Setup is installed)
echo.
pause