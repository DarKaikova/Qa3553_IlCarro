import time

from pages.login_page import LoginPage

VALID_EMAIL = 'dar.kaikova@gmail.com'
VALID_PASSWORD = 'Dar123456!'
INVALID_EMAIL = 'dar.kaikovagmail.com'
INVALID_EMAIL_2 = 'darIA.kaikova@gmail.com'
INVALID_PASSWORD = 'Dar123456!12'
UNREGISTERED_USER_EMAIL = 'darion.kaikova@gmail.com'
UNREGISTERED_USER_PASSWORD = 'sakadam_badimbadum12!'



def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL) #не проходит, так как почта не успевает встать для проверки (слишком быстро)(поставила паузы для помощи)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.login_success_text() == "You are logged in success"
    login_page.close_window()

    assert login_page.is_logged() is True



def test_login_success_1(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)

    assert login_page.login_success_text() == "You are logged in success"
    login_page.close_window()

    assert login_page.is_logged() is True


def test_with_empty_email(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email('')
    login_page.fill_password(VALID_PASSWORD)

    assert login_page.error_is_empty() == "Email is required"


def test_with_empty_password(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.error_for_password()
    login_page.fill_email(VALID_EMAIL)

    assert login_page.error_is_empty() == "Password is required"


def test_wrong_email_format(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)

    assert login_page.wrong_email_format() == 'Wrong email format'

def test_valid_email_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(INVALID_PASSWORD)
    login_page.submit_login()

    assert login_page.login_unsuccess_text() == '"Login or Password incorrect"'
    login_page.close_window()


def test_invalid_email_valid_password(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL_2)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.login_unsuccess_text() == '"Login or Password incorrect"'
    login_page.close_window()



def test_unregistered_user(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(UNREGISTERED_USER_EMAIL)
    login_page.fill_password(UNREGISTERED_USER_PASSWORD)
    login_page.submit_login()

    assert login_page.login_unsuccess_text() == '"Login or Password incorrect"'
    login_page.close_window()






