import allure
from base.base_test import BaseTest


@allure.story('Тестирование страницы "Бонусная программа"')
class TestBonusPage(BaseTest):

    @allure.title('Регистрация в бонусной программе')
    def test_keys24(self):
        with allure.step('Перейти на страницу бонусной программы: https://pizzeria.skillbox.cc/register/'):
            self.bonus_page.open()
        with allure.step('Нажать кнопку “Оформить карту” без заполнения обязательных полей'):
            self.bonus_page.click_apply_for_card()
        with allure.step('Проверить наличие сообщения с текстом валидации'):
            self.bonus_page.check_validation_message()
        with allure.step('Заполнить поле “Имя” не валидными данными, например, цифрами “123”'):
            self.bonus_page.enter_name('123')
        with allure.step('Заполнить поле “Телефон” не валидными данными, например, буквами “абвгд”'):
            self.bonus_page.enter_phone('абвгд')
        with allure.step('Нажать кнопку “Оформить карту”'):
            self.bonus_page.click_apply_for_card()
        with allure.step('Проверить наличие сообщения с текстом валидации'):
            self.bonus_page.check_validation_message()
        with allure.step('Заполнить поле “Имя” валидными данными, например: “Антон”'):
            self.bonus_page.enter_name('Антон')
        with allure.step('Заполнить поле “Телефон” валидными данными, например: “89251059619”'):
            self.bonus_page.enter_phone('89251059619')
        with allure.step('Нажать кнопку “Оформить карту”'):
            self.bonus_page.click_apply_for_card()
        with allure.step('Дождаться активации бонусной программы'):
            self.bonus_page.waiting_activation_bonus_program()
        with allure.step('Проверить что появилось сообщение об успешной активации: Ваша карта оформлена!'):
            self.bonus_page.check_confirmation_message('Ваша карта оформлена!')
