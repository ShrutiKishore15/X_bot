import random
import time
from config import driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from actions.utils.launch_app import launch_app



def send_direct_message(inst):
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
                f'new UiSelector().className("android.widget.RelativeLayout").instance({inst})'
            ))
        )
        second_profile.click()
        print("Clicked on the second profile in the DM list.")

        # Check for the "Get verified" prompt
        can_not_message = None
        try:
            can_not_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.ScrollView")'
                ))
            )
        except TimeoutException:
            print("No 'Get Verified' prompt found. Proceeding with DM.")

        if can_not_message:
            no_thanks_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.Button").instance(1)'
                ))
            )
            no_thanks_button.click()
            print("Cannot send message to this user. Pressed 'No, Thanks'.")
            
            # Navigate back to the home screen
            back_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().description("Navigate up")'
                ))
            )
            back_button.click()
            time.sleep(1)
            back_button.click()
            print("Back button clicked...")
            
            home_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().resourceId("com.twitter.android:id/channels")'
                ))
            )
            home_button.click()
            print("Back to home page...")
            return inst + 1

        # Proceed with sending the message
        message_input_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("Start a message")'
            ))
        )
        message_input_box.click()
        print("Clicked on the message input box.")

        dm_messages = ["Hello!", "Hey there!", "Hi!", "What's up?", "Greetings!"]
        dm_message = random.choice(dm_messages)
        message_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText")'
            ))
        )
        message_input.send_keys(dm_message)
        print(f"Entered message: '{dm_message}'.")

        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR, 
                'new UiSelector().description("Send")'
            ))
        )
        send_button.click()
        print("DM sent successfully.")
        time.sleep(2)
        # Navigate back to home
        back_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().description("Navigate up")'
            ))
        )
        back_button.click()
        print("Back button clicked...")
        
        home_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.twitter.android:id/channels")'
            ))
        )
        home_button.click()
        print("Back to home page...")
        return inst

    except Exception as e:
        print(f"Error while sending DM: {e}")
        launch_app()