"""
Agent Controller - Core automation module for mouse and keyboard control
"""

import pyautogui
import keyboard
import mouse
import time
import json
import os
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import threading
import queue

# Safety features
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

class ActionType(Enum):
    """Types of actions the agent can perform"""
    MOUSE_MOVE = "mouse_move"
    MOUSE_CLICK = "mouse_click"
    MOUSE_DOUBLE_CLICK = "mouse_double_click"
    MOUSE_RIGHT_CLICK = "mouse_right_click"
    MOUSE_DRAG = "mouse_drag"
    KEYBOARD_TYPE = "keyboard_type"
    KEYBOARD_PRESS = "keyboard_press"
    KEYBOARD_HOTKEY = "keyboard_hotkey"
    WAIT = "wait"
    SCREENSHOT = "screenshot"

@dataclass
class Action:
    """Represents a single automation action"""
    type: ActionType
    params: Dict
    description: str = ""

class AgentController:
    """Main controller for automation actions"""
    
    def __init__(self):
        self.actions_queue = queue.Queue()
        self.is_running = False
        self.is_paused = False
        self.recorded_actions: List[Action] = []
        self.recording = False
        self.execution_thread = None
        
        # Set up emergency stop hotkey
        keyboard.add_hotkey('ctrl+shift+escape', self.emergency_stop)
        
    def emergency_stop(self):
        """Emergency stop for all operations"""
        self.is_running = False
        self.is_paused = False
        self.recording = False
        print("Emergency stop activated!")
        
    def start_recording(self):
        """Start recording user actions"""
        self.recording = True
        self.recorded_actions = []
        
        # Set up listeners
        mouse.on_click(self._record_mouse_click)
        keyboard.on_press(self._record_keyboard)
        
    def stop_recording(self) -> List[Action]:
        """Stop recording and return recorded actions"""
        self.recording = False
        mouse.unhook_all()
        keyboard.unhook_all()
        return self.recorded_actions
        
    def _record_mouse_click(self):
        """Record mouse click events"""
        if self.recording:
            x, y = pyautogui.position()
            action = Action(
                type=ActionType.MOUSE_CLICK,
                params={"x": x, "y": y},
                description=f"Click at ({x}, {y})"
            )
            self.recorded_actions.append(action)
            
    def _record_keyboard(self, event):
        """Record keyboard events"""
        if self.recording and event.event_type == 'down':
            action = Action(
                type=ActionType.KEYBOARD_PRESS,
                params={"key": event.name},
                description=f"Press key: {event.name}"
            )
            self.recorded_actions.append(action)
    
    def execute_action(self, action: Action) -> bool:
        """Execute a single action"""
        try:
            if action.type == ActionType.MOUSE_MOVE:
                pyautogui.moveTo(
                    action.params.get('x', 0),
                    action.params.get('y', 0),
                    duration=action.params.get('duration', 0.5)
                )
                
            elif action.type == ActionType.MOUSE_CLICK:
                pyautogui.click(
                    x=action.params.get('x'),
                    y=action.params.get('y'),
                    button=action.params.get('button', 'left')
                )
                
            elif action.type == ActionType.MOUSE_DOUBLE_CLICK:
                pyautogui.doubleClick(
                    x=action.params.get('x'),
                    y=action.params.get('y')
                )
                
            elif action.type == ActionType.MOUSE_RIGHT_CLICK:
                pyautogui.rightClick(
                    x=action.params.get('x'),
                    y=action.params.get('y')
                )
                
            elif action.type == ActionType.MOUSE_DRAG:
                pyautogui.dragTo(
                    action.params.get('x', 0),
                    action.params.get('y', 0),
                    duration=action.params.get('duration', 1),
                    button=action.params.get('button', 'left')
                )
                
            elif action.type == ActionType.KEYBOARD_TYPE:
                pyautogui.typewrite(
                    action.params.get('text', ''),
                    interval=action.params.get('interval', 0.05)
                )
                
            elif action.type == ActionType.KEYBOARD_PRESS:
                pyautogui.press(action.params.get('key', ''))
                
            elif action.type == ActionType.KEYBOARD_HOTKEY:
                keys = action.params.get('keys', [])
                if keys:
                    pyautogui.hotkey(*keys)
                    
            elif action.type == ActionType.WAIT:
                time.sleep(action.params.get('seconds', 1))
                
            elif action.type == ActionType.SCREENSHOT:
                screenshot = pyautogui.screenshot()
                if 'path' in action.params:
                    screenshot.save(action.params['path'])
                return screenshot
                
            return True
            
        except Exception as e:
            print(f"Error executing action {action.type}: {e}")
            return False
    
    def execute_sequence(self, actions: List[Action], loop: bool = False):
        """Execute a sequence of actions"""
        self.is_running = True
        
        def run():
            while self.is_running:
                for action in actions:
                    if not self.is_running:
                        break
                        
                    while self.is_paused:
                        time.sleep(0.1)
                        
                    success = self.execute_action(action)
                    if not success:
                        print(f"Failed to execute action: {action.description}")
                        
                if not loop:
                    break
                    
            self.is_running = False
            
        self.execution_thread = threading.Thread(target=run)
        self.execution_thread.start()
        
    def pause(self):
        """Pause execution"""
        self.is_paused = True
        
    def resume(self):
        """Resume execution"""
        self.is_paused = False
        
    def stop(self):
        """Stop execution"""
        self.is_running = False
        if self.execution_thread:
            self.execution_thread.join(timeout=2)
    
    def save_sequence(self, actions: List[Action], filepath: str):
        """Save an action sequence to a file"""
        data = []
        for action in actions:
            data.append({
                'type': action.type.value,
                'params': action.params,
                'description': action.description
            })
            
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
            
    def load_sequence(self, filepath: str) -> List[Action]:
        """Load an action sequence from a file"""
        with open(filepath, 'r') as f:
            data = json.load(f)
            
        actions = []
        for item in data:
            action = Action(
                type=ActionType(item['type']),
                params=item['params'],
                description=item.get('description', '')
            )
            actions.append(action)
            
        return actions
    
    def get_mouse_position(self) -> Tuple[int, int]:
        """Get current mouse position"""
        return pyautogui.position()
    
    def get_screen_size(self) -> Tuple[int, int]:
        """Get screen dimensions"""
        return pyautogui.size()
    
    def find_on_screen(self, image_path: str, confidence: float = 0.8) -> Optional[Tuple[int, int]]:
        """Find an image on screen and return its center coordinates"""
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            return location
        except:
            return None

# Predefined common automation tasks
class CommonTasks:
    """Collection of common automation tasks"""
    
    @staticmethod
    def open_application(app_name: str) -> List[Action]:
        """Open an application using Windows Run dialog"""
        return [
            Action(ActionType.KEYBOARD_HOTKEY, {'keys': ['win', 'r']}, "Open Run dialog"),
            Action(ActionType.WAIT, {'seconds': 0.5}, "Wait for dialog"),
            Action(ActionType.KEYBOARD_TYPE, {'text': app_name}, f"Type {app_name}"),
            Action(ActionType.KEYBOARD_PRESS, {'key': 'enter'}, "Press Enter"),
        ]
    
    @staticmethod
    def type_text(text: str, delay: float = 0.05) -> List[Action]:
        """Type text with specified delay"""
        return [
            Action(ActionType.KEYBOARD_TYPE, {'text': text, 'interval': delay}, f"Type: {text[:50]}...")
        ]
    
    @staticmethod
    def click_at_position(x: int, y: int) -> List[Action]:
        """Click at specific position"""
        return [
            Action(ActionType.MOUSE_CLICK, {'x': x, 'y': y}, f"Click at ({x}, {y})")
        ]
    
    @staticmethod
    def copy_paste() -> List[Action]:
        """Copy and paste action"""
        return [
            Action(ActionType.KEYBOARD_HOTKEY, {'keys': ['ctrl', 'c']}, "Copy"),
            Action(ActionType.WAIT, {'seconds': 0.2}, "Wait"),
            Action(ActionType.KEYBOARD_HOTKEY, {'keys': ['ctrl', 'v']}, "Paste"),
        ]