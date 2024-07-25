from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s', filename="test_log.log")

class BasikPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    def click_button(self, xpath):
        pass


    def insert_info(self, xpath, text):
        pass


    def find_element(self, xpath):
        pass


    
    