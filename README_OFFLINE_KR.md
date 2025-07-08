# Insta Crawler Offline 버전 (KR)

## 1. 설치
```bash
python -m venv .venv
.\.venv\Scriptsctivate
pip install -r requirements.txt
```

## 2. 실행
```bash
@Windows
run_offline.bat

# 또는 수동
cd packages/offline
python batch_runner.py --segment "공구" --once
```

## 3. 주요 파일
| 파일 | 설명 |
|------|------|
| `insta_pipeline_offline.py` | 오프라인 파이프라인 진입점 |
| `batch_runner.py` | 해시태그 세그먼트 단일 실행 |
| `driver_manager.py` | Selenium WebDriver 초기화 및 옵션 설정 |
| `auth.py` | 로그인/쿠키 로직 (우회 모드) |

### 설정
- `settings_offline.ini` 에서 계정과 옵션 수정
- `settings.json` 추가 세부 파라미터

## 4. 로그
실행 로그는 `logs/` 폴더에 날짜별 생성됩니다.
