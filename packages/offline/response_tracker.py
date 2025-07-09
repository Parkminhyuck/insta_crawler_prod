# response_tracker.py

import os
import json
import time
from datetime import datetime

LOG_DIR = "logs"
REPORT_FILE = os.path.join(LOG_DIR, "response_report.json")

def track_responses():
    """
    보낸 DM에 대한 응답을 추적하고, 결과를 보고서 파일로 저장합니다.
    """
    print("🔎 응답 추적 시작...")
    responses = []

    # logs 폴더 안의 모든 log 파일을 뒤져서 응답 데이터를 수집합니다.
    for fname in os.listdir(LOG_DIR):
        if not fname.endswith(".log"):
            continue
        path = os.path.join(LOG_DIR, fname)
        with open(path, encoding="utf-8") as f:
            for line in f:
                # 예: "[2025-07-08 15:00:00] ✔ Response received from @user123"
                if "✔ Response received" in line:
                    timestamp, msg = line.split("] ", 1)
                    user = msg.split()[-1]
                    responses.append({
                        "user": user.strip(),
                        "time": timestamp.strip("[")
                    })

    # JSON 보고서로 저장
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(REPORT_FILE, "w", encoding="utf-8") as outf:
        json.dump(responses, outf, ensure_ascii=False, indent=2)

    print(f"✅ 응답 추적 완료, {len(responses)}건 저장 → {REPORT_FILE}")
