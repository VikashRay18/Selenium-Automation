import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.checkbox_page import CheckboxPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.checkbox_page import CheckboxPage


def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://xqa.io/practice/check-box")
    driver.maximize_window()
    return driver


def test_expand_all():

    driver = setup_driver()
    page = CheckboxPage(driver)

    page.click_expand_all()
    time.sleep(2)

    print("Expand test executed")

    driver.quit()


def test_collapse_all():

    driver = setup_driver()
    page = CheckboxPage(driver)

    page.click_expand_all()
    time.sleep(2)

    page.click_collapse_all()
    time.sleep(2)

    print("Collapse test executed")

    driver.quit()


def test_select_child_checkbox():

    driver = setup_driver()
    page = CheckboxPage(driver)

    page.click_expand_all()
    time.sleep(2)

    page.select_notes()

    output = page.get_output()

    assert "notes" in output.lower()

    print("Child checkbox test passed")

    driver.quit()