
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def get_chrome_driver():
    BASE = os.path.dirname(os.path.abspath(__file__))
    chrome_path = os.path.abspath(os.path.join(BASE, "..", "..", "chrome-win64", "chrome.exe"))
    driver_path = os.path.abspath(os.path.join(BASE, "..", "..", "chrome-win64", "chromedriver.exe"))

    options = Options()
    options.binary_location = chrome_path
    options.add_argument("--no-sandbox")

    return webdriver.Chrome(service=Service(driver_path), options=options)
