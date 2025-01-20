import time
from config import driver

def launch_app():
    print("Launching the app...")
    try:
        driver.execute_script("mobile: startActivity", {
            "wait": True,
            "stop": True,
            "action": "android.intent.action.MAIN",
            "component": "com.twitter.android/.StartActivity",
            "categories": ["android.intent.category.LAUNCHER"],
            "flags": "0x10200000"
        })
        print("App launched successfully.")
        time.sleep(5)
    except Exception as e:
        print(f"An error occurred while launching the app: {e}")
