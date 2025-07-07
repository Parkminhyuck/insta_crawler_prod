
import json
from pathlib import Path

def load_templates():
    file_path = Path("config/message_templates.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_dm_message(account_type="default"):
    templates = load_templates()
    if account_type in templates:
        return templates[account_type]["preview"], templates[account_type]["message"]
    return templates["default"]["preview"], templates["default"]["message"]
