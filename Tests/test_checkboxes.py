import pytest
from Pages.Checkbox_Page import CheckboxesPage


def test_checkboxes(browser):
    """Test checkbox selection."""
    checkboxes_page = CheckboxesPage(browser)
    checkboxes_page.navigate()
    assert checkboxes_page.select_checkbox(1), "Checkbox was not selected!"

def test_uncheckboxes(browser):
    """Test checkbox selection."""
    checkboxes_page = CheckboxesPage(browser)
    checkboxes_page.navigate()
    assert checkboxes_page.unselect_checkbox(2), "Checkbox was not selected!"


    