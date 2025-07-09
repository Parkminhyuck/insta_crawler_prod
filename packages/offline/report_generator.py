import os
import json
import pandas as pd
from datetime import datetime

LOG_DIR    = "logs"
EXCEL_FILE = os.path.join(LOG_DIR, "response_report.xlsx")
CSV_FILE   = os.path.join(LOG_DIR, "response_report.csv")

def generate_report():
    """
    logs/response_report.json 을 읽어
    엑셀 및 CSV 보고서를 동시에 생성합니다.
    """
    # JSON 읽기
    json_path = os.path.join(LOG_DIR, "response_report.json")
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    # DataFrame 생성
    df = pd.DataFrame(data)

    os.makedirs(LOG_DIR, exist_ok=True)

    # 엑셀 저장
    with pd.ExcelWriter(EXCEL_FILE, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Responses")
    print(f"✅ 엑셀 보고서 생성 → {EXCEL_FILE}")

    # CSV 저장
    df.to_csv(CSV_FILE, index=False, encoding="utf-8-sig")
    print(f"✅ CSV 보고서 생성 → {CSV_FILE}")