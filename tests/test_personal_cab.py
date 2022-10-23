from locators import Authorization
from locators import BurgerLocators
import time
from methods import LoginPageBurger

def test_personal_cab_1(driver):

    driver.find_element(*Authorization.personal_cab_button).click()

    time.sleep(3)

    assert driver.find_element(*Authorization.entry_button).text == 'Войти'

    driver.quit()

def test_personal_cab_2(driver):
    
    driver.find_element(*Authorization.login_button).click()

    login_page = LoginPageBurger(driver)

    login_page.login("nataliafrolova3678@ya.ru", "000018")

    driver.find_element(*Authorization.personal_cab_button).click()

    time.sleep(3)

    assert driver.find_element(*Authorization.orders_history_button).text == 'История заказов'

    driver.quit()


def test_constructor(driver):

    driver.find_element(*Authorization.login_button).click()

    login_page = LoginPageBurger(driver)

    login_page.login("nataliafrolova3678@ya.ru", "000018")

    driver.find_element(*Authorization.personal_cab_button).click()

    driver.find_element(*BurgerLocators.constructor_button).click()

    time.sleep(3)

    assert driver.find_element(*BurgerLocators.assemble_a_burger_header).text == 'Соберите бургер'

    driver.quit()


def test_logo_Burger(driver):

    driver.find_element(*Authorization.login_button).click()

    login_page = LoginPageBurger(driver)

    login_page.login("nataliafrolova3678@ya.ru", "000018")

    driver.find_element(*Authorization.personal_cab_button).click()

    time.sleep(3)

    driver.find_element(*BurgerLocators.logo_Burger).click()

    time.sleep(3)

    assert driver.find_element(*Authorization.make_an_order_button).text == 'Оформить заказ'

    driver.quit()

def test_logout_personal_cab(driver):

    driver.find_element(*Authorization.login_button).click()

    driver.find_element(*Authorization.email_field).send_keys("nataliafrolova3678@ya.ru")

    login_page = LoginPageBurger(driver)

    login_page.login("nataliafrolova3678@ya.ru", "000018")

    time.sleep(3)

    driver.find_element(*Authorization.personal_cab_button).click()

    time.sleep(3)

    driver.find_element(*Authorization.logout_button).click()

    time.sleep(3)

    assert driver.find_element(*Authorization.entry_button).text == 'Войти'

    driver.quit()





