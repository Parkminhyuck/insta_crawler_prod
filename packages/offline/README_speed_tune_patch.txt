===== SELECTIVE SPEED TUNE PATCH =====
• utils_delay.py – sleep_post() / sleep_action() 두 단계 딜레이, INI에서 조정
• hashtag_crawler.py – 게시글 간 sleep_post 사용
• batch_runner.py – like / follow / DM 후 sleep_action, 계정 간 sleep_post

settings_offline.ini 추가 항목 예:
[DELAY]
post_delay = 2.0      ; 게시글 간
action_delay = 3.0    ; 좋아요·팔로우·DM 이후

설치:
  압축 해제 후 세 파일 덮어쓰기