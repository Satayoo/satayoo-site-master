#!/usr/bin/env python3
"""
Sample Python Application
Demonstrates a simple CLI app that can be converted to .exe
"""

import sys
import os
import json
import argparse
from datetime import datetime

# Handle paths for both development and compiled executable
def get_base_path():
    """Get the base path for the application"""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        return sys._MEIPASS
    else:
        # Running as script
        return os.path.dirname(os.path.abspath(__file__))

class SimpleApp:
    """Simple demonstration application"""
    
    def __init__(self):
        self.base_path = get_base_path()
        self.config_file = os.path.join(self.base_path, 'config.json')
        self.load_config()
    
    def load_config(self):
        """Load configuration from file or create default"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            else:
                self.config = {
                    'app_name': 'Sample Application',
                    'version': '1.0.0',
                    'last_run': None
                }
                self.save_config()
        except Exception as e:
            print(f"Error loading config: {e}")
            self.config = {}
    
    def save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def run(self, args):
        """Main application logic"""
        print(f"\n{'='*50}")
        print(f"  {self.config.get('app_name', 'App')} v{self.config.get('version', '1.0')}")
        print(f"{'='*50}\n")
        
        if args.info:
            self.show_info()
        elif args.process:
            self.process_data(args.process)
        else:
            self.interactive_menu()
        
        # Update last run time
        self.config['last_run'] = datetime.now().isoformat()
        self.save_config()
    
    def show_info(self):
        """Display application information"""
        print("Application Information:")
        print(f"- Name: {self.config.get('app_name')}")
        print(f"- Version: {self.config.get('version')}")
        print(f"- Last Run: {self.config.get('last_run', 'Never')}")
        print(f"- Python Version: {sys.version}")
        print(f"- Executable: {'Yes' if getattr(sys, 'frozen', False) else 'No'}")
        print(f"- Path: {sys.executable}")
    
    def process_data(self, data):
        """Process some data (example functionality)"""
        print(f"Processing: {data}")
        # Simulate some processing
        result = data.upper()
        print(f"Result: {result}")
        
        # Save to output file
        output_file = 'output.txt'
        with open(output_file, 'w') as f:
            f.write(f"Processed at {datetime.now()}\n")
            f.write(f"Input: {data}\n")
            f.write(f"Output: {result}\n")
        print(f"Results saved to {output_file}")
    
    def interactive_menu(self):
        """Interactive menu for the application"""
        while True:
            print("\nMain Menu:")
            print("1. Show Info")
            print("2. Process Text")
            print("3. Settings")
            print("4. Exit")
            
            choice = input("\nSelect option (1-4): ").strip()
            
            if choice == '1':
                self.show_info()
            elif choice == '2':
                text = input("Enter text to process: ")
                self.process_data(text)
            elif choice == '3':
                self.settings_menu()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    
    def settings_menu(self):
        """Settings submenu"""
        print("\nCurrent Settings:")
        for key, value in self.config.items():
            print(f"  {key}: {value}")
        
        change = input("\nChange app name? (y/n): ").lower()
        if change == 'y':
            new_name = input("Enter new app name: ")
            self.config['app_name'] = new_name
            self.save_config()
            print("Settings updated!")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Sample Python Application')
    parser.add_argument('--info', action='store_true', help='Show application info')
    parser.add_argument('--process', type=str, help='Process text data')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
    
    args = parser.parse_args()
    
    try:
        app = SimpleApp()
        app.run(args)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()