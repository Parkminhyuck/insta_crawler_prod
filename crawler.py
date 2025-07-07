# crawler.py
"""
해시태그 → 게시물 URL → 사용자 ID 수집용 최소 버전
selenium driver 객체를 인자로 받아 동작
"""
import time, random
from selenium.webdriver.common.by import By

SEL_THUMB = "a[href*='/p/'][tabindex]"
SCROLL_PX = 1600

def crawl_tag(driver, tag: str, limit_posts: int = 60):
    driver.get(f"https://www.instagram.com/explore/tags/{tag}/")
    time.sleep(2)
    urls, seen = [], set()
    while len(urls) < limit_posts:
        for a in driver.find_elements(By.CSS_SELECTOR, SEL_THUMB):
            u = a.get_attribute("href")
            if u and u not in seen:
                urls.append(u); seen.add(u)
                if len(urls) >= limit_posts:
                    break
        driver.execute_script(f"window.scrollBy(0,{SCROLL_PX});")
        time.sleep(random.uniform(1.5, 2.5))
    return urls

def username_from_post(driver, url: str) -> str:
    driver.get(url); time.sleep(2)
    return driver.find_element(By.XPATH, "//header//a").text.replace("@", "")
