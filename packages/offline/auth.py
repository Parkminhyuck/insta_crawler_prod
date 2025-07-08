
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def login(driver, username, password):
    """로그인 후 페이지 로딩 안정화 처리"""
    print("🔐 로그인 페이지 접속...")
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    id_input = driver.find_element(By.NAME, "username")
    pw_input = driver.find_element(By.NAME, "password")

    id_input.clear()
    id_input.send_keys(username)
    pw_input.clear()
    pw_input.send_keys(password)
    pw_input.submit()

    # 홈 네비게이션 바가 보일 때까지 대기
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "nav"))
        )
        print("🔓 로그인 성공 및 네비게이션 감지")
    except TimeoutException:
        print("⚠️ 로그인 후 네비게이션 감지 타임아웃")

    # 알림 팝업 '나중에 하기' 자동 클릭
    for label in ["나중에 하기", "Not Now", "나중에"]:
        try:
            btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[text()='{label}']"))
            )
            btn.click()
            print(f"ℹ️ 팝업 '{label}' 클릭 완료")
            time.sleep(1)
        except:
            pass
