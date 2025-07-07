# messenger.py 전체 덮어쓰기용

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

IG_ID = "yourish_insta"
IG_PW = "yourish007!"

def get_driver(headless: bool = False) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    service = webdriver.ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def login(driver: webdriver.Chrome) -> None:
    driver.get("https://www.instagram.com/accounts/login/")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))

    user_input = driver.find_element(By.NAME, "username")
    pass_input = driver.find_element(By.NAME, "password")

    user_input.clear(); user_input.send_keys(IG_ID)
    pass_input.clear(); pass_input.send_keys(IG_PW + Keys.ENTER)

    try:
        WebDriverWait(driver, 60).until(
            EC.any_of(
                EC.presence_of_element_located((By.XPATH, "//nav")),
                EC.presence_of_element_located((By.XPATH, "//main"))
            )
        )
        print("✅ 로그인 성공")

        # 팝업 '나중에 하기' 자동 클릭
        for label in ["나중에 하기", "Not Now"]:
            try:
                btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, f"//button[text()='{label}']"))
                )
                btn.click()
                print(f"ℹ️ 팝업 '{label}' 클릭 완료")
                time.sleep(1)
            except:
                continue

    except:
        raise RuntimeError("❌ 로그인 실패 - 아이디/비번 또는 인증 문제")

