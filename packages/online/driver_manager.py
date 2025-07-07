
"""driver_manager.py

유연한 ChromeDriver 로딩 유틸.
1) settings.ini → [DRIVER] local_driver_path 값 존재 시 해당 경로 사용
2) 환경변수 CHROMEDRIVER_PATH 존재 시 사용
3) 인터넷 가능 시 webdriver_manager 로 최신 드라이버 자동 다운로드
4) 위 모두 실패 시 RuntimeError 발생
"""

import os, ssl, pathlib, socket
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

try:
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    ChromeDriverManager = None  # 오프라인 환경 대비

import configparser

def _internet_accessible(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except OSError:
        return False

def _load_config(path="settings.ini"):
    cfg = configparser.ConfigParser()
    cfg.read(path, encoding="utf-8")
    return cfg

def get_chrome_driver(headless: bool = True):
    # 1) settings.ini 확인
    cfg = _load_config()
    local_path = None
    if cfg.has_section("DRIVER"):
        local_path = cfg.get("DRIVER", "local_driver_path", fallback=None)
    # 2) 환경변수
    env_path = os.getenv("CHROMEDRIVER_PATH")
    driver_path = local_path or env_path

    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-software-rasterizer")

    if driver_path and pathlib.Path(driver_path).exists():
        service = Service(driver_path)
        return webdriver.Chrome(service=service, options=options)

    # 3) 온라인 다운로드
    if _internet_accessible() and ChromeDriverManager is not None:
        ssl._create_default_https_context = ssl._create_unverified_context  # SSL 우회
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    raise RuntimeError("❌ ChromeDriver 경로를 찾을 수 없으며 인터넷에도 연결할 수 없습니다.")
