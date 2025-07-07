
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import csv
import random, json
templates = json.load(open("message_templates.json", encoding="utf-8"))
def choose_template():
    return random.choice(list(templates.values()))

def login(driver, IG_ID, IG_PW):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)
    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    username_input.send_keys(IG_ID)
    password_input.send_keys(IG_PW)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

def run_followup_batch():
    service = Service("chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    login(driver, "gonggyu_gonggu", "qkr1008##!")

    with open("logs/responses.csv", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        responses = list(reader)

    for row in responses:
        uid = row["username"]
        print(f"🔁 후속 DM 발송 대상: {uid}")
        
message = choose_template()
print(f"   → Sending: {message}")
# TODO: Implement actual DM send using Selenium.

    print("✅ 전체 후속 DM 완료")
    driver.quit()

if __name__ == "__main__":
    run_followup_batch()
