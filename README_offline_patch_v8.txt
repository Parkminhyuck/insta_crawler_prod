===== OFFLINE PATCH v8 — div 썸네일 & lazy load 대응 =====
변경점
  • selector: a[href*='/p/'] + div[role='link'][tabindex='0']
  • 스크롤 15회, 각 0.8s 대기 (lazy‑load 안정)
  • 수집 링크 개수 콘솔 로그

덮어쓰기
  E:\insta_crawler_prod\packages\offline\hashtag_crawler.py

실행
  cd E:\insta_crawler_prod\packages\offline
  python batch_runner.py