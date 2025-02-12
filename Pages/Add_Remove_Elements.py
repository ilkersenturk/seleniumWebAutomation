from selenium.webdriver.common.by import By
from utilities.utilities import Utilities


class AddRemoveElementsPage:

    ADDELEMENT = (By.CSS_SELECTOR, "button[onClick='addElement()']")
    DELETE = (By.CSS_SELECTOR, "#elements button:nth-child({})")
    ALL_DELETE = (By.CSS_SELECTOR, '*[ onclick="deleteElement()"]')

    def  __init__(self, browser):
        self.browser = browser
        self.utils = Utilities(browser)

    def navigate(self):
        self.browser.get("https://the-internet.herokuapp.com/add_remove_elements/")

    def add_element(self):
        self.utils.click_element(*self.ADDELEMENT)

    def remove_element(self, index):
        locator = self.utils.generate_locator(*self.DELETE, 2)
        print(locator)
        self.utils.click_element(*locator)

    def return_element_counts(self):

        elements = self.utils.find_elements(*self.ALL_DELETE)
        print(f"There are total {len(elements)} elements")
        return len(elements)