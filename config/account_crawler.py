
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 설정
def setup_driver():
    options = Options()
    options.add_argument("--headless")  # 헤드리스 모드 설정
    options.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# 해시태그 크롤링 함수
def crawl_hashtag_accounts(driver, hashtags, max_posts_per_tag=20):
    collected = set()

    for tag in hashtags:
        print(f"🔎 해시태그 #{tag} 수집 중...")
        url = f"https://www.instagram.com/explore/tags/{tag}/"
        driver.get(url)
        time.sleep(3)

        # 게시물 링크 수집
        links = driver.find_elements(By.CSS_SELECTOR, "article a")
        posts = [a.get_attribute("href") for a in links if "/p/" in a.get_attribute("href")][:max_posts_per_tag]

        for post_url in posts:
            driver.get(post_url)
            time.sleep(1)
            try:
                username = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "header a"))
                ).text
                if username not in collected:
                    collected.add(username)
                    print(f"수집된 계정: {username}")
            except:
                continue

    return list(collected)

# 실행 예시
if __name__ == "__main__":
    hashtags = ["공구", "공동구매", "공구예정"]  # 해시태그 목록
    driver = setup_driver()
    accounts = crawl_hashtag_accounts(driver, hashtags)
    print(f"수집된 계정 목록: {accounts}")
    driver.quit()
