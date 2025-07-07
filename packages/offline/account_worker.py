# account_worker.py – Follow/Like/DM pipeline
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def _click(driver, elem):
    driver.execute_script("arguments[0].click()", elem)

def follow_if_needed(driver):
    try:
        btn = WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.XPATH,"//button[.='Follow' or .='팔로우']"))
        )
        _click(driver,btn)
        time.sleep(0.8)
    except:
        pass  # already following

def like_first_post(driver):
    try:
        post = WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"article a[href*='/p/']"))
        )
        _click(driver,post)
        like_btn = WebDriverWait(driver,8).until(
            EC.element_to_be_clickable((By.XPATH,"//section//span/*[@aria-label='Like' or @aria-label='좋아요']"))
        )
        _click(driver,like_btn)
        time.sleep(0.8)
        driver.find_element(By.TAG_NAME,"body").send_keys(Keys.ESCAPE)
    except Exception as e:
        print("⚠️ 좋아요 실패:",e)

def send_dm(driver,message:str):
    try:
        dm = WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.XPATH,"//div[@role='button' and (text()='Message' or text()='메시지')]"))
        )
        _click(driver,dm)
        area = WebDriverWait(driver,8).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"textarea, div[contenteditable='true']"))
        )
        area.send_keys(message+Keys.ENTER)
        return True
    except Exception as e:
        print("⚠️ DM 실패:",e)
        return False

def process(driver, uid:str, message:str, delay:float=1.0):
    driver.get(f"https://www.instagram.com/{uid}/")
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"header")))
    except: return False
    follow_if_needed(driver)
    like_first_post(driver)
    ok = send_dm(driver,message)
    time.sleep(delay)
    return ok