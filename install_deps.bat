@echo off
call .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install selenium webdriver_manager fpdf instaloader
pause
