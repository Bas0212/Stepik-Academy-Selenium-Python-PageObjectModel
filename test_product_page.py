# pytest -v -s --tb=line --browser_name=chrome --language=en test_product_page.py

from pages.product_page import ProductPage


def test_guest_should_see_busket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    
    
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.product_has_been_added_to_basket()
