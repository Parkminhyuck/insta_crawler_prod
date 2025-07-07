from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def is_following(driver)->bool:
    try:
        btn = driver.find_element(By.XPATH, "//button//*[text()='팔로잉' or text()='Following' or text()='친구' or text()='Friends']/ancestor::button")
        return True
    except:
        return False

def follow_account(driver)->None:
    try:
        btn = WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.XPATH, "//button//*[text()='팔로우' or text()='Follow']/ancestor::button"))
        )
        btn.click()
        time.sleep(1.5)
    except Exception as e:
        print("❌ 팔로우 실패:", e)