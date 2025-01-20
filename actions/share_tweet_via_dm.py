import random
import time
from config import driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from actions.utils.scroll_down import scroll_down_random
from actions.utils.scroll_up import scroll_up_small
from actions.utils.launch_app import launch_app


def share_tweet_via_dm():
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

        share_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("com.twitter.android:id/inline_action_item_icon").instance(5)'
            ))
        )
        share_button.click()
        print(f"Clicked share button for tweet.")

        dm_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.twitter.android:id/action_sheet_item_title")'
            ))
        )
        dm_option.click()
        print("Selected 'Send via Direct Message'.")

        first_profile = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.RelativeLayout").instance(0)'
            ))
        )
        first_profile.click()
        print("Selected the first profile in the recipient list.")

        messages = ["Check this out!", "Look at this!", "Thought you might like this.", "FYI", "Interesting read"]
        message_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.twitter.android:id/message_text")'
            ))
        )
        message = random.choice(messages)
        message_input.send_keys(message)
        print(f"Entered message: '{message}'.")

        send_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.Button")'
            ))
        )
        send_button.click()
        print("Tweet shared via DM.")
    except TimeoutException:
        print("Error: One or more elements could not be located within the timeout.")
        launch_app()
    except Exception as e:
        print(f"Error while sharing tweet via DM: {e}")
        launch_app()
    finally:
        scroll_up_small()
        time.sleep(2)
