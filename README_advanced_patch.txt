===== ADVANCED PATCH =====
• hashtag_crawler.py v13 – UID 추출 강화(JS + ld+json + meta), 디버그 출력
• follow_helper.py – 팔로우 여부 확인 & 팔로우 실행
• batch_runner.py – 좋아요 → (필요시 팔로우) → DM, CSV 기록 포함

설치:
  1. 압축 해제하여 세 파일을
     E:\insta_crawler_prod\packages\offline\ 에 덮어쓰기
  2. 실행
     cd E:\insta_crawler_prod\packages\offline
     python batch_runner.py
     python report_generator.py