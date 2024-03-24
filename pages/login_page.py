import random
import string
import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    LOGIN_PAGE_LINK = "https://selenium1py.pythonanywhere.com/accounts/login/"

    def register_new_user(self):
        # Generate email and password
        email = str(time.time()) + "@fakemail.org"
        password = ''.join(random.choice(string.ascii_letters) for _ in range(9))
        # Fill and submit data to register form
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        retry_password_field = self.browser.find_element(*LoginPageLocators.RETRY_PASSWORD_FIELD)
        retry_password_field.send_keys(password)
        registration_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):       
        assert "login" in self.browser.current_url, \
            "Login URL incorrect"

    def should_be_login_form(self):
        assert bool(self.is_element_present(*LoginPageLocators.LOGIN_FORM)), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert bool(self.is_element_present(*LoginPageLocators.REGISTER_FORM)), \
            "Register form is not presented"
        