
# dm_followup_router.py
# 응답 유형에 따라 후속 메시지 자동 분기 처리

import csv
from message_template_loader import get_dm_message
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 후속 템플릿 정의
FOLLOWUP_TEMPLATES = {
    "긍정 응답": "🙏 감사합니다! 이번 주 인기템 공구 제안드릴게요. 링크 확인해주세요!",
    "조회만 함": "혹시 관심 있으시면 언제든지 DM 주세요 😊",
    "부정 응답": "소중한 피드백 감사합니다. 다음에 더 좋은 제안으로 찾아뵐게요 🙏",
    "응답 없음": None  # 무응답은 생략
}

# 후속 메시지 전송
def send_followup(driver, uid, response_type):
    if response_type not in FOLLOWUP_TEMPLATES:
        print(f"❌ 알 수 없는 응답 유형: {response_type}")
        return

    msg = FOLLOWUP_TEMPLATES[response_type]
    if not msg:
        print(f"❎ 무응답 계정 생략: {uid}")
        return

    try:
        driver.get(f"https://www.instagram.com/{uid}/")
        time.sleep(2)

        btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and (text()='Message' or text()='메시지')]"))
        )
        btn.click()
        print(f"📨 DM 창 진입 → {uid}")

        area = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea, div[contenteditable='true']"))
        )
        area.click()
        area.send_keys(msg + Keys.ENTER)
        print(f"✅ 후속 메시지 전송 완료 → {uid} ({response_type})")

    except Exception as e:
        print(f"❌ 후속 메시지 전송 실패: {uid}, 오류: {e}")
