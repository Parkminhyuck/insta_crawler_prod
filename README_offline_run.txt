=============================================
OFFLINE PIPELINE QUICK START (USB / 로컬 PC)
=============================================

1) 가상환경(이미 생성됐다면 스킵)
   > python -m venv .venv
   > .\.venv\Scripts\activate

2) 의존성 설치
   > pip install -r requirements.txt

3) 오프라인 파이프라인 실행
   > cd packages\offline
   > python batch_runner.py

   ▷ headless 모드로 돌리고 싶으면:
   > python batch_runner.py  # 코드 내부에서 headless=True 수정 or main(headless=True)

---------------------------------------------
파일 배치
---------------------------------------------
* batch_runner.py  →  E:\insta_crawler_prod\packages\offline\batch_runner.py
* README_offline_run.txt  →  같은 폴더(참고용)

프로덕션(online) 파일은 이번 패치에 포함되지 않습니다.