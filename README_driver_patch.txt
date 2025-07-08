===== DRIVER PERFORMANCE PATCH =====
• driver_manager.py – Chrome 드라이버 생성 시 Performance 로그 수집 활성화
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}

설치:
  1) 압축 해제하여 driver_manager.py 덮어쓰기
     E:\insta_crawler_prod\packages\offline\driver_manager.py
  2) 이미 graphql UID 패치( hasthag_crawler.py v15 )가 적용된 상태에서 실행
     python batch_runner.py