# Instagram 해시태그 기반 자동 파이프라인 (2025-07-07)

## 신규/수정 파일
| 파일 | 설명 |
|------|-------|
| `hashtag_crawler.py` | 해시태그 검색 → 게시글 작성자 UID 수집 |
| `batch_runner.py` | 로그인 → 해시태그 수집 → 등급화 → 좋아요 + DM 전체 파이프라인 |
| `test_flow.py` | 개인 계정 단일 테스트용 (변경 없음) |

## 실행 방법
```powershell
cd E:\insta_crawler_prod
.\.venv\Scripts\Activate.ps1
pip install webdriver-manager
python batch_runner.py
```

*브라우저 버전과 무관하게 ChromeDriver가 자동 관리됩니다.*
