from pages.base_page import BasePage
from pages.locators import BasePageLocators
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, '<login> is not in URL'


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'


    def register_new_user(self, email, password):
        if self.is_not_element_present(*BasePageLocators.USER_ICON):
            self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
            self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
            self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
            self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
            assert self.is_not_element_present(*LoginPageLocators.REGISTER_ALERT), 'Registration error'
            assert self.is_element_present(*LoginPageLocators.REGISTER_OK, 5), 'Registration error'
        else:
            print('\nGlad to see you again!')
            assert True