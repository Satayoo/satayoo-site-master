#!/usr/bin/env python3
"""
Build script for creating executable from Python application
This script automates the process of creating a production-ready .exe file
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

# Configuration
APP_NAME = "SampleApp"
APP_VERSION = "1.0.0"
MAIN_SCRIPT = "sample_app.py"
ICON_FILE = None  # Set to "icon.ico" if you have an icon

def check_requirements():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        print(f"✓ PyInstaller version {PyInstaller.__version__} found")
        return True
    except ImportError:
        print("✗ PyInstaller not found")
        print("Installing PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
        return True

def clean_build_dirs():
    """Remove previous build artifacts"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"Cleaning {dir_name}/")
            shutil.rmtree(dir_name)
    
    # Remove .spec file if exists
    spec_file = f"{MAIN_SCRIPT.replace('.py', '.spec')}"
    if os.path.exists(spec_file):
        os.remove(spec_file)
        print(f"Removed {spec_file}")

def build_executable(mode='onefile'):
    """Build the executable using PyInstaller"""
    print(f"\nBuilding {mode} executable...")
    
    # Base PyInstaller command
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--name", APP_NAME,
        "--clean",
        "--noconfirm",
    ]
    
    # Add mode-specific options
    if mode == 'onefile':
        cmd.append("--onefile")
        print("Creating single-file executable (slower startup, easier distribution)")
    else:
        cmd.append("--onedir")
        print("Creating directory bundle (faster startup, multiple files)")
    
    # Add icon if available
    if ICON_FILE and os.path.exists(ICON_FILE):
        cmd.extend(["--icon", ICON_FILE])
    
    # Add data files if needed
    if os.path.exists("config.json"):
        cmd.extend(["--add-data", "config.json:." if sys.platform == "win32" else "config.json:."])
    
    # Hidden imports (add if your app needs them)
    # cmd.extend(["--hidden-import", "module_name"])
    
    # Add the main script
    cmd.append(MAIN_SCRIPT)
    
    # Run PyInstaller
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=False, text=True)
    
    if result.returncode == 0:
        print("✓ Build successful!")
        return True
    else:
        print("✗ Build failed!")
        return False

def create_distribution():
    """Create a distribution package with all necessary files"""
    dist_dir = Path("distribution")
    dist_dir.mkdir(exist_ok=True)
    
    # Copy executable
    if os.path.exists("dist"):
        # Copy everything from dist to distribution
        for item in os.listdir("dist"):
            src = os.path.join("dist", item)
            dst = os.path.join(dist_dir, item)
            if os.path.isdir(src):
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
    
    # Create README for distribution
    readme_content = f"""# {APP_NAME} v{APP_VERSION}

## Installation
No installation required! This is a standalone executable.

## Usage

### Command Line:
- Run without arguments for interactive mode: `{APP_NAME}.exe`
- Show info: `{APP_NAME}.exe --info`
- Process text: `{APP_NAME}.exe --process "your text"`
- Show version: `{APP_NAME}.exe --version`

### Interactive Mode:
Simply double-click the executable or run it without arguments.

## Requirements
- Windows 7 or later (for .exe)
- No Python installation required

## Troubleshooting
- If Windows Defender blocks the file, click "More info" and "Run anyway"
- For antivirus issues, add the executable to your antivirus whitelist

## Support
Report issues at: https://github.com/yourusername/yourrepo
"""
    
    with open(dist_dir / "README.txt", "w") as f:
        f.write(readme_content)
    
    print(f"\n✓ Distribution package created in '{dist_dir}/'")

def test_executable():
    """Test the built executable"""
    exe_name = f"{APP_NAME}.exe" if sys.platform == "win32" else APP_NAME
    exe_path = os.path.join("dist", exe_name)
    
    if not os.path.exists(exe_path):
        # Try directory mode
        exe_path = os.path.join("dist", APP_NAME, exe_name)
    
    if os.path.exists(exe_path):
        print(f"\nTesting executable: {exe_path}")
        print("-" * 50)
        
        # Test with --info flag
        result = subprocess.run([exe_path, "--info"], capture_output=True, text=True)
        print(result.stdout)
        
        if result.returncode == 0:
            print("✓ Executable test passed!")
            
            # Show file size
            size_mb = os.path.getsize(exe_path) / (1024 * 1024)
            print(f"✓ Executable size: {size_mb:.2f} MB")
            
            return True
    else:
        print(f"✗ Executable not found at {exe_path}")
    
    return False

def main():
    """Main build process"""
    print(f"{'='*60}")
    print(f"  Building {APP_NAME} v{APP_VERSION}")
    print(f"{'='*60}")
    
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='Build executable from Python script')
    parser.add_argument('--mode', choices=['onefile', 'onedir'], default='onefile',
                       help='Build mode: onefile (single exe) or onedir (folder with exe)')
    parser.add_argument('--no-test', action='store_true',
                       help='Skip testing the executable')
    parser.add_argument('--no-clean', action='store_true',
                       help='Do not clean previous builds')
    
    args = parser.parse_args()
    
    # Step 1: Check requirements
    if not check_requirements():
        print("Failed to install requirements")
        return 1
    
    # Step 2: Clean previous builds
    if not args.no_clean:
        print("\nCleaning previous builds...")
        clean_build_dirs()
    
    # Step 3: Build executable
    if not build_executable(args.mode):
        print("Build failed!")
        return 1
    
    # Step 4: Test executable
    if not args.no_test:
        if not test_executable():
            print("Warning: Executable test failed")
    
    # Step 5: Create distribution package
    create_distribution()
    
    print(f"\n{'='*60}")
    print("  BUILD COMPLETE!")
    print(f"{'='*60}")
    print(f"\n📦 Your executable is ready in the 'dist' folder")
    print(f"📁 Distribution package is in the 'distribution' folder")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())