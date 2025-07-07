from selenium import webdriver

def crawl_hashtag_users(segment, tag):
    # 올바르게 드라이버 초기화
    driver = webdriver.Chrome(executable_path="path_to_chromedriver")  # chromedriver 경로 설정
    
    # URL 생성
    url = f"https://www.instagram.com/explore/tags/{segment}/"
    
    # 웹 페이지 로딩
    driver.get(url)

    # 그 외 크롤링 작업...

    driver.quit()  # 크롤링이 끝난 후 드라이버 종료
