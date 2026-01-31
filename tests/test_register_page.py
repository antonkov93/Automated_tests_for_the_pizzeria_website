import allure
from base.base_test import BaseTest
from helpers_function.helpers_function import registration_new_user


@allure.story('Тестирование страницы "Регистрация"')
class TestRegisterPage(BaseTest):

    @allure.title('Проверка перехода на страницу регистрации')
    def test_keys14(self):
        with allure.step('Перейти на главную страницу по ссылке: https://pizzeria.skillbox.cc/'):
            self.main_page.open()
        with allure.step('Нажать на ссылку “Мой аккаунт” в шапке'):
            self.main_page.click_my_account_header()
        with allure.step('Нажать кнопку "Зарегистрироваться"'):
            self.my_account_page.click_registration_button()
        with allure.step('Проверить загрузку страницы регистрации'):
            self.register_page.check_registration_page_loaded()

    @allure.title('Регистрация нового пользователя и проверка авторизации после регистрации')
    def test_keys15(self):
        with allure.step('Перейти на страницу регистрации по ссылке: https://pizzeria.skillbox.cc/register/'):
            self.register_page.open()
        with allure.step('Заполнить все поля пользовательских данных и провести регистрацию'):
            username = registration_new_user(self)  # рег-ия нового пользователя (описание шагов в helpers_function.py)
        with allure.step('Нажать на ссылку “Мой аккаунт” в шапке'):
            self.base_page.click_my_account_header()
        with allure.step('Проверить загрузку страницы личного кабинета с приветствием по имени пользователя'):
            self.register_page.check_greeting_user_name(username)
