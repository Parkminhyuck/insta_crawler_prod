import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from dm_sender import get_dm_button, send_dm
from liker import like_recent_posts
from test_flow_utils import wait_for_profile_header

def follow_if_needed(driver, uid, delay=1.0):
    try:
        btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,
                "//button[.='Follow' or .='팔로우' or .='팔로잉']"
            ))
        )
        text = btn.text.strip()
        if text in ('Follow', '팔로우'):
            btn.click()
            time.sleep(delay)
            print(f"✅ Followed: {uid}")
        else:
            print(f"ℹ️ Already following: {uid}")
    except TimeoutException:
        print(f"⚠️ Follow button not found for {uid}")

def like_first_post(driver, num_posts=1, delay=1.0):
    try:
        thumbs = driver.find_elements(By.CSS_SELECTOR, "article a[href*='/p/']")[:num_posts]
        if thumbs:
            driver.execute_script("arguments[0].click();", thumbs[0])
            like_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//section//span/*[(local-name()='svg') and (@aria-label='Like' or @aria-label='좋아요')]"
                ))
            )
            like_btn.click()
            time.sleep(delay)
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            time.sleep(delay)
            print("✅ Liked a post")
        else:
            print("ℹ️ No posts to like")
    except Exception as e:
        print(f"⚠️ Like failed: {e}")

def process_account(driver, uid):
    print(f"▶ Processing account: {uid}")
    driver.get(f"https://www.instagram.com/{uid}/")
    wait_for_profile_header(driver, timeout=10)
    follow_if_needed(driver, uid)
    like_first_post(driver)
    try:
        dm_btn = get_dm_button(driver)
        if dm_btn:
            dm_btn.click()
            time.sleep(1)
            send_dm(driver, "요약콘텐츠로 공구 제안드려요")
            print("✉️ DM 전송 완료")
        else:
            print(f"⚠️ DM button not found for {uid}")
    except Exception as e:
        print(f"⚠️ DM send failed: {e}")
    time.sleep(1)