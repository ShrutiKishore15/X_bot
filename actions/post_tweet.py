import random
from config import driver
from appium.webdriver.common.appiumby import AppiumBy
from actions.navigate_to_home import navigate_to_home
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def post_tweet():
    try:
        initial_new_post_button = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.twitter.android:id/composer_write")'
        )
        initial_new_post_button.click()
        print("Clicked the initial 'New post' button.")

        second_new_post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.twitter.android:id/composer_write")'
            ))
        )
        second_new_post_button.click()
        print("Clicked the second 'New post' button.")

        tweet_texts = ["Great day", "Sunshine so good", "Feeling motivated", "Life is beautiful", "Stay positive"]
        tweet_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.twitter.android:id/tweet_text")'
            ))
        )
        tweet_text = random.choice(tweet_texts)
        tweet_input.send_keys(tweet_text)
        print(f"Typed the message: '{tweet_text}'.")

        tweet_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.twitter.android:id/button_tweet")'
            ))
        )
        tweet_button.click()
        print("Clicked the 'Tweet' button. Tweet posted successfully.")
    except Exception as e:
        print(f"Error while posting tweet: {e}")
    finally:
        navigate_to_home()
