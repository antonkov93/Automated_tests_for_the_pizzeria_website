import allure
from base.base_test import BaseTest
from helpers_function.helpers_function import (download_cookies_and_filling_cart, making_order,
                                               download_cookies_and_clear_cart)


@allure.story('Тестирование страницы "Оформление заказа"')
class TestMakingOrderPage(BaseTest):

    @allure.title('Проверка требования авторизации при оформлении заказа')
    def test_keys13(self):
        with allure.step('Перейти на главную страницу по ссылке: https://pizzeria.skillbox.cc/'):
            self.main_page.open()
        with allure.step('Навести мышь на товар в слайдере “Пицца 4 в 1” и добавить в корзину'):
            self.main_page.hover_cursor_pizza_4_in_1()
            self.main_page.click_into_cart_pizza()
        with allure.step('Нажать на ссылку “Корзина” в шапке'):
            self.base_page.click_cart_header()
        with allure.step('Нажать на кнопку “Перейти к оплате”'):
            self.cart_page.click_proceed_payment()
        with allure.step('Проверить загрузку страницы с наличием сообщения о требовании авторизации'):
            self.making_order_page.check_text_authorization_requirements()

    @allure.title('Переход к оформлению заказа')
    def test_keys17(self):
        # пересохранение куков, т.к. со временем они протухают
        self.my_account_page.save_cookies()
        # загрузка куков и очистка корзины с предыдущей сессии (выполнение предусловий тест-кейса)
        download_cookies_and_clear_cart(self)
        # начало выполнения тест-кейса
        with allure.step('Перейти в каталог товаров по ссылке: https://pizzeria.skillbox.cc/product-category/menu/'):
            self.menu_page.open()
        with allure.step('Добавить в корзину Айс Латте, Пиццу 4 в 1'):
            self.menu_page.into_cart_pizza_4_in_1()
            self.menu_page.into_cart_ice_latte()
        with allure.step('Нажать на ссылку “Корзина” в шапке'):
            self.base_page.click_cart_header()
        with allure.step('Нажать на кнопку “Перейти к оплате”'):
            self.cart_page.click_proceed_payment()
        with allure.step('Проверить загрузку страницы с наличием всех необходимых полей для оформления заказа'):
            self.making_order_page.check_delivery_all_fields()

    @allure.title('Оформление заказа')
    def test_keys18(self):
        # загрузка куков и заполнение корзины (выполнение предусловий тест-кейса)
        download_cookies_and_filling_cart(self)
        # начало выполнения тест-кейса
        with allure.step('Перейти на страницу оформления заказа по ссылке: https://pizzeria.skillbox.cc/checkout/'):
            self.making_order_page.open()
        with allure.step('Заполнить все поля необходимые для доставки и оформить заказ'):
            making_order(self)  # заполнение полей и оформление заказа (описание шагов в helpers_function.py)
        with allure.step('Проверить загрузку страницы подтверждения заказа'):
            self.making_order_page.check_order_received_page()
