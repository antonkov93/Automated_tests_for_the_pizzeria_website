import allure
from base.base_test import BaseTest


@allure.story('Тестирование страницы "Описание товара"')
class TestProductPage(BaseTest):

    @allure.title('Добавление в корзину пиццы с дополнительной опцией')
    def test_keys06(self):
        with allure.step('Перейти на страницу с описанием товара “Пицца 4 в 1”:'
                         ' https://pizzeria.skillbox.cc/product/пицца-4-в-1'):
            self.product_page.open()
        with allure.step('Выбрать опцию "Сырный борт"'):
            self.product_page.choosing_cheese_board()
        with allure.step('Проверить изменение цены пиццы'):
            self.product_page.check_price_pizza(490.0)
        with allure.step('Нажать кнопку “В корзину”'):
            self.product_page.click_into_cart()
        with allure.step('Нажать на ссылку “Корзина” в шапке'):
            self.base_page.click_cart_header()
        with allure.step('Проверить что пицца добавлена с дополнительной опцией'):
            self.product_page.check_additional_option_into_cart()
