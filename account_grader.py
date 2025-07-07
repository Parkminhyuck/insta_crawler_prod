
"""account_grader.py – patched (2025‑07)

get_followers(driver)  함수 포함 버전
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_followers(driver, timeout: int = 30) -> int:
    """현재 프로필 페이지에서 팔로워 수 정수로 반환.
       0 을 반환하면 파싱 실패
    """
    try:
        elem = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//li//a[contains(@href,'followers')]/span/span | //li//a[contains(@href,'followers')]/span")
            )
        )
        raw = elem.get_attribute('title') or elem.text
        raw = raw.replace(',', '').replace('.', '').replace('명', '')
        return int(raw)
    except Exception:
        return 0
