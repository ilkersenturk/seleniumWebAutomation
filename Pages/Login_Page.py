from selenium.webdriver.common.by import By
from utilities.utilities import Utilities


class LoginPage:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "radius")
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, browser):
        self.browser = browser
        self.utils = Utilities(browser)

    def navigate(self):
        self.browser.get("https://the-internet.herokuapp.com/login")
    
    def login(self, username, password):
        self.utils.enter_text(*self.USERNAME, username)
        self.utils.enter_text(*self.PASSWORD, password)
        self.utils.click_element(*self.LOGIN_BUTTON)
    
    def get_flash_message(self):
        return self.utils.get_element_text(*self.FLASH_MESSAGE)
    
