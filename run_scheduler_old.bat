@echo off
setlocal

REM ── 1) 이 배치파일 위치(=E:\insta_crawler_prod)로 이동 ──
pushd "%~dp0"

REM ── 2) python.exe 검색 우선순위 설정 ──
REM    1) insta_crawler_prod\python.exe
REM    2) USB 루트(E:\python.exe)
REM    3) 시스템 PATH 의 python
set "BASE=%~dp0"
set "USBROOT=%~dp0\.."

if exist "%BASE%python.exe" (
    set "PY=%BASE%python.exe"
) else if exist "%USBROOT%\python.exe" (
    set "PY=%USBROOT%\python.exe"
) else (
    set "PY=python"
)

echo [INFO] Using Python: %PY%

REM ── 3) pip / 의존성 보장 ──
"%PY%" -m ensurepip --default-pip
"%PY%" -m pip install --upgrade pip selenium pyyaml pandas xlsxwriter

REM ── 4) 스케줄러 실행 ──
"%PY%" -m packages.offline.scheduler

REM ── 5) 종료 ──
popd
endlocal
pause
