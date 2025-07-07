import time
from selenium.webdriver.common.by import By

def login(driver, username, password):
    print("🔐 로그인 페이지 접속...")
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    id_input = driver.find_element(By.NAME, "username")
    pw_input = driver.find_element(By.NAME, "password")

    id_input.send_keys(username)
    pw_input.send_keys(password)

    login_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_btn.click()

    print(f"🔓 로그인 시도 완료: {username}")
    time.sleep(4)
