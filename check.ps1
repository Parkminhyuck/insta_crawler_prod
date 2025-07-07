Write-Host "== Python version =="; python --version
Write-Host "`n== pip packages =="; python -m pip show selenium instaloader fpdf
Write-Host "`n== Selenium quick test ==";
python -c "from selenium import webdriver as w; from selenium.webdriver.chrome.service import Service; drv=w.Chrome(service=Service('chromedriver-win64/chromedriver.exe')); print('Chrome OK'); drv.quit()"
Write-Host "`n== Instaloader version =="; python -c "import instaloader, sys; print('instaloader', instaloader.__version__)"
