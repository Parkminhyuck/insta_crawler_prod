# batch_runner.py – 로그인 인자 및 드라이버 호출 수정 (2025‑07‑08)

import argparse
from configparser import ConfigParser
from driver_manager import get_chrome_driver
from auth import login
from hashtag_crawler import crawl_hashtag_users
from account_worker import process_account

def run_crawler(segment, limit):
    # 설정 읽기
    cfg = ConfigParser()
    cfg.read('settings_offline.ini', encoding='utf-8')
    USERNAME = cfg.get('INSTAGRAM', 'username')
    PASSWORD = cfg.get('INSTAGRAM', 'password')

    # 드라이버 생성 및 로그인
    driver = get_chrome_driver(headless=False)
    login(driver, USERNAME, PASSWORD)

    # 크롤링 & 계정 처리
    uids = crawl_hashtag_users(driver, segment, max_posts=limit, delay=cfg.getfloat('DELAY', 'multiplier', fallback=1.0))
    for uid in uids:
        process_account(driver, uid)

    driver.quit()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--segment", required=True, help="segmentation key")
    ap.add_argument("--limit", type=int, default=10, help="max posts per tag")
    args = ap.parse_args()
    run_crawler(args.segment, args.limit)