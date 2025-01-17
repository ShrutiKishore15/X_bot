import random
from config import driver
from appium.webdriver.common.appiumby import AppiumBy
from actions.navigate_to_home import navigate_to_home

def comment_on_tweet():
    try:
        tweet_index = random.randint(0, 5)  # Randomly choose a tweet index
        reply_button = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().resourceId("com.twitter.android:id/inline_action_item_icon").instance({0})'
        )
        reply_button.click()
        print(f"Clicked reply button for tweet at index {tweet_index}.")

        comments = ["That's news", "Informative", "Enlightening", "Interesting", "Thought-provoking"]
        comment_input = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.twitter.android:id/tweet_text")'
        )
        comment = random.choice(comments)
        comment_input.send_keys(comment)
        print(f"Entered comment: '{comment}'.")

        reply_button = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.twitter.android:id/button_tweet")'
        )
        reply_button.click()
        print("Posted the comment.")
    except Exception as e:
        print(f"Error while commenting on tweet: {e}")
    finally:
        navigate_to_home()
