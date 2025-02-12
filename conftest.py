import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os

@pytest.fixture(scope="session")
def browser():
    """Setup WebDriver with custom preferences for file downloads."""
    download_dir = os.path.abspath("/home/ilker/Desktop/selenium_python/downloads")
    os.makedirs(download_dir, exist_ok=True)

    options = Options()
    options.headless = False  # Set to False to see the browser in action
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", download_dir)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
    
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()