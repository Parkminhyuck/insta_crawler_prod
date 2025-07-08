===== SPEED CONTROL PATCH =====
• utils_delay.py  – sleep(base, jitter) 함수, multiplier 읽어 전체 속도 제어
• hashtag_crawler.py v14 – 모든 time.sleep → sleep() 적용
• settings_append.txt – [DELAY] 섹션 예시 (multiplier = 1.5)

설치:
  1) 압축 해제하여 utils_delay.py, hashtag_crawler.py 를
     E:\insta_crawler_prod\packages\offline\ 에 덮어쓰기
  2) settings_offline.ini 가장 아래에 [DELAY] 블록 추가:

     [DELAY]
     multiplier = 1.5

     multiplier 값을 1.0~3.0 범위로 조절해 속도를 느리게/빠르게 변경

사용:
  cd E:\insta_crawler_prod\packages\offline
  python batch_runner.py