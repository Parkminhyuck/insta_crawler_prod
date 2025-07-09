import time
from selenium.webdriver.common.by import By
from .test_flow_utils import wait_for_profile_header

def process_account(driver, uid, delay=1.0):
    """
    UID의 프로필로 직접 이동. 스크롤 & 대기 로직을 통해 헤더 로딩 안정화.
    """
    profile_url = f"https://www.instagram.com/{uid}/"
    driver.get(profile_url)
    # 헤더 완전 로딩 대기
    wait_for_profile_header(driver, timeout=10)
    # 예시: 프로필 정보 추출
    # username = driver.find_element(By.CSS_SELECTOR, "section span > h1").text
    # print(f"Processed profile: {username}")
    time.sleep(delay)