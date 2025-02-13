from selenium.webdriver.common.by import By
from utilities.utilities import Utilities
import time

class FileUploadPage:
    
    URL = "https://the-internet.herokuapp.com/upload"
    FILE_INPUT = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOADED_MESSAGE = (By.ID, "uploaded-files")

    def __init__(self, browser):
        self.browser = browser
        self.utils = Utilities(self.browser)
        print("File upload page is created")
   
    def navigate(self):
        self.browser.get(self.URL)

    def upload_file(self, file_path):
        """Upload a file."""
        self.utils.enter_text(*self.FILE_INPUT, file_path)
        self.utils.click_element(*self.UPLOAD_BUTTON)
        
    def get_uploaded_message(self):
        """Get uploaded file name confirmation."""

        return self.utils.get_element_text(*self.UPLOADED_MESSAGE)
       