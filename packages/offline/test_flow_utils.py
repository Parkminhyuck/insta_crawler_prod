import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_profile_header(driver, timeout=10):
    """
    프로필 헤더 로딩을 기다립니다. 실패 시 TimeoutError 발생.
    페이지가 삭제/비공개 된 경우도 감지하여 TimeoutError을 던집니다.
    """
    end_time = time.time() + timeout
    while True:
        # 페이지가 삭제되었거나 사용할 수 없는 경우
        if "죄송합니다. 페이지를 사용할 수 없습니다" in driver.page_source:
            raise TimeoutError("⚠️ 프로필 페이지 접근 불가 — 페이지가 삭제되었거나 비공개입니다.")

        try:
            # 헤더 또는 section 태그가 로드될 때까지 대기
            return WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.TAG_NAME, "header"))
            )
        except:
            if time.time() > end_time:
                # 스크린샷 저장
                screenshot_path = f"logs/header_timeout_{int(time.time())}.png"
                driver.save_screenshot(screenshot_path)
                raise TimeoutError(f"프로필 헤더 로딩 타임아웃. 스크린샷: {screenshot_path}")
            time.sleep(0.5)
