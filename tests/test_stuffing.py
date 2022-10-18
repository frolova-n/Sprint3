from selenium.webdriver.common.by import By
import time

def test_stuffing_click(driver):

    driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]/span").click()

    time.sleep(3)

    assert driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[2]/ul[3]/a[1]/p').text == 'Мясо бессмертных моллюсков Protostomia'

    driver.quit()