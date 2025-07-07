import os
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "logs")
SCREENSHOT_DIR = os.path.join(LOG_DIR, "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def log_error(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join(LOG_DIR, "errors.log"), "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def get_screenshot_path(uid: str):
    filename = f"{uid}_error.png"
    return os.path.join(SCREENSHOT_DIR, filename)
