@echo off
REM Quick build script for Windows users

echo ===================================
echo   Quick Python to EXE Builder
echo ===================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Run the build script
echo Building executable...
python build_exe.py %*

echo.
echo Build complete! Check the 'dist' folder for your executable.
pause