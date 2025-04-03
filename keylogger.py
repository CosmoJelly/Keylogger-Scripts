import time
import csv
import json
import os
from pynput import keyboard

# File names
csv_file = "keystroke_data.csv"
json_file = "keystroke_data.json"

# Load previous session data from JSON
if os.path.exists(json_file):
    with open(json_file, "r") as f:
        try:
            keystrokes = json.load(f)
        except json.JSONDecodeError:
            keystrokes = []
else:
    keystrokes = []

# Function to handle key press events
def on_press(key):
    try:
        key_char = key.char if hasattr(key, 'char') else str(key)
    except AttributeError:
        key_char = str(key)
    
    timestamp = time.time()
    keystroke_entry = {"key": key_char, "timestamp": timestamp}
    keystrokes.append(keystroke_entry)
    
    print(f"Key: {key_char}, Time: {timestamp:.4f}s")
    
    # Append to CSV
    with open(csv_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([key_char, timestamp])
    
    # Save to JSON
    with open(json_file, "w") as f:
        json.dump(keystrokes, f, indent=4)

# Ensure CSV file has a header if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Key", "Timestamp (s)"])

# Set up listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
