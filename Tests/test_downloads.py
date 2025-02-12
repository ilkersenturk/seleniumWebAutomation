import pytest
from Pages.Download_Page import DownloadPage

def test_file_download(browser):
    """Test file download functionality."""
    download_page = DownloadPage(browser)
    download_page.navigate()
    download_page.download_file()
    print("File download test completed successfully!")

    