@echo off

REM Navigate to project directory
cd /d E:\insta_crawler_prod\packages\offline

REM Run automation script
..\..\.\.venv\Scripts\python.exe batch_runner.py --limit 3

pause
