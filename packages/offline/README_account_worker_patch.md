
offline_account_worker_patch_20250708.zip

## 수정 파일
- account_worker.py

## 내용
1. 프로필 방문 후 팔로우 버튼이 'Follow' 또는 '팔로우'일 때만 클릭
2. 팔로우 상태 확인 후 첫 게시물 좋아요
3. DM 버튼 클릭 → DM 전송
4. 예외 처리 강화 및 단계별 로그 출력

## 적용 방법
1. 압축 해제 후 `packages/offline/account_worker.py` 덮어쓰기
2. `python batch_runner.py --segment "공구" --limit 3` 재실행
