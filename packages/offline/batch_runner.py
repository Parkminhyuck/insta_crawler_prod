import sys, os
# 프로젝트 루트를 PYTHONPATH에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from offline.auth import login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from offline.hashtag_crawler import crawl_hashtag_users

def run_crawler(segment):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    login(driver)
    crawl_hashtag_users(driver, segment)
    driver.quit()

if __name__ == '__main__':
    import sys
    segment = sys.argv[2] if len(sys.argv) >= 3 and sys.argv[1]=='--segment' else "공구"
    run_crawler(segment)
