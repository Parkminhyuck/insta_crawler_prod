offline_account_worker_fix_20250708.zip

## 수정 파일
- account_worker.py

## 변경 사항
1. account_grader import 제거
2. get_followers 호출 제거 (사용되지 않음)

## 적용 방법
1. 압축 해제 후 packages/offline/account_worker.py를 덮어쓰기
2. python batch_runner.py --segment "공구" --limit 3 로 실행