import random
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import driver

def scroll_down_random():
    """
    Scrolls down the screen by a random amount using the tweet list view.
    Returns the scroll amount used for later use.
    """
    try:
        print("Locating tweet list element...")
        tweet_list = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("android:id/list")'
        )

        # Random percentage for scrolling (e.g., between 20% to 60% of the list height)
        scroll_amount = random.uniform(0.5, 0.8)
        print(f"Scrolling down by {scroll_amount * 100:.2f}% of the tweet list height.")

        driver.execute_script("mobile: scrollGesture", {
            "elementId": tweet_list.id,
            "direction": "down",
            "percent": scroll_amount
        })
        return scroll_amount
    except Exception as e:
        print(f"Error while scrolling down: {e}")
        return None