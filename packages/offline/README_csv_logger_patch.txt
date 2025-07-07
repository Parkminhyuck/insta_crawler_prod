===== CSV LOGGER PATCH (Option 1) =====
파일:
  • logger.py  – log_processed() 추가 (logs/processed_accounts.csv 자동 기록)

덮어쓰기:
  E:\insta_crawler_prod\packages\offline\logger.py

batch_runner.py 수정 지침:
  process_account() 내부 DM 전송 성공 직후 다음 코드 한 줄 추가:

    from logger import log_processed
    log_processed(uid, "", "", "", "성공")

  예)
    if get_dm_button(driver):
        send_dm(driver, "요약콘텐츠로 공구 제안드려요")
        print(f"✉️ DM 전송 → {uid}")
        log_processed(uid, "", "", "", "성공")

이후:
  python batch_runner.py          # 크롤링
  python report_generator.py      # 엑셀 생성