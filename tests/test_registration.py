from locators import Authorization
import time

def test_registration(driver):

    driver.find_element(*Authorization.login_button).click()

    driver.find_element(*Authorization.registration_form_button).click()

    driver.find_element(*Authorization.name_registration_form_field).send_keys("Наталья")

    driver.find_element(*Authorization.email_registration_form_field).send_keys("nataliafrolova3678@ya.ru")

    driver.find_element(*Authorization.password_registration_form_field).send_keys("000018")

    driver.find_element(*Authorization.register_button).click()

    time.sleep(5)

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()


def test_wrong_password(driver):

    driver.find_element(*Authorization.login_button).click()

    driver.find_element(*Authorization.registration_form_button).click()

    driver.find_element(*Authorization.name_registration_form_field).send_keys("Наталья")

    driver.find_element(*Authorization.email_registration_form_field).send_keys("nataliafrolov32435@ya.ru")

    driver.find_element(*Authorization.password_registration_form_field).send_keys("00001")

    driver.find_element(*Authorization.register_button).click()

    time.sleep(3)

    assert driver.find_element(*Authorization.wrong_password_header).text == 'Некорректный пароль'

    driver.quit()

