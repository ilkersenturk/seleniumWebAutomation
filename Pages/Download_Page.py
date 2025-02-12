from selenium.webdriver.common.by import By
import time
from utilities.utilities import Utilities

class DownloadPage:
    def __init__(self, browser):
        self.browser = browser
        self.utils = Utilities(browser)
    
    def navigate(self):
        self.browser.get("https://the-internet.herokuapp.com/download")
    
    def download_file(self):
        file_link = self.browser.find_elements(By.TAG_NAME, "a")[0]
        self.browser.execute_script("arguments[0].scrollIntoView();", file_link)
        self.utils.click_element(By.XPATH, '//a[@href="download/12.png"]')
        time.sleep(3)  # Allow time for file download