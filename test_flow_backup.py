# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from auth import login
from liker import like_recent_posts
from dm_sender import get_dm_button, send_dm
from account_grader import get_followers
from test_flow_utils import wait_for_profile_header

USERNAME = "gonggyu_gonggu"
PASSWORD = "qkr1008##!"
TARGET_UIDS = ["gonggyu_gonggu", "another_test_user"]
MIN_FOLLOWERS = 1000
MAX_FOLLOWERS = 100000
DM_TEMPLATE = "요약콘텐츠로 공구 제안드려요"

def create_driver(headless: bool = False) -> webdriver.Chrome:
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("prefs", {"intl.accept_languages": "ko-KR"})
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_window_size(1280, 1000)
    return driver

def process_account(driver: webdriver.Chrome, uid: str) -> None:
    from time import sleep
    from traceback import print_exc
    try:
        print(f"🚀 실행 ▶ 계정: {uid}")
        driver.get(f"https://www.instagram.com/{uid}/")
        wait_for_profile_header(driver)

        followers = get_followers(driver)
        print(f"STEP 6 ▶ 팔로워 수: {followers:,}")
        if not MIN_FOLLOWERS <= followers <= MAX_FOLLOWERS:
            print("❌ 대상 제외: 팔로워 수 조건 불충족")
            return

        like_recent_posts(driver, num_posts=3)
        print("❤️ 최근 게시물 3개 좋아요 완료")

        dm_btn = get_dm_button(driver)
        if not dm_btn:
            print("❌ DM 버튼 탐색 실패 – 비공개 계정이거나 메시지 차단")
            return

        send_dm(driver, DM_TEMPLATE)
        print("✉️  DM 전송 완료")
    except Exception:
        print("❌ 예외 발생:")
        print_exc()
    finally:
        sleep(2)

def main():
    driver = create_driver(headless=False)
    try:
        login(driver, USERNAME, PASSWORD)
        for uid in TARGET_UIDS:
            process_account(driver, uid)
    finally:
        driver.quit()
        print("\n🔒 테스트 완료, 드라이버 종료")

if __name__ == "__main__":
    main()
