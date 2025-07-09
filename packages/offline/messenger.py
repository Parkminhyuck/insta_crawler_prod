"""
messenger.py
– Instagram DM 전송 모듈
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_message(driver, uid: str, message: str) -> bool:
    try:
        # 1) 프로필 이동
        driver.get(f"https://www.instagram.com/{uid}/")
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='메시지']"))
        ).click()
        # 2) 입력창 대기
        textarea = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea"))
        )
        textarea.send_keys(message)
        # 3) 보내기
        send_btn = driver.find_element(By.XPATH, "//button[text()='보내기']")
        send_btn.click()
        return True
    except Exception:
        return False

__all__ = ["send_message"]
