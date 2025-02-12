from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains


class Utilities:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def click_element(self, locator_type, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
            element.click()
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error clicking element {locator}: {str(e)}")

    def enter_text(self, locator_type, locator, value):
        try:
            element = self.wait.until(EC.presence_of_element_located((locator_type, locator)))
            element.clear()
            element.send_keys(value)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error entering text in {locator}: {str(e)}")

    def get_element_text(self, locator_type, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located((locator_type, locator)))
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error getting text from {locator}: {str(e)}")
            return None

    def is_element_visible(self, locator_type, locator):
        try:
            self.wait.until(EC.visibility_of_element_located((locator_type, locator)))
            return True
        except TimeoutException:
            return False
        
    def scroll_to_element(self, locator_type, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located((locator_type, locator)))
            try:
                self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            except Exception as js_error:
                print(f"JavaScript scroll failed for {locator}. Error: {js_error}")
                try:
                    actions = ActionChains(self.browser)
                    actions.move_to_element(element).perform()
                except Exception as action_error:
                    print(f"ActionChains scroll failed for {locator}. Error: {action_error}")
        except TimeoutException:
            print(f"Timeout: Could not locate element {locator} to scroll.")
        except NoSuchElementException:
            print(f"Error: Element {locator} not found for scrolling.")

    def click_checkbox(self, locator_type, locator):
        
        checkbox = self.browser.find_element(locator_type,locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(checkbox).click().perform()

    def generate_locator(self,locator_type, locator, index):

        locator = locator.replace("{}",str(index))

        return (locator_type,locator)
    
    def find_element(self, locator_type, locator):
        """Finds a single element and handles exceptions."""
        try:
            return self.browser.find_element(*(locator_type, locator))
        except NoSuchElementException:
            print(f"Error: Element {locator} not found.")
        except StaleElementReferenceException:
            print(f"Error: Stale element reference for {locator}. Retrying...")
            return self.browser.find_element((locator_type, locator))
        except TimeoutException:
            print(f"Timeout: Could not find element {locator}.")
        return None

    def find_elements(self,locator_type, locator):
        """Finds multiple elements and handles exceptions."""
        try:
            return self.browser.find_elements(*(locator_type, locator))
        except NoSuchElementException:
            print(f"Error: Elements {locator} not found.")
        except StaleElementReferenceException:
            print(f"Error: Stale element reference for {locator}. Retrying...")
            return self.find_elements((locator_type,locator))
        except TimeoutException:
            print(f"Timeout: Could not find elements {locator}.")
        return []