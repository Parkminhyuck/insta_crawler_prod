
import argparse
import time
from datetime import datetime
from hashtag_crawler import crawl_hashtag_users
from driver_manager import get_chrome_driver
from dm_sender import send_dm
from response_tracker import like_and_follow

def is_dm_time():
    now = datetime.now()
    return 0 <= now.hour < 3

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    tags = ["공구", "공동구매", "공구예정"]
    driver = get_chrome_driver()

    for tag in tags:
        print(f"▶ TAG: #{tag}")
        uids = crawl_hashtag_users(driver, tag, max_posts=args.limit, delay=1.0)
        print(f"  🔍 Collected {len(uids)} UIDs")

        for uid in uids:
            if is_dm_time():
                print(f"💬 DM 대상: {uid}")
                send_dm(driver, uid)
            else:
                print(f"👍 좋아요 & 팔로우 대상: {uid}")
                like_and_follow(driver, uid)

            time.sleep(1)

    driver.quit()

if __name__ == "__main__":
    main()
