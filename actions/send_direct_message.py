import random
from config import driver
from appium.webdriver.common.appiumby import AppiumBy
from actions.navigate_to_home import navigate_to_home
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def send_direct_message():
    try:
        dm_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.twitter.android:id/dms")'
            ))
        )
        dm_tab.click()
        print("Clicked on the DM tab.")

        new_message = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.twitter.android:id/composer_write")'
            ))
        )
        new_message.click()
        print("Clicked on the new message button.")

        second_profile = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.RelativeLayout").instance(5)'
            ))
        )
        second_profile.click()
        print("Clicked on the second profile in the DM list.")

        dm_messages = ["Hello!", "Hey there!", "Hi!", "What's up?", "Greetings!"]
        message_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(4)'
            ))
        )
        dm_message = random.choice(dm_messages)
        message_input.send_keys(dm_message)
        print(f"Entered message: '{dm_message}'.")

        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                'new UiSelector().className("android.widget.Button").instance(3)'
            ))
        )
        send_button.click()
        print("DM sent successfully.")
    except Exception as e:
        print(f"Error while sending DM: {e}")
    finally:
        navigate_to_home()
