"""
Build script to create the Windows installer for Agent Tool
This script:
1. Creates the executable using PyInstaller
2. Prepares all necessary files
3. Builds the installer using Inno Setup (if available)
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def clean_build_dirs():
    """Clean previous build directories"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"Cleaned {dir_name}")

def create_icon():
    """Create a simple icon file if it doesn't exist"""
    icon_content = """
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

# Create a simple icon
img = PIL.Image.new('RGBA', (256, 256), (0, 0, 0, 0))
draw = PIL.ImageDraw.Draw(img)

# Draw a robot emoji-like icon
draw.ellipse([50, 50, 206, 206], fill=(70, 130, 180), outline=(0, 0, 0, 255), width=3)
draw.rectangle([80, 90, 110, 120], fill=(255, 255, 255))
draw.rectangle([146, 90, 176, 120], fill=(255, 255, 255))
draw.arc([80, 140, 176, 180], 0, 180, fill=(255, 255, 255), width=5)

img.save('icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
print("Icon created successfully")
"""
    
    if not os.path.exists('icon.ico'):
        try:
            exec(icon_content)
        except:
            print("Could not create icon, continuing without it")

def create_license():
    """Create LICENSE.txt file"""
    with open('LICENSE.txt', 'w') as f:
        f.write("""MIT License

Copyright (c) 2024 Agent Tool

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")
    print("LICENSE.txt created")

def create_readme():
    """Create README.txt file"""
    with open('README.txt', 'w') as f:
        f.write("""Agent Tool - Automation Assistant
==================================

Welcome to Agent Tool, a powerful automation assistant that helps you control
your computer through programmed mouse and keyboard actions.

FEATURES:
---------
• Record and replay mouse and keyboard actions
• Create custom automation sequences
• Save and load automation macros
• Quick actions for common tasks
• Emergency stop with Ctrl+Shift+Esc
• Modern, user-friendly interface

GETTING STARTED:
----------------
1. Launch Agent Tool from your Start Menu or Desktop
2. Click "Start Recording" to record your actions
3. Perform the actions you want to automate
4. Click "Stop Recording" when done
5. Click "Play Sequence" to replay your actions

SAFETY:
-------
• Press Ctrl+Shift+Esc at any time for emergency stop
• The tool includes safety delays between actions
• Always test your sequences before running them unattended

SYSTEM REQUIREMENTS:
--------------------
• Windows 10 or later (64-bit)
• 4GB RAM minimum
• 100MB free disk space
• Administrator privileges for installation

SUPPORT:
--------
For help and support, please visit: https://yourwebsite.com/support

Thank you for using Agent Tool!
""")
    print("README.txt created")

def build_executable():
    """Build the executable using PyInstaller"""
    
    # PyInstaller spec file content
    spec_content = """
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main_app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('macros', 'macros'),
    ],
    hiddenimports=[
        'PIL._tkinter_finder',
        'customtkinter',
        'pyautogui',
        'keyboard',
        'mouse',
        'pynput',
        'cv2',
        'numpy',
        'requests'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='AgentTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
    version_file=None,
)
"""
    
    # Write spec file
    with open('AgentTool.spec', 'w') as f:
        f.write(spec_content)
    
    print("Building executable with PyInstaller...")
    
    # Run PyInstaller
    try:
        subprocess.run([
            sys.executable, '-m', 'PyInstaller',
            '--onefile',
            '--windowed',
            '--name', 'AgentTool',
            '--icon', 'icon.ico' if os.path.exists('icon.ico') else 'NONE',
            '--add-data', 'macros;macros',
            '--hidden-import', 'customtkinter',
            '--hidden-import', 'pyautogui',
            '--hidden-import', 'keyboard',
            '--hidden-import', 'mouse',
            '--hidden-import', 'pynput',
            '--collect-all', 'customtkinter',
            'main_app.py'
        ], check=True)
        print("Executable built successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error building executable: {e}")
        return False
    except FileNotFoundError:
        print("PyInstaller not found. Installing...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])
        return build_executable()  # Retry after installation

def build_installer():
    """Build the installer using Inno Setup"""
    
    # Check if Inno Setup is installed
    inno_paths = [
        r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe",
        r"C:\Program Files\Inno Setup 6\ISCC.exe",
        r"C:\Program Files (x86)\Inno Setup 5\ISCC.exe",
        r"C:\Program Files\Inno Setup 5\ISCC.exe",
    ]
    
    iscc_path = None
    for path in inno_paths:
        if os.path.exists(path):
            iscc_path = path
            break
    
    if iscc_path:
        print(f"Building installer with Inno Setup at {iscc_path}...")
        try:
            subprocess.run([iscc_path, 'installer_config.iss'], check=True)
            print("Installer built successfully!")
            print("Find your installer in the 'dist' directory")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error building installer: {e}")
            return False
    else:
        print("Inno Setup not found. Please install it from: https://jrsoftware.org/isdl.php")
        print("The executable has been created in the 'dist' directory")
        return False

def create_nsis_installer():
    """Alternative: Create NSIS installer script"""
    nsis_script = """
!define APP_NAME "Agent Tool"
!define APP_VERSION "1.0.0"
!define APP_PUBLISHER "Your Company"
!define APP_URL "https://yourwebsite.com"
!define APP_EXE "AgentTool.exe"

!include "MUI2.nsh"

Name "${APP_NAME}"
OutFile "dist\\AgentTool_Setup_${APP_VERSION}.exe"
InstallDir "$PROGRAMFILES64\\${APP_NAME}"
InstallDirRegKey HKLM "Software\\${APP_NAME}" "Install_Dir"
RequestExecutionLevel admin

!define MUI_ABORTWARNING
!define MUI_ICON "icon.ico"

!insertmacro MUI_PAGE_LICENSE "LICENSE.txt"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"

Section "Agent Tool (required)"
  SectionIn RO
  
  SetOutPath $INSTDIR
  File "dist\\AgentTool.exe"
  File "LICENSE.txt"
  File "README.txt"
  
  CreateDirectory "$INSTDIR\\macros"
  CreateDirectory "$INSTDIR\\logs"
  
  WriteRegStr HKLM "Software\\${APP_NAME}" "Install_Dir" "$INSTDIR"
  
  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}" \\
                   "DisplayName" "${APP_NAME}"
  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}" \\
                   "UninstallString" '"$INSTDIR\\uninstall.exe"'
  WriteRegDWORD HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}" \\
                     "NoModify" 1
  WriteRegDWORD HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}" \\
                     "NoRepair" 1
  WriteUninstaller "uninstall.exe"
SectionEnd

Section "Start Menu Shortcuts"
  CreateDirectory "$SMPROGRAMS\\${APP_NAME}"
  CreateShortcut "$SMPROGRAMS\\${APP_NAME}\\${APP_NAME}.lnk" "$INSTDIR\\${APP_EXE}"
  CreateShortcut "$SMPROGRAMS\\${APP_NAME}\\Uninstall.lnk" "$INSTDIR\\uninstall.exe"
SectionEnd

Section "Desktop Shortcut"
  CreateShortcut "$DESKTOP\\${APP_NAME}.lnk" "$INSTDIR\\${APP_EXE}"
SectionEnd

Section "Uninstall"
  DeleteRegKey HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}"
  DeleteRegKey HKLM "Software\\${APP_NAME}"
  
  Delete "$INSTDIR\\${APP_EXE}"
  Delete "$INSTDIR\\LICENSE.txt"
  Delete "$INSTDIR\\README.txt"
  Delete "$INSTDIR\\uninstall.exe"
  
  RMDir /r "$INSTDIR\\macros"
  RMDir /r "$INSTDIR\\logs"
  RMDir "$INSTDIR"
  
  Delete "$SMPROGRAMS\\${APP_NAME}\\*.*"
  RMDir "$SMPROGRAMS\\${APP_NAME}"
  Delete "$DESKTOP\\${APP_NAME}.lnk"
SectionEnd
"""
    
    with open('installer_nsis.nsi', 'w') as f:
        f.write(nsis_script)
    print("NSIS installer script created as 'installer_nsis.nsi'")
    print("You can compile it with NSIS from: https://nsis.sourceforge.io/")

def main():
    """Main build process"""
    print("=" * 50)
    print("Agent Tool - Build Script")
    print("=" * 50)
    
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create necessary directories
    os.makedirs('macros', exist_ok=True)
    
    # Step 1: Clean previous builds
    clean_build_dirs()
    
    # Step 2: Create necessary files
    create_icon()
    create_license()
    create_readme()
    
    # Step 3: Install dependencies
    print("\nInstalling dependencies...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
    
    # Step 4: Build executable
    if build_executable():
        print("\n✓ Executable created successfully!")
        
        # Step 5: Build installer
        if not build_installer():
            # If Inno Setup is not available, create NSIS script as alternative
            create_nsis_installer()
    else:
        print("\n✗ Failed to create executable")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("Build complete!")
    print("=" * 50)
    
    if os.path.exists('dist/AgentTool.exe'):
        print(f"\nExecutable location: {os.path.abspath('dist/AgentTool.exe')}")
    
    installer_files = list(Path('dist').glob('*Setup*.exe'))
    if installer_files:
        print(f"Installer location: {os.path.abspath(installer_files[0])}")

if __name__ == "__main__":
    main()