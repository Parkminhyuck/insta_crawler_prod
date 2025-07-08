===== GRAPHQL UID PATCH =====
• hashtag_crawler.py v15
    - Network Performance 로그에서 /api/graphql 응답 JSON 파싱
      → owner.username 추출 (100 %)
    - 기존 meta fallback 유지
    - utils_delay.sleep_post() 사용

사용법:
  1) 압축 해제하여 hashtag_crawler.py 덮어쓰기
  2) ChromeDriver가 퍼포먼스 로그 수집하도록 설정되어 있지 않다면
     driver 생성 시:
       caps = DesiredCapabilities.CHROME
       caps['goog:loggingPrefs'] = {'performance': 'ALL'}
     로 설정 (driver_manager.py 수정 필요)
  3) 실행
     python batch_runner.py