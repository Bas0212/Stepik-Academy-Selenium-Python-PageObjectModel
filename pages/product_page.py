from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Basket button is not presented'

    def add_product_to_basket(self):
        busket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        busket_button.click()
        self.solve_quiz_and_get_code()

    def product_has_been_added_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_added_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_NAME)
        product_added_price = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_PRICE)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert (product_name.text == product_added_name.text) and (product_price.text == product_added_price.text), 'The product has not been added to the basket'
