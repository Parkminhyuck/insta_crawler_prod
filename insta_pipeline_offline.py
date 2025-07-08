
"""insta_pipeline_offline.py

외부 PC / 오프라인 전용 전체 파이프라인:
- 로그인
- 해시태그 기반 계정 수집
- 필터링 + 좋아요 + DM 발송

루트 모듈(import)을 위해 sys.path에 프로젝트 상위 경로 추가.
"""

import sys, pathlib, time
from configparser import ConfigParser

# ---------- 프로젝트 루트 경로 등록 ----------
ROOT = pathlib.Path(__file__).resolve().parents[2]   # insta_crawler_prod
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# ---------- 내부 모듈 import ----------
from driver_manager import get_chrome_driver
from auth import login
from hashtag_crawler import crawl_hashtag_users
from dm_sender import get_dm_button, send_dm
from liker import like_recent_posts
from account_grader import get_followers
from test_flow_utils import wait_for_profile_header

# ---------- 설정 읽기 ----------
CFG = ConfigParser()
CFG.read('settings_offline.ini', encoding='utf-8')

USERNAME = CFG.get('INSTAGRAM', 'username')
PASSWORD = CFG.get('INSTAGRAM', 'password')

HASHTAGS = [tag.strip('# ') for tag in CFG.get('CRAWLER','hashtags').split(',')]
MAX_POSTS = CFG.getint('CRAWLER','max_posts', fallback=60)

# ---------- 계정 처리 ----------
def process_account(driver, uid:str):
    try:
        driver.get(f"https://www.instagram.com/{uid}/")
        wait_for_profile_header(driver, timeout=10)
        followers = get_followers(driver)
        print(f"{uid} ▶ 팔로워 {followers:,}")
        like_recent_posts(driver, num_posts=2)
        if btn := get_dm_button(driver):
            send_dm(driver, "요약콘텐츠로 공구 제안드려요")
            print("✉️ DM 전송 완료")
        time.sleep(1)
    except Exception as e:
        print("⚠️", uid, "처리 실패:", e)

# ---------- 메인 루틴 ----------
def main():
    driver = get_chrome_driver(headless=True, ini='settings_offline.ini')
    try:
        login(driver, USERNAME, PASSWORD)
        uids = crawl_hashtag_users(driver, HASHTAGS, max_posts_per_tag=20, max_accounts=50)
        print("총 수집", len(uids), "계정")
        for uid in uids:
            process_account(driver, uid)
    finally:
        driver.quit()
        print("🔒 종료")

if __name__ == '__main__':
    main()
