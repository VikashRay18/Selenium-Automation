from selenium.webdriver.common.by import By

class CheckboxPage:

    expand_all = (By.XPATH, "//button[text()='Expand all']")
    collapse_all = (By.XPATH, "//button[text()='Collapse all']")
    desktop = (By.XPATH, "//span[text()='Desktop']")
    home = (By.XPATH, "//span[text()='Home']")
    notes = (By.XPATH, "//span[text()='Notes']")
    result = (By.ID, "result")

    def __init__(self, driver):
        self.driver = driver

    def click_expand_all(self):
        self.driver.find_element(*self.expand_all).click()

    def click_collapse_all(self):
        self.driver.find_element(*self.collapse_all).click()

    def select_notes(self):
        self.driver.find_element(*self.notes).click()

    def get_output(self):
        return self.driver.find_element(*self.result).text