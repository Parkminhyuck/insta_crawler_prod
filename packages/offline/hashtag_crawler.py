import time
from selenium.webdriver.common.by import By

def crawl_hashtag_users(driver, segment: str, max_posts: int = 10, delay_multiplier: float = 1.0):
    """
    지정한 해시태그 페이지에서 최대 max_posts 개의 게시물 작성자 UID와
    해당 게시물 URL 리스트를 동시에 반환합니다.
    """
    uids = []
    post_urls = []

    url = f"https://www.instagram.com/explore/tags/{segment}/"
    driver.get(url)
    time.sleep(2 * delay_multiplier)

    # 페이지 스크롤로 추가 로딩
    for _ in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1 * delay_multiplier)

    # 게시물 링크 모으기
    links = driver.find_elements(By.CSS_SELECTOR, "article a")
    count = 0

    for elem in links:
        if count >= max_posts:
            break
        href = elem.get_attribute("href")
        if not href or href in post_urls:
            continue

        post_urls.append(href)
        driver.get(href)
        time.sleep(1 * delay_multiplier)

        try:
            # 프로필 헤더에서 UID 추출
            user_elem = driver.find_element(By.CSS_SELECTOR, "header a")
            uid = user_elem.get_attribute("href").rstrip("/").split("/")[-1]
            if uid not in uids:
                uids.append(uid)
                count += 1
        except Exception:
            pass

        driver.back()
        time.sleep(0.5 * delay_multiplier)

    return uids, post_urls
