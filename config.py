from appium import webdriver
from appium.options.common import AppiumOptions
from typing import Any, Dict

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'RZ8R32G2E6F',
    'appPackage': 'com.twitter.android',
    'appActivity': '.StartActivity',
    'language': 'en',
    'locale': 'us',
    'noReset': True,
    'fullReset': False,
}

url = 'http://localhost:4723'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
