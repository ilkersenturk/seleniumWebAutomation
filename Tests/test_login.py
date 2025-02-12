import pytest
from Pages.Login_Page import LoginPage

def test_login(browser):
    """Test login functionality."""
    login_page = LoginPage(browser)
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_flash_message()