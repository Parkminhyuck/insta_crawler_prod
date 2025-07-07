===== BATCH + LOGGER PATCH =====
• batch_runner.py – log_processed(uid, …) 자동 호출 추가
  성공/실패 모두 logs/processed_accounts.csv 에 기록.

덮어쓰기:
  E:\insta_crawler_prod\packages\offline\batch_runner.py

이후 실행:
  cd E:\insta_crawler_prod\packages\offline
  python batch_runner.py        # CSV 생성
  python report_generator.py    # 엑셀 생성