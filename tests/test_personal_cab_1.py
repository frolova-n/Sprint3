from selenium.webdriver.common.by import By
import time

def test_personal_cab_1(driver):

    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()

    time.sleep(3)

    assert driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").text == 'Войти'

    driver.quit()