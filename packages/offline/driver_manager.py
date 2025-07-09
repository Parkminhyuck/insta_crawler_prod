# packages/offline/driver_manager.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_chrome_driver(headless=False):
    """
    크롬 드라이버 생성 함수.
    headless=True 로 호출하면 브라우저 창을 표시하지 않습니다.
    """
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    # 필요에 따라 추가 옵션을 넣으실 수 있습니다.
    service = Service("chrome-win64/chromedriver.exe")
    return webdriver.Chrome(service=service, options=options)
