# pytest -v -s --tb=line --browser_name=chrome --language=en test_main_page.py

from pages.main_page import MainPage
# Вариант 2
from pages.login_page import LoginPage


def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
    
def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com'
    page = MainPage(browser, link)
    page.open()
    # Вариант 1 (https://stepik.org/lesson/238819/step/9?auth=login&unit=211271)
    # login_page = page.go_to_login_page()
    # login_page.should_be_login_page()
    # Вариант 2 (https://stepik.org/lesson/238819/step/9?auth=login&unit=211271)
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    