"""
Auto-updater module for Agent Tool
Handles checking for updates and downloading/installing new versions
"""

import os
import sys
import json
import requests
import hashlib
import tempfile
import subprocess
import threading
from typing import Optional, Dict, Tuple
from packaging import version
import zipfile
import shutil

class AutoUpdater:
    """Handles automatic updates for the application"""
    
    def __init__(self, current_version: str, update_url: str):
        """
        Initialize the auto-updater
        
        Args:
            current_version: Current version of the application
            update_url: URL to check for updates (should return JSON)
        """
        self.current_version = current_version
        self.update_url = update_url
        self.update_info = None
        
    def check_for_updates(self) -> Tuple[bool, Optional[Dict]]:
        """
        Check if updates are available
        
        Returns:
            Tuple of (update_available, update_info)
        """
        try:
            # Fetch update information from server
            response = requests.get(self.update_url, timeout=10)
            response.raise_for_status()
            
            update_data = response.json()
            latest_version = update_data.get('version', '0.0.0')
            
            # Compare versions
            if version.parse(latest_version) > version.parse(self.current_version):
                self.update_info = update_data
                return True, update_data
            
            return False, None
            
        except requests.RequestException as e:
            print(f"Error checking for updates: {e}")
            return False, None
        except Exception as e:
            print(f"Unexpected error during update check: {e}")
            return False, None
    
    def download_update(self, progress_callback=None) -> Optional[str]:
        """
        Download the update file
        
        Args:
            progress_callback: Function to call with download progress (0-100)
            
        Returns:
            Path to downloaded file or None if failed
        """
        if not self.update_info:
            return None
            
        download_url = self.update_info.get('download_url')
        file_hash = self.update_info.get('hash')
        file_size = self.update_info.get('size', 0)
        
        if not download_url:
            print("No download URL in update info")
            return None
            
        try:
            # Create temporary file
            temp_dir = tempfile.gettempdir()
            temp_file = os.path.join(temp_dir, 'agent_tool_update.exe')
            
            # Download with progress
            response = requests.get(download_url, stream=True)
            response.raise_for_status()
            
            downloaded = 0
            chunk_size = 8192
            
            with open(temp_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        if progress_callback and file_size > 0:
                            progress = int((downloaded / file_size) * 100)
                            progress_callback(progress)
            
            # Verify file hash if provided
            if file_hash and not self.verify_file_hash(temp_file, file_hash):
                os.remove(temp_file)
                print("File hash verification failed")
                return None
                
            return temp_file
            
        except Exception as e:
            print(f"Error downloading update: {e}")
            return None
    
    def verify_file_hash(self, file_path: str, expected_hash: str) -> bool:
        """
        Verify the SHA256 hash of a file
        
        Args:
            file_path: Path to file to verify
            expected_hash: Expected SHA256 hash
            
        Returns:
            True if hash matches, False otherwise
        """
        sha256_hash = hashlib.sha256()
        
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
                
        calculated_hash = sha256_hash.hexdigest()
        return calculated_hash.lower() == expected_hash.lower()
    
    def install_update(self, update_file: str) -> bool:
        """
        Install the downloaded update
        
        Args:
            update_file: Path to the update file
            
        Returns:
            True if installation started successfully
        """
        try:
            if not os.path.exists(update_file):
                print("Update file not found")
                return False
                
            # Create update script
            update_script = self.create_update_script(update_file)
            
            # Execute update script
            if sys.platform == 'win32':
                # On Windows, start the updater and exit current process
                subprocess.Popen([update_script], shell=True)
                return True
            else:
                # On other platforms, might need different approach
                subprocess.Popen(['sh', update_script])
                return True
                
        except Exception as e:
            print(f"Error installing update: {e}")
            return False
    
    def create_update_script(self, update_file: str) -> str:
        """
        Create a script to perform the update
        
        Args:
            update_file: Path to the update file
            
        Returns:
            Path to the update script
        """
        if sys.platform == 'win32':
            # Windows batch script
            script_content = f"""@echo off
echo Waiting for application to close...
timeout /t 3 /nobreak > nul
echo Installing update...
move /Y "{update_file}" "{sys.executable}"
echo Update complete!
echo Starting application...
start "" "{sys.executable}"
del "%~f0"
"""
            script_path = os.path.join(tempfile.gettempdir(), 'update_agent_tool.bat')
            
        else:
            # Unix shell script
            script_content = f"""#!/bin/bash
echo "Waiting for application to close..."
sleep 3
echo "Installing update..."
mv -f "{update_file}" "{sys.executable}"
chmod +x "{sys.executable}"
echo "Update complete!"
echo "Starting application..."
"{sys.executable}" &
rm -f "$0"
"""
            script_path = os.path.join(tempfile.gettempdir(), 'update_agent_tool.sh')
            
        with open(script_path, 'w') as f:
            f.write(script_content)
            
        if sys.platform != 'win32':
            os.chmod(script_path, 0o755)
            
        return script_path
    
    def perform_update_check_async(self, callback):
        """
        Perform update check in background thread
        
        Args:
            callback: Function to call with results (update_available, update_info)
        """
        def check():
            result = self.check_for_updates()
            callback(*result)
            
        thread = threading.Thread(target=check, daemon=True)
        thread.start()
    
    def get_changelog(self) -> Optional[str]:
        """
        Get changelog for the available update
        
        Returns:
            Changelog text or None
        """
        if self.update_info:
            return self.update_info.get('changelog', 'No changelog available')
        return None

class UpdateServer:
    """
    Simple update server implementation for testing
    In production, this would be a proper web service
    """
    
    @staticmethod
    def generate_update_manifest(version: str, download_url: str, 
                                file_path: str, changelog: str = "") -> Dict:
        """
        Generate update manifest JSON
        
        Args:
            version: Version string
            download_url: URL where update can be downloaded
            file_path: Path to the update file (for hash calculation)
            changelog: Changelog text
            
        Returns:
            Update manifest dictionary
        """
        # Calculate file hash
        file_hash = ""
        file_size = 0
        
        if os.path.exists(file_path):
            sha256_hash = hashlib.sha256()
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            file_hash = sha256_hash.hexdigest()
            file_size = os.path.getsize(file_path)
        
        manifest = {
            "version": version,
            "download_url": download_url,
            "hash": file_hash,
            "size": file_size,
            "changelog": changelog,
            "release_date": "2024-01-01",
            "minimum_version": "1.0.0",  # Minimum version that can update to this
            "critical": False,  # Whether this is a critical update
        }
        
        return manifest
    
    @staticmethod
    def save_manifest(manifest: Dict, output_path: str):
        """Save update manifest to file"""
        with open(output_path, 'w') as f:
            json.dump(manifest, f, indent=2)

# Example usage in main application
def integrate_updater(app_instance, version="1.0.0", update_url="https://yourserver.com/updates/manifest.json"):
    """
    Integrate auto-updater into the main application
    
    Args:
        app_instance: Instance of the main application
        version: Current application version
        update_url: URL to check for updates
    """
    updater = AutoUpdater(version, update_url)
    
    def on_update_check_complete(update_available, update_info):
        """Callback when update check is complete"""
        if update_available:
            # Show update dialog in main thread
            app_instance.after(0, lambda: show_update_dialog(app_instance, updater, update_info))
    
    # Check for updates on startup
    updater.perform_update_check_async(on_update_check_complete)
    
    return updater

def show_update_dialog(parent, updater, update_info):
    """Show update available dialog"""
    import tkinter as tk
    from tkinter import messagebox
    
    version = update_info.get('version', 'Unknown')
    changelog = updater.get_changelog()
    
    message = f"A new version ({version}) is available!\n\n"
    message += f"Changelog:\n{changelog}\n\n"
    message += "Would you like to download and install it now?"
    
    if messagebox.askyesno("Update Available", message):
        # Start download
        download_and_install(parent, updater)

def download_and_install(parent, updater):
    """Download and install update with progress dialog"""
    import tkinter as tk
    from tkinter import ttk
    
    # Create progress dialog
    progress_dialog = tk.Toplevel(parent)
    progress_dialog.title("Downloading Update")
    progress_dialog.geometry("400x150")
    progress_dialog.resizable(False, False)
    
    label = tk.Label(progress_dialog, text="Downloading update...")
    label.pack(pady=20)
    
    progress_bar = ttk.Progressbar(progress_dialog, length=350, mode='determinate')
    progress_bar.pack(pady=10)
    
    status_label = tk.Label(progress_dialog, text="0%")
    status_label.pack()
    
    def update_progress(value):
        progress_bar['value'] = value
        status_label['text'] = f"{value}%"
        progress_dialog.update()
    
    def download_thread():
        update_file = updater.download_update(update_progress)
        
        if update_file:
            progress_dialog.destroy()
            
            if messagebox.askyesno("Install Update", 
                                  "Update downloaded successfully. Install now?\n\n"
                                  "The application will restart after installation."):
                if updater.install_update(update_file):
                    parent.quit()  # Exit application for update
        else:
            progress_dialog.destroy()
            messagebox.showerror("Update Error", "Failed to download update")
    
    # Start download in background thread
    import threading
    thread = threading.Thread(target=download_thread, daemon=True)
    thread.start()

if __name__ == "__main__":
    # Example: Generate update manifest for testing
    manifest = UpdateServer.generate_update_manifest(
        version="1.1.0",
        download_url="https://yourserver.com/downloads/AgentTool_1.1.0.exe",
        file_path="dist/AgentTool.exe",  # Path to your built executable
        changelog="- Added new automation features\n- Improved UI\n- Bug fixes"
    )
    
    UpdateServer.save_manifest(manifest, "update_manifest.json")
    print("Update manifest created: update_manifest.json")