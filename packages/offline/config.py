# packages/offline/config.py

import os
import json

# 프로젝트 루트의 settings.json 경로
ROOT = os.path.dirname(os.path.abspath(__file__))       # .../packages/offline
PROJECT_ROOT = os.path.dirname(os.path.dirname(ROOT))   # .../packages
PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)            # .../insta_crawler_prod
SETTINGS_PATH = os.path.join(PROJECT_ROOT, 'settings.json')

def load_settings():
    """루트의 settings.json 을 읽어 dict 로 반환합니다."""
    if not os.path.isfile(SETTINGS_PATH):
        raise FileNotFoundError(f"settings.json을 찾을 수 없습니다: {SETTINGS_PATH}")
    with open(SETTINGS_PATH, encoding='utf-8') as f:
        return json.load(f)
