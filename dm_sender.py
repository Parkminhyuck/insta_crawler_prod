from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_dm_button(driver):
    selectors = [
        (By.CSS_SELECTOR, 'button[aria-label="Message"][role="button"]'),
        (By.XPATH, '//button//*[contains(text(), "Message")]/ancestor::button'),
        (By.CSS_SELECTOR, 'svg[aria-label="Direct"]')
    ]
    for by, sel in selectors:
        try:
            return WebDriverWait(driver, 5).until(EC.element_to_be_clickable((by, sel)))
        except:
            continue
    raise Exception("DM 버튼 찾기 실패")

def send_dm(driver, message):
    try:
        area = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea, div[contenteditable='true']"))
        )
        area.click()
        area.send_keys(message + Keys.ENTER)
        print("✅ DM 전송 완료")
    except Exception as e:
        print("❌ DM 입력 실패:", e)