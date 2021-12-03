from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Basket button is not presented'

    def add_product_to_basket(self):
        busket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        busket_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name_and_price(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return {'name': product_name.text, 'price': product_price.text}

    def get_added_product_name_and_price(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_NAME)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_PRICE)
        return {'name': product_name.text, 'price': product_price.text}

    def product_has_been_added_to_basket(self):
        product = self.get_product_name_and_price()
        product_added = self.get_added_product_name_and_price()
        assert (product['name'] == product_added['name']) and (product['price'] == product_added['price']), 'The product has not been added to the basket'
