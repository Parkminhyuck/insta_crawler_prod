from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_dm_button(driver):
    # 여러 가지 셀렉터를 순차적으로 시도
    SELECTORS = [
        (By.CSS_SELECTOR, 'button[aria-label="Message"][role="button"]'),
        (By.XPATH, '//button//*[contains(text(), "Message")]/ancestor::button'),
        (By.CSS_SELECTOR, 'svg[aria-label="Direct"]')
    ]
    
    for by, selector in SELECTORS:
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((by, selector))
            )
            return element
        except:
            continue

    raise Exception("❌ DM 버튼을 찾을 수 없습니다.")
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_dm(driver, message):
    print("✉️ DM 입력창 탐색 중...")

    try:
        area = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea, div[contenteditable='true']"))
        )
        area.click()
        area.send_keys(message + Keys.ENTER)
        print("✅ DM 전송 완료")
    except Exception as e:
        print("❌ DM 입력 실패:", e)
