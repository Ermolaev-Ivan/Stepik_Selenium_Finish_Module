from .base_page import BasePage
from .locators import LoginPageLocators




class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert LoginPageLocators.LOGIN_SUBSTRING in self.browser.current_url, 'substring "login" is not in URL'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'login form is None'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), 'register form is None'

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        self.browser.implicitly_wait(5)
        assert self.browser.find_element(*LoginPageLocators.MESSAGE_REGISTER)



