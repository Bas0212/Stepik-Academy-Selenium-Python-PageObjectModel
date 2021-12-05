import pytest
from pages.locators import MainPageLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


@pytest.mark.guest_login
class TestGuestLoginFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = MainPageLocators.URL_MAIN


    @pytest.fixture(scope="function", autouse=True)
    def teardown(self):
        pass


    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.should_be_login_link()
        

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    

@pytest.mark.guest_empty_basket
class TestGuestEmptyBasketFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = MainPageLocators.URL_MAIN


    @pytest.fixture(scope="function", autouse=True)
    def teardown(self):
        pass


    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.view_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket_page()
