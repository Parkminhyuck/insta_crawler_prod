
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def like_and_follow(driver, uid):
    try:
        profile_url = f"https://www.instagram.com/{uid}/"
        driver.get(profile_url)
        time.sleep(2)

        # 팔로우 버튼 클릭
        try:
            follow_btn = driver.find_element(By.XPATH, "//button[normalize-space()='팔로우']")
            follow_btn.click()
            print(f"✅ 팔로우: {uid}")
            time.sleep(1)
        except NoSuchElementException:
            print(f"⚠️ 팔로우 버튼 없음: {uid}")

        # 첫 번째 게시물 클릭해서 좋아요 누르기
        try:
            post = driver.find_element(By.CSS_SELECTOR, "article a[href*='/p/']")
            post.click()
            time.sleep(2)

            like_btn = driver.find_element(By.XPATH, "//section/span/button/div[*[name()='svg'][@aria-label='좋아요']]")
            like_btn.click()
            print(f"❤️ 좋아요: {uid}")
            time.sleep(1)

            # 닫기
            close_btn = driver.find_element(By.XPATH, "//div[@role='dialog']//button[contains(@aria-label, '닫기')]")
            close_btn.click()
        except Exception as e:
            print(f"⚠️ 좋아요 실패: {uid} - {e}")

    except Exception as e:
        print(f"❌ 전체 실패: {uid} - {e}")
