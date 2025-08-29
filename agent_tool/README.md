# Agent Tool - Windows Automation Assistant

A powerful Windows automation tool that can record and replay mouse and keyboard actions, similar to macro recording software but with advanced features for creating complex automation sequences.

## Features

### Core Functionality
- **🔴 Record & Replay**: Record your mouse movements, clicks, and keyboard inputs, then replay them automatically
- **⚡ Quick Actions**: Pre-configured actions for common tasks (open apps, take screenshots, etc.)
- **📝 Sequence Editor**: Visual editor to create, edit, and organize automation sequences
- **🎯 Macro Management**: Save and organize your automation sequences as reusable macros
- **🛑 Emergency Stop**: Press `Ctrl+Shift+Esc` at any time to immediately stop all automation

### Advanced Features
- **Mouse Control**:
  - Click, double-click, right-click
  - Drag and drop operations
  - Precise coordinate targeting
  - Image recognition for dynamic positioning

- **Keyboard Control**:
  - Type text with customizable speed
  - Send individual key presses
  - Execute keyboard shortcuts
  - Support for special keys

- **Automation Features**:
  - Wait/delay between actions
  - Loop sequences
  - Conditional execution
  - Screenshot capture
  - Window management

### User Interface
- Modern dark theme interface
- Tabbed organization
- Real-time action logging
- Visual sequence editor
- Status monitoring

## System Requirements

- **OS**: Windows 10 or later (64-bit)
- **RAM**: 4GB minimum
- **Storage**: 100MB free space
- **Python**: 3.8 or later (for development)
- **Permissions**: Administrator privileges for installation

## Installation Methods

### Method 1: Using the Installer (Recommended for End Users)

1. Download the latest installer: `AgentTool_Setup_1.0.0.exe`
2. Run the installer as Administrator
3. Follow the installation wizard
4. Launch Agent Tool from Start Menu or Desktop

### Method 2: Building from Source

#### Prerequisites
1. Install Python 3.8+ from [python.org](https://www.python.org/)
2. Install Git (optional, for cloning)
3. Install Inno Setup (optional, for creating installer) from [jrsoftware.org](https://jrsoftware.org/isdl.php)

#### Build Steps

##### Windows (Automated Build)
```batch
# Navigate to the agent_tool directory
cd agent_tool

# Run the build script
build.bat
```

##### Manual Build
```bash
# Install dependencies
pip install -r requirements.txt

# Run the build script
python build_installer.py
```

The build process will:
1. Install all required Python packages
2. Create the standalone executable using PyInstaller
3. Generate the installer using Inno Setup (if available)
4. Output files will be in the `dist` directory

## Project Structure

```
agent_tool/
├── agent_controller.py    # Core automation engine
├── main_app.py            # GUI application
├── auto_updater.py        # Auto-update functionality
├── build_installer.py     # Build automation script
├── installer_config.iss   # Inno Setup configuration
├── requirements.txt       # Python dependencies
├── build.bat             # Windows build script
├── macros/               # Saved macro files
└── dist/                 # Build output directory
```

## Usage Guide

### Recording Actions
1. Click "🔴 Start Recording"
2. Perform the actions you want to automate
3. Click "⏹ Stop Recording"
4. Your actions are now saved in the sequence

### Playing Sequences
1. Ensure you have a recorded or loaded sequence
2. Click "▶ Play Sequence"
3. The tool will replay your actions
4. Use "⏸ Pause" or "⏹ Stop" to control playback

### Creating Custom Sequences
1. Go to the "Sequence Editor" tab
2. Click "➕ Add Action"
3. Select action type and configure parameters
4. Arrange actions using the up/down buttons
5. Save your sequence for later use

### Using Quick Actions
1. Go to the "Quick Actions" tab
2. Click any preset action button
3. The action executes immediately

### Managing Macros
1. Save sequences as macros using "💾 Save Sequence"
2. Load saved macros with "📁 Load Sequence"
3. Organize macros in the "Macros" tab

## Safety Features

- **Failsafe**: Move mouse to screen corner to abort
- **Emergency Stop**: `Ctrl+Shift+Esc` stops all operations
- **Pause Control**: Pause execution at any time
- **Action Delays**: Built-in delays prevent system overload

## Development

### Setting Up Development Environment

```bash
# Clone the repository (if using git)
git clone <repository-url>
cd agent_tool

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application in development mode
python main_app.py
```

### Creating the Installer

The project uses multiple methods to create installers:

1. **Inno Setup** (Recommended):
   - Install Inno Setup
   - Run `build_installer.py`
   - Installer is created automatically

2. **NSIS** (Alternative):
   - Install NSIS
   - Compile `installer_nsis.nsi`

3. **PyInstaller Only**:
   - Creates standalone `.exe` without installer
   - Located in `dist/AgentTool.exe`

### Adding New Features

1. **New Action Types**: Add to `ActionType` enum in `agent_controller.py`
2. **GUI Components**: Modify `main_app.py`
3. **Quick Actions**: Add to `setup_quick_actions_tab()` method

## Auto-Update System

The application includes an auto-update system that:
1. Checks for updates on startup
2. Downloads updates in the background
3. Verifies file integrity with SHA256
4. Installs updates automatically

To deploy updates:
1. Build new version
2. Generate update manifest using `auto_updater.py`
3. Host files on your update server
4. Update manifest URL in the application

## Troubleshooting

### Common Issues

**Application won't start**
- Ensure you have administrator privileges
- Check Windows Defender/Antivirus settings
- Verify all dependencies are installed

**Recording doesn't work**
- Grant accessibility permissions
- Disable other macro software
- Run as administrator

**Build fails**
- Update pip: `python -m pip install --upgrade pip`
- Clear build directories: `rmdir /s build dist`
- Reinstall dependencies

**Installer creation fails**
- Ensure Inno Setup is installed
- Check path in `build_installer.py`
- Use NSIS as alternative

## Security Considerations

- The tool requires system-level access for automation
- Windows Defender may flag it as potentially unwanted
- Add to antivirus exceptions if needed
- Never run untrusted macro sequences
- Be cautious with automation that involves sensitive data

## License

MIT License - See LICENSE.txt for details

## Support

For issues, questions, or contributions:
- Create an issue in the repository
- Contact support at support@yourwebsite.com

## Acknowledgments

Built with:
- PyAutoGUI for automation
- CustomTkinter for modern UI
- PyInstaller for executable creation
- Inno Setup for installer generation

---

**Note**: This tool is for legitimate automation purposes only. Users are responsible for compliance with all applicable laws and regulations.