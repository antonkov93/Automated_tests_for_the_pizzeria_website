import allure
from base.base_test import BaseTest


@allure.story('Тестирование страницы "Мой аккаунт"')
class TestMyAccountPage(BaseTest):

    @allure.title('Авторизация ранее зарегистрированного пользователя')
    def test_keys16(self):
        with allure.step('Перейти на страницу “Мой аккаунт” по ссылке: https://pizzeria.skillbox.cc/my-account/'):
            self.my_account_page.open()
        with allure.step('Заполнить поле "Имя пользователя или почта", например: hiddify'):
            username = self.my_account_page.enter_username('hiddify')
        with allure.step('Заполнить поле "Пароль", например: 1234'):
            self.my_account_page.enter_password('1234')
        with allure.step('Установить чекбокс “Запомнить меня”'):
            self.my_account_page.click_remember_me_checkbox()
        with allure.step('Нажать кнопку “Войти”'):
            self.my_account_page.click_login_button()
        with allure.step('Проверить загрузку страницы личного кабинета с приветствием по имени пользователя'):
            self.register_page.check_greeting_user_name(username)
