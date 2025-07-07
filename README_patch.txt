# InstaCrawler Patch – 자동 드라이버 적용 버전

## ✅ 주요 변경 사항
- `create_driver()` 함수가 더 이상 `chromedriver.exe` 직접 경로를 요구하지 않습니다.
- `webdriver_manager.chrome.ChromeDriverManager().install()` 자동 사용

## 📦 포함 파일
- `test_flow.py` – 자동 드라이버 연동 완료본
- `README_patch.txt`

## 📌 사용법
1. 기존 `test_flow.py` 백업
2. 이 zip 안의 파일로 교체
3. 가상환경에서 아래 명령 실행:

```
pip install webdriver-manager
python test_flow.py
```

– Generated 2025-07-06T15:06:00.141442
