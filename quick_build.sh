#!/bin/bash
# Quick build script for Linux/Mac users

echo "==================================="
echo "  Quick Python to EXE Builder"
echo "==================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run the build script
echo "Building executable..."
python build_exe.py "$@"

echo ""
echo "Build complete! Check the 'dist' folder for your executable."
echo "Note: Linux executables won't have .exe extension"