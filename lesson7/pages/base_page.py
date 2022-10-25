from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators
from .locators import BasePageLocators

class BasePage():

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def should_be_authorized(self):
        assert self.element_is_present(*BasePageLocators.USER_ICON)
