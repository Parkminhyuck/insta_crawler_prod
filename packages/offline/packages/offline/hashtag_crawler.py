from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def crawl_hashtag_users(driver, tag):
    url = f"https://www.instagram.com/explore/tags/{tag}/"
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article div img"))
        )
    except TimeoutException:
        print(f"⚠️ 태그 #{tag} 로딩 실패: Timeout waiting for images")
        return
    posts = driver.find_elements(By.CSS_SELECTOR, "article div a")
    for post in posts:
        href = post.get_attribute("href")
        if href:
            print(href)
