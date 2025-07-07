import sys
from packages.offline.auth import login
from packages.offline.hashtag_crawler import crawl_hashtag_users

def run_crawler(segment):
    driver = login()
    crawl_hashtag_users(driver, segment)
    driver.quit()

if __name__ == "__main__":
    segment = sys.argv[2] if len(sys.argv)>=3 and sys.argv[1]=='--segment' else "공구"
    run_crawler(segment)
