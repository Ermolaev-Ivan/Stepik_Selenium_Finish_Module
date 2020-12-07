from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логин


def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_should_be_login_page(browser):  # общий тест для login_page
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
'''тесты по одному'''
# def test_should_register_form_login_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_register_form()


# def test_should_login_form_login_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_form()
#
#
# def test_should_be_login_url_login_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_url()
