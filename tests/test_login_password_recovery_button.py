from selenium.webdriver.common.by import By
import time

def test_login_password_recovery_button(driver):

    driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[2]/a").click()

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p/a").click()

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(
        "nataliafrolova3678@ya.ru")

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("000018")

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

    time.sleep(3)

    assert driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").text == 'Оформить заказ'

    driver.quit()
