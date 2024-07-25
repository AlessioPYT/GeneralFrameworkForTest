from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="logs_info.log")

class Driver:
    driver = None

    @classmethod
    def start(cls):
        options = Options()
        logging.info("launching the driver browser")
        options.add_argument("dom.webnotifications.enabled")
        prefs = {"profile.default_content_setting_values.notifications": 2}  # Отключить уведомления
        options.add_experimental_option("prefs", prefs)
        options.add_argument("user-data-dir=C:\\Users\\Алексей\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1") # свой профиль
        cls.driver = webdriver.Chrome(options=options)
        logging.info("launching the driver browser was successful")
        return cls.driver

        
    @classmethod
    def open_browser(cls):
        logging.info("Opening the browser")
        cls.driver.get("somesite.com")
        return cls.driver


    @classmethod
    def stop(cls):
        if cls.driver:
            logging.info("Browser was closed successful")
            cls.driver.quit()