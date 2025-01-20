import random
from config import driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from actions.utils.scroll_down import scroll_down_random
from actions.utils.scroll_up import scroll_up_small
from actions.utils.launch_app import launch_app

def like_tweet():
    try:
        print("Scrolling down by a random amount...")
        scroll_amount = scroll_down_random()

        # Re-locate the tweet element after scrolling
        print("Locating the first visible tweet after scrolling...")
        tweet_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.twitter.android:id/outer_layout_row_view_tweet").instance(0)'
            ))
        )
        print("Located the first visible tweet after scrolling.")
        # Locate the like button for the selected tweet
        like_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.twitter.android:id/inline_action_item_icon").instance(2)'
            ))
        )

        # Click the like button
        like_button.click()
        print(f"Liked tweet.")

    except Exception as e:
        print(f"Error while trying to like tweet: {e}")
        launch_app()
    finally:
        scroll_up_small()
