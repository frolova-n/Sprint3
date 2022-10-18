from selenium.webdriver.common.by import By
import time


def test_registration(driver):

    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Наталья")

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(
        "nataliafrolova3678@ya.ru")

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("000018")

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

    time.sleep(5)

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()