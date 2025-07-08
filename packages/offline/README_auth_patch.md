
offline_patch_auth_20250708.zip

## 수정 파일
- auth.py

## 변경 내역
1. 로그인 완료 대기 요소를 span[@aria-label='Home']에서 nav 요소로 변경
2. TimeoutException 시 경고만 출력하고 진행
3. '나중에 하기', 'Not Now' 팝업 자동 클릭 로직 추가

## 적용 방법
1. 압축 해제 후 packages/offline/auth.py 덮어쓰기
2. python batch_runner.py --segment "공구" --once 으로 재실행
