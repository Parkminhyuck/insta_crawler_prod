import csv, os, datetime, json

LOG_FILE = "logs/app.log"
os.makedirs("logs", exist_ok=True)

def log_result(uid, result):
    # result can be dict or tuple
    if isinstance(result, tuple):
        success, message = (result + (None, None))[:2]
    elif isinstance(result, dict):
        success = result.get("success")
        message = result.get("message")
    else:
        success = False
        message = str(result)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        ts = datetime.datetime.now().isoformat(timespec="seconds")
        f.write(json.dumps({"uid": uid,
                            "success": bool(success),
                            "message": message,
                            "timestamp": ts},
                           ensure_ascii=False) + "\n")