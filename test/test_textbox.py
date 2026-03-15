import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.textbox_page import TextboxPage


def setup_driver():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://xqa.io/practice/text-box")
    driver.maximize_window()

    return driver


def test_fill_textbox():

    driver = setup_driver()

    page = TextboxPage(driver)

    page.enter_username("Hello")
    page.enter_email("vikash@test.com")
    page.enter_current_address("Somnath")
    page.enter_permanent_address("Ahmedabad")

    page.click_submit()

    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 200);")

    output = page.get_output()

    print(output)

    driver.quit()