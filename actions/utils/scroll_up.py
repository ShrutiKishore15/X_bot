from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import driver
import time

def scroll_up_small():
    """
    Scrolls up by a small amount to make the bottom navigation bar visible.
    """
    try:
        print("Locating tweet list element...")
        tweet_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("android:id/list")'
            ))
        )

        # Define a small scroll percentage (e.g., 5%)
        small_scroll_percent = 0.2
        print(f"Scrolling up by {small_scroll_percent * 100:.2f}% of the tweet list height.")

        # Perform the scroll gesture
        driver.execute_script("mobile: scrollGesture", {
            "elementId": tweet_list.id,  # Scrolling within the tweet list
            "direction": "up",
            "percent": small_scroll_percent,
            "speed": 400  # Adjust speed if necessary for a smoother gesture
        })
        print("Small scroll up gesture completed.")
        time.sleep(2)
    except Exception as e:
        print(f"Error while scrolling up: {e}")
