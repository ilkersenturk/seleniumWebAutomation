from selenium.webdriver.common.by import By
from utilities.utilities import Utilities


class CheckboxesPage:

    GENERIC_CHECKBOX = (By.XPATH, "//form[@id='checkboxes']/input[{}]")

    def __init__(self, browser):
        self.browser = browser
        self.utils = Utilities(browser)
    
    def navigate(self):
        self.browser.get("https://the-internet.herokuapp.com/checkboxes")
    

    def select_checkbox(self, index):

        checkbox_locator = self.utils.generate_locator(*self.GENERIC_CHECKBOX, index)
        checkbox = self.browser.find_element(*checkbox_locator)
        if not checkbox.is_selected():
            self.utils.click_checkbox(*checkbox_locator)
        return checkbox.is_selected()
    
    def unselect_checkbox(self, index):

        checkbox_locator = self.utils.generate_locator(*self.GENERIC_CHECKBOX, index)
        checkbox = self.browser.find_element(*checkbox_locator)
        if checkbox.is_selected():
            self.utils.click_checkbox(*checkbox_locator)
        return not checkbox.is_selected()
    
    
   