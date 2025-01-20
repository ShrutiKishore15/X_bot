import time
import random
from config import driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from actions.utils.scroll_down import scroll_down_random
from actions.utils.scroll_up import scroll_up_small
from actions.utils.launch_app import launch_app


def comment_on_tweet():
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

        # Interact with the tweet (e.g., click the reply button)
        reply_button = tweet_element.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.twitter.android:id/inline_action_item_icon")'
        )
        reply_button.click()
        print("Clicked the reply button for the tweet.")

        # Post a comment
        comments = ["That's news", "Informative", "Enlightening", "Interesting", "Thought-provoking"]
        comment_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.twitter.android:id/tweet_text")'
            ))
        )
        comment = random.choice(comments)
        comment_input.send_keys(comment)
        print(f"Entered comment: '{comment}'.")

        # Click the reply button to post the comment
        post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.twitter.android:id/button_tweet")'
            ))
        )
        post_button.click()
        print("Posted the comment.")

        # Scroll back up
        #scroll_up(scroll_amount)

    except TimeoutException:
        print("Timeout while locating an element. Check if the UI structure has changed.")
        launch_app()
    except Exception as e:
        print(f"Error while commenting on tweet: {e}")
        launch_app()
    finally:
        scroll_up_small()
