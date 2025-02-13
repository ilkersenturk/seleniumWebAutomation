from utilities.utilities import Utilities
from selenium.webdriver.common.by import By
import requests

class BrokenImagesPage:

    ALL_IMAGES = (By.XPATH, "(//div[@class='example']/img)")
    SINGLE_IMAGE=(By.XPATH, "(//div[@class='example']/img)[{}]")
    URL ="https://the-internet.herokuapp.com/broken_images"
    def __init__(self,browser):
        self.browser = browser
        self.utils = Utilities(self.browser)

    def navitage(self):
        self.browser.get(self.URL)

    def return_image_count(self):
        
        return len(self.return_all_images())
    
    def return_all_images(self):
        return self.utils.find_elements(*self.ALL_IMAGES)
    
    
    def is_image_broken(self,url):
        """Send an HTTP request to check if the image is accessible."""
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            return response.status_code != 200  # If not 200, image is broken
        except requests.RequestException:
            return True  