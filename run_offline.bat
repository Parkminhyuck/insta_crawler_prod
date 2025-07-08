@echo off
REM Activate virtualenv (modify path if needed)
if exist .venv\Scripts\activate (
    call .\.venv\Scripts\activate
) else (
    python -m venv .venv
    call .\.venv\Scripts\activate
    pip install -r requirements.txt
)
REM Navigate to offline package folder
cd packages\offline
python batch_runner.py --segment "공구" --once
pause
