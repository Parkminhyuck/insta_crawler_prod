===== DRIVER FIX (set_capability) =====
• driver_manager.py – Selenium 4 호환: desired_capabilities 제거,
  options.set_capability('goog:loggingPrefs', {'performance':'ALL'}) 사용

설치:
  압축 해제 후 driver_manager.py 덮어쓰기
  E:\insta_crawler_prod\packages\offline\driver_manager.py