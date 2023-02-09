from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators


def compare_basket_with_product(price_basket, price_product):
    assert price_product == price_basket, "Price Product is't the same as Basket Product"


def compare_basket_name_with_product_name(product_name, name_in_basket):
    assert product_name == name_in_basket, "Wrong name"


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

    def get_success_massage(self):
        success_massage = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        return success_massage

    def get_product_name_basket(self):
        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        return product_name_basket

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be dissapear"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_EMPTY), \
            "Success message is presented, but should not be"