# Python to Executable (.exe) Guide for Production

## Quick Methods to Create .exe Files

### Method 1: PyInstaller (Most Popular & Easiest)

PyInstaller is the most commonly used tool for creating standalone executables from Python scripts.

#### Installation:
```bash
pip install pyinstaller
```

#### Basic Usage:
```bash
# Single file executable
pyinstaller --onefile your_script.py

# With custom icon and no console window (for GUI apps)
pyinstaller --onefile --windowed --icon=app.ico your_script.py

# For better performance (directory output)
pyinstaller your_script.py
```

#### Advanced Options:
- `--name`: Specify output name
- `--hidden-import`: Include modules not detected automatically
- `--add-data`: Include data files
- `--noconsole` or `-w`: Hide console window (GUI apps)
- `--clean`: Clean PyInstaller cache before building

### Method 2: cx_Freeze (Cross-platform)

Good for cross-platform distribution.

#### Installation:
```bash
pip install cx_Freeze
```

#### Setup Script (setup.py):
```python
from cx_Freeze import setup, Executable

setup(
    name="YourApp",
    version="1.0",
    description="Your application description",
    executables=[Executable("your_script.py")]
)
```

#### Build:
```bash
python setup.py build
```

### Method 3: Py2exe (Windows Only)

Specifically for Windows executables.

#### Installation:
```bash
pip install py2exe
```

#### Setup Script:
```python
from distutils.core import setup
import py2exe

setup(
    console=['your_script.py'],
    options={
        'py2exe': {
            'bundle_files': 1,
            'compressed': True
        }
    },
    zipfile=None
)
```

### Method 4: Nuitka (Fastest Performance)

Compiles Python to C++ for better performance.

#### Installation:
```bash
pip install nuitka
```

#### Usage:
```bash
# Standalone executable
nuitka --standalone --onefile your_script.py
```

### Method 5: Auto-py-to-exe (GUI Tool)

A graphical interface for PyInstaller.

#### Installation:
```bash
pip install auto-py-to-exe
```

#### Usage:
```bash
auto-py-to-exe
```

## Production Best Practices

### 1. Requirements Management
Create a `requirements.txt`:
```bash
pip freeze > requirements.txt
```

### 2. Virtual Environment
Always use virtual environments:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Configuration Management
Use environment variables or config files:
```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')
```

### 4. Error Handling & Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### 5. Testing Before Building
```bash
# Run tests
pytest tests/

# Check code quality
pylint your_script.py
```

## Sample Build Script

Create `build.py`:
```python
import PyInstaller.__main__
import os
import shutil

def build_exe():
    # Clean previous builds
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')
    
    # Build executable
    PyInstaller.__main__.run([
        'your_script.py',
        '--onefile',
        '--name=YourAppName',
        '--icon=icon.ico',
        '--add-data=config.ini;.',  # Include config files
        '--hidden-import=module_name',  # Include hidden imports
        '--clean',
        '--noconfirm'
    ])
    
    print("Build complete! Check the 'dist' folder.")

if __name__ == "__main__":
    build_exe()
```

## Troubleshooting Common Issues

### 1. Missing Modules
Add hidden imports:
```bash
pyinstaller --hidden-import=pkg_resources --hidden-import=PIL your_script.py
```

### 2. Large File Size
- Use UPX for compression: `pyinstaller --upx-dir=/path/to/upx your_script.py`
- Consider `--onedir` instead of `--onefile`

### 3. Antivirus False Positives
- Sign your executable with a code signing certificate
- Submit to antivirus vendors for whitelisting

### 4. Path Issues
Use absolute paths or:
```python
import sys
import os

if getattr(sys, 'frozen', False):
    # Running as compiled
    base_path = sys._MEIPASS
else:
    # Running as script
    base_path = os.path.dirname(os.path.abspath(__file__))
```

## Docker Alternative for Production

If .exe isn't strictly required, consider Docker:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "your_script.py"]
```

Build and run:
```bash
docker build -t your-app .
docker run your-app
```

## Quick Start Template

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Create your executable:
   ```bash
   pyinstaller --onefile --name MyApp your_script.py
   ```

3. Find your .exe in the `dist` folder

## Next Steps

1. Choose the method that best fits your needs
2. Test the executable on a clean system
3. Consider code signing for production
4. Implement auto-update mechanism if needed
5. Set up CI/CD for automated builds