import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def login(driver, username: str, password: str):
    """
    1) 로그인 페이지 접속
    2) ID/PW 입력 후 로그인 버튼 클릭
    3) 홈 아이콘 또는 오류 메시지 감지
    4) 알림 팝업 처리
    """
    os.makedirs("logs/screenshots", exist_ok=True)

    print("🔐 로그인 페이지 접속...")
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(1)

    # 1) 계정 정보 입력
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    except Exception:
        driver.save_screenshot("logs/screenshots/login_input_timeout.png")
        raise RuntimeError("❌ 로그인 입력 단계 타임아웃")

    # 2) 홈 아이콘 또는 오류 메시지 대기
    wait = WebDriverWait(driver, 10)
    try:
        # 홈 아이콘이 뜨면 성공
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "svg[aria-label='홈']")))
        print("✅ 로그인 성공 및 피드 감지")
    except TimeoutException:
        # 오류 메시지(잘못된 비밀번호 등) 감지
        try:
            err = driver.find_element(By.ID, "slfErrorAlert")
            msg = err.text.strip()
            driver.save_screenshot("logs/screenshots/login_failed.png")
            raise RuntimeError(f"❌ 로그인 실패: {msg}")
        except NoSuchElementException:
            screenshot = "logs/screenshots/login_feed_timeout.png"
            driver.save_screenshot(screenshot)
            raise RuntimeError(f"⚠️ 로그인 후 피드 로딩 타임아웃, 스크린샷 → {screenshot}")

    # 3) 알림 팝업 처리
    for label in ("나중에 하기", "Not Now", "나중에"):
        try:
            btn = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[text()='{label}']"))
            )
            btn.click()
            time.sleep(0.5)
            break
        except Exception:
            continue
