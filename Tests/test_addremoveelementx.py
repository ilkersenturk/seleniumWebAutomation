import pytest
import time
from Pages.Add_Remove_Elements import AddRemoveElementsPage


def test_add_remove(browser):
    """Test login functionality."""
    addremoveelementspage = AddRemoveElementsPage(browser)
    addremoveelementspage.navigate()

    for i in range(0,4):
        addremoveelementspage.add_element()
        time.sleep(1)

    addremoveelementspage.remove_element(2)
    time.sleep(2)
    addremoveelementspage.remove_element(2)
    time.sleep(2)
    addremoveelementspage.add_element()
    element_counts = addremoveelementspage.return_element_counts()
    assert 3 == element_counts
