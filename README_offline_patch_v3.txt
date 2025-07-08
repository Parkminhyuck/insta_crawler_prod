=============================================
OFFLINE PATCH v3 – (dm_sender import 경로 문제 수정)
=============================================
덮어쓰기 위치:
    E:\insta_crawler_prod\packages\offline\batch_runner.py

주요 변경:
  • sys.path 에 루트(insta_crawler_prod)와 packages 폴더를 추가
  • driver_manager/auth/dm_sender 등 모듈을 offline 또는 루트에서 안전하게 import

실행:
    cd E:\insta_crawler_prod\packages\offline
    python batch_runner.py