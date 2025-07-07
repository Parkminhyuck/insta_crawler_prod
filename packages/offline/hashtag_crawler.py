from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def crawl_hashtag_users(driver, tag):
    url = f"https://www.instagram.com/explore/tags/{tag}/"
    driver.get(url)
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article div div div div"))
        )
    except TimeoutException:
        print(f"⚠️ 태그 #{tag} 로딩 실패: Timeout")
        return
    posts = driver.find_elements(By.CSS_SELECTOR, "article div div div div a")
    for post in posts:
        print(post.get_attribute("href"))
