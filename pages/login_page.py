import time

from selenium.webdriver.common.by import By

def pause(seconds):
    time.sleep(seconds)

class LoginPage:


    LOGIN_NAV = (By.CSS_SELECTOR, "[href='/login']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='password']")
    YALLA_BTN = (By.XPATH, "//button[contains(text(),'Y’alla!')]")

    def __init__(self, driver):
        self.driver = driver

    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV).click()
        pause(1)


    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        pause(1)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        pause(1)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        pause(1)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        pause(1)

    def submit_login(self):
        self.driver.find_element(*self.YALLA_BTN).click()