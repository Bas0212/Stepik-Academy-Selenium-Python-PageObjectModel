from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'div.basket-mini a.btn')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    URL_MAIN = 'http://selenium1py.pythonanywhere.com/'


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')
    REGISTER_ALERT = (By.CSS_SELECTOR, 'div.alert-danger')
    REGISTER_OK = (By.CSS_SELECTOR, 'i.icon-ok-sign')
    URL_LOGIN = 'http://selenium1py.pythonanywhere.com/accounts/login/'


class ProductPageLocators():
    BASKET_ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    PRODUCT_ADDED_NAME = (By.CSS_SELECTOR, 'div.alert-success strong')
    PRODUCT_ADDED_PRICE = (By.CSS_SELECTOR, 'div.alert-info p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')
    URL_CITY_AND_STARTS = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    URL_PRODUCT_CODERS_AT_WORK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    URL_PRODUCT_SHELLCODERS_HANDBOOK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '#content_inner div.row')
