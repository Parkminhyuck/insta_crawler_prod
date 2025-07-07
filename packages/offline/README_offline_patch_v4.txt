========== OFFLINE PATCH v4 ==========
• 문제: dm_sender 모듈 미존재 / 경로 오류
• 내용: batch_runner.py 경로 수정 + dm_sender.py 포함

설치:
  1) zip 파일을 풀어 아래 두 파일을 덮어쓰기
     E:\insta_crawler_prod\packages\offline\batch_runner.py
     E:\insta_crawler_prod\packages\offline\dm_sender.py

  2) 실행
     cd E:\insta_crawler_prod\packages\offline
     python batch_runner.py