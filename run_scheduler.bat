@echo off
REM ─────────────────────────────────────────────────────
REM  1) 프로젝트 폴더로 이동 & 가상환경 활성화
pushd E:\insta_crawler_prod
call .\venv\Scripts\activate.bat

REM  2) 스케줄러 실행
echo [INFO] Scheduler starting...
py -3 -m packages.offline.scheduler

REM  3) 이전 폴더 복귀
popd
