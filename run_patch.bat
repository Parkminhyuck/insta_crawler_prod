@echo off
rem === Insta Crawler Patch • apply & run ===
setlocal
cd /d %~dp0
echo Applying patch files...
copy /Y account_grader.py ..\account_grader.py >nul
copy /Y test_flow_utils.py ..\test_flow_utils.py >nul
echo Patch applied.

echo Activating venv...
call ..\.venv\Scripts\activate

echo Running batch_runner.py ...
python ..\batch_runner.py
pause
