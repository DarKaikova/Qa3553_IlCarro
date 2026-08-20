import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def pause(seconds):
    time.sleep(seconds)

class LoginPage:


    LOGIN_NAV = (By.CSS_SELECTOR, "[href='/login']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    YALLA_BTN = (By.XPATH, "//button[contains(text(),'Y’alla!')]")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, "h3")
    OK_BTN = (By.XPATH, "//*[text()='OK']")
    LOG_OUT_BTN = (By.XPATH, "//*[text()='Log out']")
    ERROR_EMPTY = (By.XPATH, "//*[contains(text(), 'is required')]")
    WRONG_EMAIL = (By.XPATH, "//*[text()='Wrong email format']")
    UNSUCCESS_LOGIN_TEXT = (By.CSS_SELECTOR, "p")

    def __init__(self, driver):
        self.driver = driver

    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV).click()
        pause(2)


    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.YALLA_BTN).click()

    def login(self, email, password): #это просто краткая версия подтверждения логина
        self.fill_email(email)
        self.fill_password(password)
        self.submit_login()

    def login_success_text(self):
        # return self.driver.find_element(*self.CONFIRMATION_TEXT).text
        element = WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.visibility_of_element_located(self.CONFIRMATION_TEXT)
        )
        return element.text



    def close_window(self):
        self.driver.find_element(*self.OK_BTN).click()

    def is_logged(self):
        try:
            WebDriverWait(self.driver, timeout=5).until(
                expected_conditions.visibility_of_element_located(self.LOG_OUT_BTN)
                # можно еще написать как EC.visibility_of_element_located
                # только в случае, когда сверху мы поменяла expected conditions на ec
            )
            return True
        except TimeoutException :
            return False



    def error_is_empty(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.visibility_of_element_located(self.ERROR_EMPTY)
        )
        return element.text


    def wrong_email_format(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.visibility_of_element_located(self.WRONG_EMAIL)
        )
        return element.text

    def login_unsuccess_text(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.visibility_of_element_located(self.UNSUCCESS_LOGIN_TEXT)
        )
        return element.text

    def error_for_password(self):
        self.driver.find_element(*self.PASSWORD_INPUT).click()

