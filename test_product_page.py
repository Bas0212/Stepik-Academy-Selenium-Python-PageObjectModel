# pytest -v -s --tb=line --browser_name=chrome --language=en test_product_page.py

from pages.product_page import ProductPage


def test_guest_should_see_busket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019' # Независимость от данных (https://stepik.org/lesson/201964/step/3?auth=login&unit=176022)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    
    
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019' # Независимость от данных (https://stepik.org/lesson/201964/step/3?auth=login&unit=176022)
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.product_has_been_added_to_basket()
