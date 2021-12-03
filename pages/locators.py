from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'div.basket-mini a.btn')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link')
    
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')
    PRODUCT_ADDED_NAME = (By.CSS_SELECTOR, 'div.alert-success strong')
    PRODUCT_ADDED_PRICE = (By.CSS_SELECTOR, 'div.alert-info p strong')


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '#content_inner div.row')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
