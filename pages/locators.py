from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    LOGIN_FORM = (By.ID, "login_form")
    PRICE_PRODUCT = (By.CLASS_NAME, "price_color")
    PRICE_BASKET = (By.XPATH, '//p[contains(text(), "Your basket total is now")]/strong')
    PRODUCT_NAME = (By.XPATH, '//h1')
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, ".alert:first-child>.alertinner >strong")