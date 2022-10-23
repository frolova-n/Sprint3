from locators import Authorization
import time
from methods import LoginPageBurger

def test_login_account(driver):

    driver.find_element(*Authorization.login_button).click()

    login_page = LoginPageBurger(driver)

    login_page.login("nataliafrolova3678@ya.ru", "000018")

    time.sleep(3)

    assert driver.find_element(*Authorization.make_an_order_button).text == 'Оформить заказ'

    driver.quit()

def test_login_personal_cab(driver):

    driver.find_element(*Authorization.personal_cab_button).click()

    login_page = LoginPageBurger(driver)

    login_page.login("nataliafrolova3678@ya.ru", "000018")

    time.sleep(3)

    assert driver.find_element(*Authorization.make_an_order_button).text == 'Оформить заказ'

    driver.quit()

def test_login_reg_form(driver):


    driver.find_element(*Authorization.personal_cab_button).click()

    driver.find_element(*Authorization.registration_form_button).click()

    driver.find_element(*Authorization.login_registration_form_button).click()

    login_page = LoginPageBurger(driver)

    login_page.login("nataliafrolova3678@ya.ru", "000018")

    time.sleep(3)

    assert driver.find_element(*Authorization.make_an_order_button).text == 'Оформить заказ'

    driver.quit()

def test_login_password_recovery_button(driver):

    driver.find_element(*Authorization.login_button).click()

    driver.find_element(*Authorization.recovery_password_button).click()

    driver.find_element(*Authorization.login_registration_form_button).click()

    login_page = LoginPageBurger(driver)

    login_page.login("nataliafrolova3678@ya.ru", "000018")

    time.sleep(3)

    assert driver.find_element(*Authorization.make_an_order_button).text == 'Оформить заказ'

    driver.quit()

