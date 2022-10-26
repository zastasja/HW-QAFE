from .locators import LoginPageLocators
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_from()


    def should_be_login_link(self):
        assert 'login' in self.browser.current_url, 'wrong url'

    def should_be_login_form(self):
        assert self.element_is_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_from(self):
        assert self.element_is_present(*LoginPageLocators.REGISTER_FORM)

    def register_user(self, email='email', password='password'):
        email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_input.send_keys(email)
        pass_input = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        pass_input.send_keys(password)
        pass_confirm_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        pass_confirm_input.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BTN).click()