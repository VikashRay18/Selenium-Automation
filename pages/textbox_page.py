from selenium.webdriver.common.by import By

class TextboxPage:

    username = (By.ID, "userName")
    email = (By.ID, "userEmail")
    current_address = (By.ID, "currentAddress")
    permanent_address = (By.ID, "permanentAddress")
    submit_button = (By.ID, "submit")
    output = (By.ID, "output")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, name):
        self.driver.find_element(*self.username).send_keys(name)

    def enter_email(self, mail):
        self.driver.find_element(*self.email).send_keys(mail)

    def enter_current_address(self, address):
        self.driver.find_element(*self.current_address).send_keys(address)

    def enter_permanent_address(self, address):
        self.driver.find_element(*self.permanent_address).send_keys(address)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_output(self):
        return self.driver.find_element(*self.output).text