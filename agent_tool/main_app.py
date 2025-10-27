"""
Agent Tool - Main GUI Application
A powerful automation tool for controlling mouse and keyboard
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import json
import os
import sys
from datetime import datetime
from agent_controller import AgentController, Action, ActionType, CommonTasks
import requests
import webbrowser

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AgentToolApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Agent Tool - Automation Assistant")
        self.geometry("1000x700")
        self.minsize(800, 600)
        
        # Initialize controller
        self.controller = AgentController()
        self.current_sequence = []
        
        # Configure grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create UI
        self.create_sidebar()
        self.create_main_panel()
        self.create_status_bar()
        
        # Check for updates on startup
        self.check_for_updates()
        
    def create_sidebar(self):
        """Create the sidebar with main controls"""
        sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_rowconfigure(8, weight=1)
        
        # Logo/Title
        logo_label = ctk.CTkLabel(
            sidebar, 
            text="🤖 Agent Tool", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # Main action buttons
        self.record_btn = ctk.CTkButton(
            sidebar,
            text="🔴 Start Recording",
            command=self.toggle_recording,
            fg_color="red",
            hover_color="darkred"
        )
        self.record_btn.grid(row=1, column=0, padx=20, pady=10)
        
        self.play_btn = ctk.CTkButton(
            sidebar,
            text="▶ Play Sequence",
            command=self.play_sequence,
            fg_color="green",
            hover_color="darkgreen"
        )
        self.play_btn.grid(row=2, column=0, padx=20, pady=10)
        
        self.pause_btn = ctk.CTkButton(
            sidebar,
            text="⏸ Pause",
            command=self.pause_execution,
            state="disabled"
        )
        self.pause_btn.grid(row=3, column=0, padx=20, pady=10)
        
        self.stop_btn = ctk.CTkButton(
            sidebar,
            text="⏹ Stop",
            command=self.stop_execution,
            state="disabled"
        )
        self.stop_btn.grid(row=4, column=0, padx=20, pady=10)
        
        # Separator
        separator = ttk.Separator(sidebar, orient='horizontal')
        separator.grid(row=5, column=0, sticky="ew", padx=20, pady=20)
        
        # File operations
        self.save_btn = ctk.CTkButton(
            sidebar,
            text="💾 Save Sequence",
            command=self.save_sequence
        )
        self.save_btn.grid(row=6, column=0, padx=20, pady=10)
        
        self.load_btn = ctk.CTkButton(
            sidebar,
            text="📁 Load Sequence",
            command=self.load_sequence
        )
        self.load_btn.grid(row=7, column=0, padx=20, pady=10)
        
        # Settings button at bottom
        self.settings_btn = ctk.CTkButton(
            sidebar,
            text="⚙ Settings",
            command=self.open_settings
        )
        self.settings_btn.grid(row=9, column=0, padx=20, pady=(10, 20), sticky="s")
        
    def create_main_panel(self):
        """Create the main panel with tabs"""
        main_panel = ctk.CTkFrame(self)
        main_panel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        main_panel.grid_columnconfigure(0, weight=1)
        main_panel.grid_rowconfigure(1, weight=1)
        
        # Tab view
        self.tabview = ctk.CTkTabview(main_panel)
        self.tabview.grid(row=0, column=0, sticky="nsew")
        
        # Create tabs
        self.sequence_tab = self.tabview.add("📝 Sequence Editor")
        self.quick_actions_tab = self.tabview.add("⚡ Quick Actions")
        self.macros_tab = self.tabview.add("🎯 Macros")
        self.logs_tab = self.tabview.add("📊 Logs")
        
        # Setup each tab
        self.setup_sequence_tab()
        self.setup_quick_actions_tab()
        self.setup_macros_tab()
        self.setup_logs_tab()
        
    def setup_sequence_tab(self):
        """Setup the sequence editor tab"""
        # Action list
        self.action_listbox = tk.Listbox(
            self.sequence_tab,
            bg="#2b2b2b",
            fg="white",
            selectbackground="#4a4a4a",
            font=("Consolas", 10)
        )
        self.action_listbox.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Control buttons frame
        control_frame = ctk.CTkFrame(self.sequence_tab)
        control_frame.pack(fill="x", padx=10, pady=(0, 10))
        
        ctk.CTkButton(
            control_frame,
            text="➕ Add Action",
            command=self.add_action_dialog,
            width=100
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            control_frame,
            text="✏ Edit",
            command=self.edit_action,
            width=100
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            control_frame,
            text="🗑 Delete",
            command=self.delete_action,
            width=100
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            control_frame,
            text="⬆ Move Up",
            command=self.move_action_up,
            width=100
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            control_frame,
            text="⬇ Move Down",
            command=self.move_action_down,
            width=100
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            control_frame,
            text="🔄 Clear All",
            command=self.clear_sequence,
            width=100,
            fg_color="red",
            hover_color="darkred"
        ).pack(side="right", padx=5)
        
    def setup_quick_actions_tab(self):
        """Setup quick actions tab"""
        quick_frame = ctk.CTkScrollableFrame(self.quick_actions_tab)
        quick_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Quick action buttons
        actions = [
            ("Open Notepad", lambda: self.quick_action("notepad")),
            ("Open Calculator", lambda: self.quick_action("calc")),
            ("Open Browser", lambda: self.quick_action("chrome")),
            ("Take Screenshot", self.take_screenshot),
            ("Type Date/Time", self.type_datetime),
            ("Minimize All Windows", self.minimize_all),
            ("Lock Computer", self.lock_computer),
            ("Open Task Manager", lambda: self.quick_action("taskmgr")),
        ]
        
        for i, (name, command) in enumerate(actions):
            btn = ctk.CTkButton(
                quick_frame,
                text=name,
                command=command,
                height=50,
                font=ctk.CTkFont(size=14)
            )
            btn.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="ew")
            
        quick_frame.grid_columnconfigure(0, weight=1)
        quick_frame.grid_columnconfigure(1, weight=1)
        
    def setup_macros_tab(self):
        """Setup macros tab for saved sequences"""
        macros_frame = ctk.CTkFrame(self.macros_tab)
        macros_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Macro list
        self.macro_listbox = tk.Listbox(
            macros_frame,
            bg="#2b2b2b",
            fg="white",
            selectbackground="#4a4a4a"
        )
        self.macro_listbox.pack(side="left", fill="both", expand=True)
        
        # Macro controls
        macro_controls = ctk.CTkFrame(macros_frame)
        macro_controls.pack(side="right", fill="y", padx=(10, 0))
        
        ctk.CTkButton(
            macro_controls,
            text="▶ Run Macro",
            command=self.run_macro
        ).pack(pady=5)
        
        ctk.CTkButton(
            macro_controls,
            text="📝 Edit Macro",
            command=self.edit_macro
        ).pack(pady=5)
        
        ctk.CTkButton(
            macro_controls,
            text="🗑 Delete Macro",
            command=self.delete_macro
        ).pack(pady=5)
        
        self.load_macros()
        
    def setup_logs_tab(self):
        """Setup logs tab"""
        self.log_text = tk.Text(
            self.logs_tab,
            bg="#1e1e1e",
            fg="#00ff00",
            font=("Consolas", 9),
            wrap="word"
        )
        self.log_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Log controls
        log_controls = ctk.CTkFrame(self.logs_tab)
        log_controls.pack(fill="x", padx=10, pady=(0, 10))
        
        ctk.CTkButton(
            log_controls,
            text="Clear Logs",
            command=self.clear_logs,
            width=100
        ).pack(side="right")
        
        self.log("Agent Tool started successfully")
        
    def create_status_bar(self):
        """Create status bar at bottom"""
        self.status_bar = ctk.CTkLabel(
            self,
            text="Ready | Press Ctrl+Shift+Esc for emergency stop",
            anchor="w"
        )
        self.status_bar.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=2)
        
    def toggle_recording(self):
        """Toggle recording state"""
        if not self.controller.recording:
            self.controller.start_recording()
            self.record_btn.configure(text="⏹ Stop Recording", fg_color="darkred")
            self.update_status("Recording... Click and type to record actions")
            self.log("Recording started")
        else:
            actions = self.controller.stop_recording()
            self.record_btn.configure(text="🔴 Start Recording", fg_color="red")
            self.current_sequence.extend(actions)
            self.refresh_sequence_display()
            self.update_status(f"Recording stopped. {len(actions)} actions recorded")
            self.log(f"Recording stopped: {len(actions)} actions captured")
            
    def play_sequence(self):
        """Play the current sequence"""
        if not self.current_sequence:
            messagebox.showwarning("No Sequence", "No sequence to play. Record or load a sequence first.")
            return
            
        self.controller.execute_sequence(self.current_sequence)
        self.play_btn.configure(state="disabled")
        self.pause_btn.configure(state="normal")
        self.stop_btn.configure(state="normal")
        self.update_status(f"Playing sequence with {len(self.current_sequence)} actions")
        self.log(f"Sequence playback started: {len(self.current_sequence)} actions")
        
    def pause_execution(self):
        """Pause execution"""
        if self.controller.is_paused:
            self.controller.resume()
            self.pause_btn.configure(text="⏸ Pause")
            self.update_status("Execution resumed")
        else:
            self.controller.pause()
            self.pause_btn.configure(text="▶ Resume")
            self.update_status("Execution paused")
            
    def stop_execution(self):
        """Stop execution"""
        self.controller.stop()
        self.play_btn.configure(state="normal")
        self.pause_btn.configure(state="disabled", text="⏸ Pause")
        self.stop_btn.configure(state="disabled")
        self.update_status("Execution stopped")
        self.log("Sequence playback stopped")
        
    def save_sequence(self):
        """Save current sequence to file"""
        if not self.current_sequence:
            messagebox.showwarning("No Sequence", "No sequence to save")
            return
            
        filepath = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filepath:
            self.controller.save_sequence(self.current_sequence, filepath)
            self.update_status(f"Sequence saved to {os.path.basename(filepath)}")
            self.log(f"Sequence saved: {filepath}")
            
    def load_sequence(self):
        """Load sequence from file"""
        filepath = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filepath:
            self.current_sequence = self.controller.load_sequence(filepath)
            self.refresh_sequence_display()
            self.update_status(f"Loaded {len(self.current_sequence)} actions")
            self.log(f"Sequence loaded: {filepath}")
            
    def add_action_dialog(self):
        """Open dialog to add new action"""
        dialog = ActionDialog(self, self.add_action_to_sequence)
        
    def add_action_to_sequence(self, action):
        """Add action to current sequence"""
        self.current_sequence.append(action)
        self.refresh_sequence_display()
        self.log(f"Action added: {action.description}")
        
    def edit_action(self):
        """Edit selected action"""
        selection = self.action_listbox.curselection()
        if selection:
            index = selection[0]
            action = self.current_sequence[index]
            dialog = ActionDialog(self, lambda a: self.update_action(index, a), action)
            
    def update_action(self, index, action):
        """Update action at index"""
        self.current_sequence[index] = action
        self.refresh_sequence_display()
        self.log(f"Action updated: {action.description}")
        
    def delete_action(self):
        """Delete selected action"""
        selection = self.action_listbox.curselection()
        if selection:
            index = selection[0]
            del self.current_sequence[index]
            self.refresh_sequence_display()
            self.log("Action deleted")
            
    def move_action_up(self):
        """Move selected action up"""
        selection = self.action_listbox.curselection()
        if selection and selection[0] > 0:
            index = selection[0]
            self.current_sequence[index], self.current_sequence[index-1] = \
                self.current_sequence[index-1], self.current_sequence[index]
            self.refresh_sequence_display()
            self.action_listbox.selection_set(index-1)
            
    def move_action_down(self):
        """Move selected action down"""
        selection = self.action_listbox.curselection()
        if selection and selection[0] < len(self.current_sequence) - 1:
            index = selection[0]
            self.current_sequence[index], self.current_sequence[index+1] = \
                self.current_sequence[index+1], self.current_sequence[index]
            self.refresh_sequence_display()
            self.action_listbox.selection_set(index+1)
            
    def clear_sequence(self):
        """Clear all actions"""
        if messagebox.askyesno("Clear Sequence", "Are you sure you want to clear all actions?"):
            self.current_sequence = []
            self.refresh_sequence_display()
            self.log("Sequence cleared")
            
    def refresh_sequence_display(self):
        """Refresh the sequence display"""
        self.action_listbox.delete(0, tk.END)
        for i, action in enumerate(self.current_sequence):
            self.action_listbox.insert(tk.END, f"{i+1}. {action.description}")
            
    def quick_action(self, app_name):
        """Execute quick action to open application"""
        actions = CommonTasks.open_application(app_name)
        self.controller.execute_sequence(actions)
        self.log(f"Quick action: Open {app_name}")
        
    def take_screenshot(self):
        """Take a screenshot"""
        action = Action(ActionType.SCREENSHOT, {'path': f'screenshot_{datetime.now():%Y%m%d_%H%M%S}.png'})
        self.controller.execute_action(action)
        self.log("Screenshot taken")
        
    def type_datetime(self):
        """Type current date and time"""
        text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        actions = CommonTasks.type_text(text)
        self.controller.execute_sequence(actions)
        
    def minimize_all(self):
        """Minimize all windows"""
        action = Action(ActionType.KEYBOARD_HOTKEY, {'keys': ['win', 'd']}, "Minimize all windows")
        self.controller.execute_action(action)
        
    def lock_computer(self):
        """Lock the computer"""
        action = Action(ActionType.KEYBOARD_HOTKEY, {'keys': ['win', 'l']}, "Lock computer")
        self.controller.execute_action(action)
        
    def load_macros(self):
        """Load saved macros"""
        macro_dir = "macros"
        if os.path.exists(macro_dir):
            for file in os.listdir(macro_dir):
                if file.endswith(".json"):
                    self.macro_listbox.insert(tk.END, file[:-5])
                    
    def run_macro(self):
        """Run selected macro"""
        selection = self.macro_listbox.curselection()
        if selection:
            macro_name = self.macro_listbox.get(selection[0])
            filepath = f"macros/{macro_name}.json"
            if os.path.exists(filepath):
                sequence = self.controller.load_sequence(filepath)
                self.controller.execute_sequence(sequence)
                self.log(f"Running macro: {macro_name}")
                
    def edit_macro(self):
        """Edit selected macro"""
        selection = self.macro_listbox.curselection()
        if selection:
            macro_name = self.macro_listbox.get(selection[0])
            filepath = f"macros/{macro_name}.json"
            if os.path.exists(filepath):
                self.current_sequence = self.controller.load_sequence(filepath)
                self.refresh_sequence_display()
                self.tabview.set("📝 Sequence Editor")
                
    def delete_macro(self):
        """Delete selected macro"""
        selection = self.macro_listbox.curselection()
        if selection:
            macro_name = self.macro_listbox.get(selection[0])
            if messagebox.askyesno("Delete Macro", f"Delete macro '{macro_name}'?"):
                filepath = f"macros/{macro_name}.json"
                if os.path.exists(filepath):
                    os.remove(filepath)
                    self.macro_listbox.delete(selection[0])
                    self.log(f"Macro deleted: {macro_name}")
                    
    def open_settings(self):
        """Open settings dialog"""
        SettingsDialog(self)
        
    def update_status(self, message):
        """Update status bar"""
        self.status_bar.configure(text=f"{message} | Press Ctrl+Shift+Esc for emergency stop")
        
    def log(self, message):
        """Add message to log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        
    def clear_logs(self):
        """Clear log text"""
        self.log_text.delete(1.0, tk.END)
        
    def check_for_updates(self):
        """Check for application updates"""
        try:
            # This would connect to your update server
            # For now, we'll just log that we checked
            self.log("Checking for updates...")
        except:
            pass

class ActionDialog(ctk.CTkToplevel):
    """Dialog for adding/editing actions"""
    
    def __init__(self, parent, callback, action=None):
        super().__init__(parent)
        self.callback = callback
        self.action = action
        
        self.title("Add Action" if action is None else "Edit Action")
        self.geometry("500x400")
        self.resizable(False, False)
        
        # Action type selection
        ctk.CTkLabel(self, text="Action Type:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.action_type = ctk.CTkComboBox(
            self,
            values=[t.value for t in ActionType],
            command=self.on_type_change
        )
        self.action_type.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        # Parameters frame
        self.params_frame = ctk.CTkFrame(self)
        self.params_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        # Description
        ctk.CTkLabel(self, text="Description:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.description = ctk.CTkEntry(self)
        self.description.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        # Buttons
        button_frame = ctk.CTkFrame(self)
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        ctk.CTkButton(button_frame, text="OK", command=self.on_ok).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Cancel", command=self.destroy).pack(side="left", padx=5)
        
        # Configure grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Load existing action if editing
        if action:
            self.action_type.set(action.type.value)
            self.description.insert(0, action.description)
            self.on_type_change(action.type.value)
            
    def on_type_change(self, value):
        """Update parameter fields based on action type"""
        # Clear existing widgets
        for widget in self.params_frame.winfo_children():
            widget.destroy()
            
        self.param_widgets = {}
        
        action_type = ActionType(value)
        
        if action_type in [ActionType.MOUSE_MOVE, ActionType.MOUSE_CLICK, 
                           ActionType.MOUSE_DOUBLE_CLICK, ActionType.MOUSE_RIGHT_CLICK]:
            ctk.CTkLabel(self.params_frame, text="X:").grid(row=0, column=0, padx=5, pady=5)
            self.param_widgets['x'] = ctk.CTkEntry(self.params_frame)
            self.param_widgets['x'].grid(row=0, column=1, padx=5, pady=5)
            
            ctk.CTkLabel(self.params_frame, text="Y:").grid(row=1, column=0, padx=5, pady=5)
            self.param_widgets['y'] = ctk.CTkEntry(self.params_frame)
            self.param_widgets['y'].grid(row=1, column=1, padx=5, pady=5)
            
        elif action_type == ActionType.KEYBOARD_TYPE:
            ctk.CTkLabel(self.params_frame, text="Text:").grid(row=0, column=0, padx=5, pady=5)
            self.param_widgets['text'] = ctk.CTkTextbox(self.params_frame, height=100)
            self.param_widgets['text'].grid(row=0, column=1, padx=5, pady=5)
            
        elif action_type == ActionType.KEYBOARD_PRESS:
            ctk.CTkLabel(self.params_frame, text="Key:").grid(row=0, column=0, padx=5, pady=5)
            self.param_widgets['key'] = ctk.CTkEntry(self.params_frame)
            self.param_widgets['key'].grid(row=0, column=1, padx=5, pady=5)
            
        elif action_type == ActionType.WAIT:
            ctk.CTkLabel(self.params_frame, text="Seconds:").grid(row=0, column=0, padx=5, pady=5)
            self.param_widgets['seconds'] = ctk.CTkEntry(self.params_frame)
            self.param_widgets['seconds'].grid(row=0, column=1, padx=5, pady=5)
            
        # Load existing values if editing
        if self.action and self.action.type == action_type:
            for key, widget in self.param_widgets.items():
                if key in self.action.params:
                    if isinstance(widget, ctk.CTkTextbox):
                        widget.insert("1.0", str(self.action.params[key]))
                    else:
                        widget.insert(0, str(self.action.params[key]))
                        
    def on_ok(self):
        """Save action and close"""
        action_type = ActionType(self.action_type.get())
        params = {}
        
        for key, widget in self.param_widgets.items():
            if isinstance(widget, ctk.CTkTextbox):
                value = widget.get("1.0", "end-1c")
            else:
                value = widget.get()
                
            if key in ['x', 'y']:
                params[key] = int(value) if value else 0
            elif key == 'seconds':
                params[key] = float(value) if value else 1.0
            else:
                params[key] = value
                
        action = Action(
            type=action_type,
            params=params,
            description=self.description.get() or f"{action_type.value}"
        )
        
        self.callback(action)
        self.destroy()

class SettingsDialog(ctk.CTkToplevel):
    """Settings dialog"""
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.title("Settings")
        self.geometry("400x300")
        self.resizable(False, False)
        
        # Settings options
        ctk.CTkLabel(self, text="Settings", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
        
        # Theme selection
        theme_frame = ctk.CTkFrame(self)
        theme_frame.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(theme_frame, text="Theme:").pack(side="left", padx=10)
        ctk.CTkComboBox(
            theme_frame,
            values=["dark", "light"],
            command=lambda v: ctk.set_appearance_mode(v)
        ).pack(side="left", padx=10)
        
        # Auto-update toggle
        self.auto_update = ctk.CTkCheckBox(self, text="Check for updates on startup")
        self.auto_update.pack(pady=10)
        
        # Hotkey settings
        ctk.CTkLabel(self, text="Emergency Stop: Ctrl+Shift+Esc", 
                    font=ctk.CTkFont(size=12)).pack(pady=10)
        
        # Close button
        ctk.CTkButton(self, text="Close", command=self.destroy).pack(pady=20)

if __name__ == "__main__":
    # Create macros directory if it doesn't exist
    os.makedirs("macros", exist_ok=True)
    
    app = AgentToolApp()
    app.mainloop()