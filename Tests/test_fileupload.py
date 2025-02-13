import pytest
import os
from Pages.FileUploadPage import FileUploadPage

def test_file_upload(browser):
    """Test file upload functionality."""
    file_upload_page = FileUploadPage(browser)
    file_upload_page.navigate()

    # Define the file path (ensure this file exists in your project)
    file_path = os.path.abspath("/home/ilker/Desktop/selenium_python/resources/sample_file.txt")

    file_upload_page.upload_file(file_path)

    # Verify file upload success
    uploaded_text = file_upload_page.get_uploaded_message()
    assert "sample_file.txt" in uploaded_text, "File upload failed!"