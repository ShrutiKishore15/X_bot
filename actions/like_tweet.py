import random
from config import driver
from appium.webdriver.common.appiumby import AppiumBy

def like_tweet():
    try:
        tweet_index = random.randint(0, 5)  # Randomly choose a tweet index
        like_button = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().resourceId("com.twitter.android:id/inline_action_item_icon").instance({2})'
        )
        like_button.click()
        print(f"Liked tweet at index {tweet_index}.")
    except Exception as e:
        print(f"Error while trying to like tweet: {e}")
