"""Utility functions for `test_flow.py` (patched header wait).

Import `wait_for_profile_header` and use instead of the previous
`WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME,'header')))`.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_profile_header(driver, timeout: int = 30) -> None:
    """Wait until profile header is visible (compatible with 2025‑06 UI)."""
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "header, header section")
        )
    )
