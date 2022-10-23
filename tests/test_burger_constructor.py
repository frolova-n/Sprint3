from locators import BurgerLocators
from locators import Authorization
import time
from methods import LoginPageBurger

def test_buns_click(driver):

    driver.find_element(*BurgerLocators.sauses_button).click()

    time.sleep(3)

    driver.find_element(*BurgerLocators.buns_button).click()

    assert driver.find_element(*BurgerLocators.fluorescent_bun_button).text == 'Флюоресцентная булка R2-D3'


def test_sauces_click(driver):

    driver.find_element(*Authorization.login_button).click()

    login_page = LoginPageBurger(driver)

    login_page.login("nataliafrolova3678@ya.ru", "000018")

    time.sleep(3)

    driver.find_element(*BurgerLocators.sauses_button).click()

    time.sleep(3)

    assert driver.find_element(*BurgerLocators.spicyx_sause_button).text == 'Соус Spicy-X'


def test_stuffing_click(driver):

    driver.find_element(*BurgerLocators.stuffing_button).click()

    time.sleep(3)

    assert driver.find_element(*BurgerLocators.meat_of_immortal_clams_button).text == 'Мясо бессмертных моллюсков Protostomia'

    driver.quit()