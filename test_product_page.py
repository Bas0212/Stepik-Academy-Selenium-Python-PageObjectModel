# pytest -v -s --tb=line --browser_name=chrome --language=en test_product_page.py

import pytest
from pages.product_page import ProductPage


@pytest.mark.skip
def test_guest_should_see_busket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019' # Независимость от данных (https://stepik.org/lesson/201964/step/3?auth=login&unit=176022)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    
    
@pytest.mark.skip
@pytest.mark.parametrize('link', [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}' for offer in range(7)] +
                                 [pytest.param('fhttp://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7', marks=pytest.mark.xfail(reason='Bad link'))] +
                                 [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}' for offer in range(8, 10)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.product_has_been_added_to_basket()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared_success_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    