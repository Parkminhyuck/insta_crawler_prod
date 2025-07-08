
# account_crawler_offline.py
# 외부 PC / 오프라인 실행용 최소 예제 (테스트 페이지만 접속)

from driver_manager import get_chrome_driver
import time

def main():
    driver = get_chrome_driver(headless=True, ini='settings_offline.ini')
    try:
        driver.get('https://www.google.com')
        print('✅ 오프라인 모드: 구글 페이지 열림')
        time.sleep(2)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
