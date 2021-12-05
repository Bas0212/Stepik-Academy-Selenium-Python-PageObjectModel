import pytest
from pages.locators import LoginPageLocators, ProductPageLocators
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time     # import Faker


@pytest.mark.guest_add_to_basket
class TestGuestAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = ProductPageLocators.URL_PRODUCT_CODERS_AT_WORK


    @pytest.fixture(scope="function", autouse=True)
    def teardown(self):
        pass


    def test_guest_should_see_busket_button(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_basket_button()
        

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}' for offer in range(7)] +
                                    [pytest.param(f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7', marks=pytest.mark.xfail(reason='Bad link'))] +
                                    [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}' for offer in range(8, 10)])
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.product_has_been_added_to_basket()


    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = self.link
        link = ProductPageLocators.URL_PRODUCT_SHELLCODERS_HANDBOOK
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()


    def test_guest_cant_see_success_message(self, browser):
        link = self.link
        link = ProductPageLocators.URL_PRODUCT_SHELLCODERS_HANDBOOK
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


    @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = self.link
        link = ProductPageLocators.URL_PRODUCT_SHELLCODERS_HANDBOOK
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_disappeared_success_message()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LoginPageLocators.URL_LOGIN)
        page.open()

        # fake = Faker()
        email = str(time.time()) + '@fakemail.org'  # fake.email()
        password = 'Qwerty_12345'                   # fake.password()
        page.register_new_user(email, password)

        page.should_be_authorized_user()
        self.link = ProductPageLocators.URL_PRODUCT_SHELLCODERS_HANDBOOK


    @pytest.fixture(scope="function", autouse=True)
    def teardown(self):
        pass


    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()


    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_product_to_basket()
        page.product_has_been_added_to_basket()


@pytest.mark.guest_login
class TestGuestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = ProductPageLocators.URL_CITY_AND_STARTS


    @pytest.fixture(scope="function", autouse=True)
    def teardown(self):
        pass


    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()


    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
    

@pytest.mark.guest_empty_basket
class TestGuestEmptyBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = ProductPageLocators.URL_CITY_AND_STARTS


    @pytest.fixture(scope="function", autouse=True)
    def teardown(self):
        pass


    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.view_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket_page()
