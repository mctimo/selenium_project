from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group>a")
    BASKET_EMPTY = (By.XPATH, "//a[text()='Continue shopping']")

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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
