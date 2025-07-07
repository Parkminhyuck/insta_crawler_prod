
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 수동으로 다운로드한 크롬 드라이버 경로 설정
driver_path = "E:/insta_crawler_prod/chrome-win64/chromedriver.exe"  # 다운로드한 chromedriver.exe 파일 경로

# 크롬 옵션 설정
options = Options()
options.add_argument("--headless")  # 헤드리스 모드 설정
options.add_argument("--disable-gpu")  # GPU 사용 안함
options.add_argument("--no-sandbox")  # 보안 샌드박스 문제 우회
options.add_argument("--disable-software-rasterizer")  # 소프트웨어 방식 렌더링 강제
service = Service(driver_path)  # 서비스 객체 생성
driver = webdriver.Chrome(service=service, options=options)  # options만 전달

# 구글 페이지 열기
driver.get("https://www.google.com")
print("구글 페이지가 정상적으로 열렸습니다.")
driver.quit()
