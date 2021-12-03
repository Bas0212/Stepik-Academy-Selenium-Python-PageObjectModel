from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_page(self):
        self.should_be_basket_url()
        self.should_be_empty_basket()
        self.should_not_be_items_in_basket()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, '<basket> is not in URL'

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), 'Basket is not empty'

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Items to buy is presented, but basket should be empty'
