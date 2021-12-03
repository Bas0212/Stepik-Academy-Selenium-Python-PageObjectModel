from pages.base_page import BasePage
# Вариант 1 (https://stepik.org/lesson/238819/step/9?auth=login&unit=211271)
# from pages.login_page import LoginPage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # Вариант 1 (https://stepik.org/lesson/238819/step/9?auth=login&unit=211271)
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # Обработка alert (https://stepik.org/lesson/238819/step/10?auth=login&unit=211271)
        # alert = self.browser.switch_to.alert
        # alert.accept()
