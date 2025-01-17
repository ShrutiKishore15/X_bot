import time
from config import driver

def navigate_to_home():
    """
    Navigates back to the start activity screen (Twitter feed).
    """
    try:
        driver.activate_app("com.twitter.android")  # Relaunches the app, bringing it back to the start activity
        print("Navigated back to the home screen.")
        time.sleep(10)
    except Exception as e:
        print(f"Error while navigating back to the home screen: {e}")
