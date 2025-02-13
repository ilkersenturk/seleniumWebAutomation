from Pages.Broken_Images import BrokenImagesPage
import pytest

def test_broken_image_count(browser):


    broken_images = BrokenImagesPage(browser)
    broken_images.navitage()

    assert  3 == broken_images.return_image_count()

def get_all_images(browser):
    broken_images_page = BrokenImagesPage(browser)
    broken_images_page.navitage()

    all_images = broken_images_page.return_all_images()

    return all_images



def test_image_broken(browser):

    broken_images_page = BrokenImagesPage(browser)
    broken_images_page.navitage()
    all_images = broken_images_page.return_all_images()

    expected_results =[True,True, False]
    results = []
    for i, image in enumerate(all_images):

        image_src = image.get_attribute('src')
        results.append(broken_images_page.is_image_broken(image_src))
    assert expected_results == results