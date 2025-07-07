import sys
from packages.offline.auth import login
from packages.offline.hashtag_crawler import crawl_hashtag_users

def main():
    if len(sys.argv) >= 3 and sys.argv[1] == '--segment':
        segment = sys.argv[2]
    else:
        print("Usage: python main.py --segment <해시태그>")
        return
    driver = login()
    crawl_hashtag_users(driver, segment)
    driver.quit()

if __name__ == "__main__":
    main()
