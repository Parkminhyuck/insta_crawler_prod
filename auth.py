from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import config

def login():
    options = Options()
    options.headless = False
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.instagram.com/accounts/login/")

    # Accept cookie banner if present
    try:
        btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept All']"))
        )
        btn.click()
    except:
        pass

    # Wait for login form
    

# ----- Handle 'Save your login info?' prompt -----
try:
    save_info_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(text(),'나중에 하기') or contains(text(),'Not Now') or contains(text(),'나중에') or contains(text(),'나중')]"
        ))
    )
    save_info_btn.click()
# ---- Robust wait for home feed ----
try:
    WebDriverWait(driver, 60).until(
        EC.any_of(
            EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Home']")),
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/home')]")),
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/']"))
        )
    )
except TimeoutException:
    driver.save_screenshot("login_wait_timeout.png")
    raise
# -----------------------------------

except TimeoutException:
    pass  # prompt not shown
# -------------------------------------------------
# --- Patched July 8 2025: robust home element wait ---
try:
    WebDriverWait(driver, 40).until(
        EC.any_of(
            EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Home']")),
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/home')]")),
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/']"))
        )
    )
except TimeoutException:
    # 캡처 후 에러 전파
    driver.save_screenshot("login_timeout.png")
    raise
# -----------------------------------------------------

        EC.url_changes("https://www.instagram.com/accounts/login/")
    )))
    driver.find_element(By.NAME, "username").send_keys(config.USERNAME)
    pwd = driver.find_element(By.NAME, "password")
    pwd.send_keys(config.PASSWORD)
    pwd.send_keys(Keys.RETURN)

    # Wait until Home icon indicates login success
    
# --- Patched July 8 2025: robust home element wait ---
try:
    WebDriverWait(driver, 40).until(
        EC.any_of(
            EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Home']")),
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/home')]")),
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/']"))
        )
    )
except TimeoutException:
    # 캡처 후 에러 전파
    driver.save_screenshot("login_timeout.png")
    raise
# -----------------------------------------------------

        EC.url_changes("https://www.instagram.com/accounts/login/")
    ))
    )
    return driver
