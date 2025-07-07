## offline_patch_v2  –  2025‑07‑07

**설치 방법**

1. ZIP 압축을 `E:\insta_crawler_prod\packages\offline` 폴더에 다운
2. 기존 파일 덮어쓰기 (hashtag_crawler.py, driver_manager.py)
3. 실행:

```powershell
cd E:\insta_crawler_prod\packages\offline
python batch_runner.py --limit 3
```

driver_manager.py가 webdriver-manager를 사용하므로
`pip install webdriver-manager` 가 되어 있어야 합니다.