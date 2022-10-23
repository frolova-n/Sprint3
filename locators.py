from selenium.webdriver.common.by import By

class BurgerLocators:

    sauses_button = [By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]/span"]

    buns_button = [By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[1]/span"]

    stuffing_button = [By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]/span"]

    fluorescent_bun_button = [By.XPATH, '/html/body/div/div/main/section[1]/div[2]/ul[1]/a[1]/p']

    meat_of_immortal_clams_button = [By.XPATH, '/html/body/div/div/main/section[1]/div[2]/ul[3]/a[1]/p']

    spicyx_sause_button = [By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[2]/a[1]/p"]

    constructor_button = [By.XPATH, "html/body/div/div/header/nav/ul/li[1]/a/p"]

    assemble_a_burger_header = [By.XPATH, "/html/body/div/div/main/section[1]/h1"]

    logo_Burger = [By.XPATH, "/html/body/div/div/header/nav/div"]

class Authorization:

    registration_form_button = [By.XPATH, "/html/body/div/div/main/div/div/p[1]/a"]

    name_registration_form_field = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input"]

    email_registration_form_field = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input"]

    password_registration_form_field = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input"]

    register_button = [By.XPATH, "/html/body/div/div/main/div/form/button"]

    wrong_password_header = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p"]

    login_registration_form_button = [By.XPATH, "/html/body/div/div/main/div/div/p/a"]

    login_button = [By.XPATH, "/html/body/div/div/main/section[2]/div/button"]

    email_field = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input"]

    password_field = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input"]

    entry_button = [By.XPATH, "/html/body/div/div/main/div/form/button"]

    recovery_password_button = [By.XPATH, "/html/body/div/div/main/div/div/p[2]/a"]

    make_an_order_button = [By.XPATH, "/html/body/div/div/main/section[2]/div/button"]

    personal_cab_button = [By.XPATH, "/html/body/div/div/header/nav/a"]

    orders_history_button = [By.XPATH, "/html/body/div/div/main/div/nav/ul/li[2]/a"]

    logout_button = [By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button"]



