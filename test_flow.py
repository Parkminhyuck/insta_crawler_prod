
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 크롬 옵션 설정
options = Options()
options.add_argument("--headless")  # 원한다면 헤드리스 모드 추가
options.add_argument("--disable-gpu")

# 크롬 드라이버 설치 및 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 구글 페이지 열기
driver.get("https://www.google.com")

# 페이지가 정상적으로 열리면 종료
print("구글 페이지가 정상적으로 열렸습니다.")
driver.quit()
