from selenium.webdriver.common.by import By

class LoginPageBurger:

    email_field = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input"]

    password_field = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input"]

    sign_in_button = [By.XPATH, "/html/body/div/div/main/div/form/button"]

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()