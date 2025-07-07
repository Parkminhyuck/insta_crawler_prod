
# account_crawler.py – flexible driver version
from driver_manager import get_chrome_driver
import time

def main():
    driver = get_chrome_driver(headless=True)
    try:
        driver.get("https://www.google.com")
        print("✔ 구글 페이지 열림")
        time.sleep(2)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
