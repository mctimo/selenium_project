from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        login_link.click()

    def get_product_prise(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        return price_product

    def get_basket_price(self):
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        return price_basket

    def get_product_name_main(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_name_basket(self):
        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        return product_name_basket

    def compare_basket_with_product(self, price_basket, price_product):
        assert price_product == price_basket, "Price Product is't the same as Basket Product"

    def compare_basket_name_with_product_name(self, product_name, name_in_basket):
        assert product_name == name_in_basket, "Wrong name"