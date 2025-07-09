import argparse
import json
import os
import logging

from .config import load_settings
from .driver_manager import get_chrome_driver
from .auth import login
from .hashtag_crawler import crawl_hashtag_users
from .account_worker import process_account
from .messenger import send_message
from .response_tracker import track_responses
from .report_generator import generate_report

def run_crawler(segment: str, limit: int, dm_enabled: bool = True):
    # ─── 1) 설정 로드 ───────────────────────────────
    cfg = load_settings()
    INST = cfg["INSTAGRAM"]
    USERNAME = INST["username"]
    PASSWORD = INST["password"]
    multiplier = cfg.get("DELAY", {}).get("multiplier", 1.0)

    # ─── 2) 드라이버 생성 + 로그인 ───────────────────
    driver = get_chrome_driver(headless=False)
    login(driver, USERNAME, PASSWORD)
    logging.info(f"▶️ 크롤 시작: segment={segment}, limit={limit}")

    # ─── 3) 해시태그 크롤 → UID + URL 수집 ─────────────
    uids, post_urls = crawl_hashtag_users(driver, segment, limit, multiplier)
    # 수집된 게시물 URL도 JSON으로 저장
    os.makedirs("logs", exist_ok=True)
    with open("logs/collected_posts.json", "w", encoding="utf-8") as f:
        json.dump(post_urls, f, ensure_ascii=False, indent=2)
    logging.info(f"✅ Collected {len(post_urls)} post URLs → logs/collected_posts.json")

    # ─── 4) 계정별 처리 + DM 전송 ──────────────────────
    for uid in uids:
        process_account(driver, uid)
        if dm_enabled:
            # 메시지 템플릿 로드 (config 또는 별도 모듈에서)
            msg = cfg.get("MESSAGE_TEMPLATE", "안녕하세요!")
            success = send_message(driver, uid, msg)
            logging.info(f"DM to {uid}: {'성공' if success else '실패'}")

    # ─── 5) 응답 추적 & 보고서 생성 ────────────────────
    track_responses()
    generate_report()

    # ─── 6) 드라이버 종료 ───────────────────────────
    driver.quit()
    logging.info("✅ 매크로 전체 파이프라인 완료")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--segment", required=True, help="segmentation key")
    ap.add_argument("--limit", type=int, default=10, help="max posts per tag")
    ap.add_argument("--dm_enabled", action="store_true", help="DM 전송 활성화")
    args = ap.parse_args()
    run_crawler(args.segment, args.limit, args.dm_enabled)
