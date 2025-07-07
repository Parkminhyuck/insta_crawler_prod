===== OFFLINE PATCH v6 – 썸네일 클릭 우회 =====
• JS로 href 링크 수집 후 driver.get(post_url) 방식으로 계정 추출
• 클릭 불가 이슈 해결

덮어쓰기:
  E:\insta_crawler_prod\packages\offline\hashtag_crawler.py

실행:
  cd E:\insta_crawler_prod\packages\offline
  python batch_runner.py