offline_batch_runner_patch_20250708.zip

## 수정 파일
- batch_runner.py

## 변경 사항
1. login() 호출 시 driver, username, password 인자 전달
2. settings_offline.ini에서 USERNAME, PASSWORD 읽기
3. get_chrome_driver()로 드라이버 생성

## 적용 방법
1. 압축 해제 후 packages/offline/batch_runner.py 덮어쓰기
2. python batch_runner.py --segment "공구" --limit 3 로 실행