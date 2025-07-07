===== OFFLINE PATCH v7 – keyword search 페이지 대응 =====
변경:
  • 페이지 로딩 판정: article → a[href*='/p/'] 로 교체
  • 스크롤 12회로 증가

설치:
  1) zip 압축을 풀어 아래 파일을 덮어쓰기
     E:\insta_crawler_prod\packages\offline\hashtag_crawler.py

  2) 실행
     cd E:\insta_crawler_prod\packages\offline
     python batch_runner.py