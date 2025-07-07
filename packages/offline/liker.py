"""Patched liker.py — Instagram UI update (2025‑06)

Usage:
    from liker import like_recent_posts
    like_recent_posts(driver, num_posts=3)

Changes:
    * Uses flexible CSS selector "article a[href*='/p/']" for posts
    * Waits for Like button via XPath that matches both English ('Like') and Korean ('좋아요') aria‑labels
    * Clicks via JavaScript to avoid overlay interception
    * Esc key to close modal, tiny sleep between actions
"""

import time
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


def like_recent_posts(driver: WebDriver, num_posts: int = 3, delay: float = 1.0) -> None:
    """Like the most recent *num_posts* posts on the current profile page.

    Works with Instagram UI as of 2025‑07.

    Args:
        driver: Selenium WebDriver already on a user's profile page.
        num_posts: How many recent posts to like (default 3).
        delay: Seconds to sleep after each like to avoid rate‑limits.
    """
    # Select thumbnails of recent posts (feed or profile)
    post_links = driver.find_elements(By.CSS_SELECTOR, "article a[href*='/p/']")[:num_posts]

    for link in post_links:
        # Open the post
        driver.execute_script("arguments[0].click();", link)

        try:
            # Wait until the like (heart) button is clickable
            like_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//section//span/*[(local-name()='svg') and (@aria-label='Like' or @aria-label='좋아요')]",
                    )
                )
            )
            like_btn.click()
            time.sleep(delay)

        except Exception:
            # Ignore if like button not found or already liked
            pass

        finally:
            # Close the modal post viewer
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            time.sleep(0.5)
