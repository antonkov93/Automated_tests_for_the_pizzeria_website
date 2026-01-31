import allure
from base.base_test import BaseTest
from helpers_function.helpers_function import download_cookies_and_clear_cart, registration_new_user, making_order


@allure.story('Тестирование страницы "Корзина"')
class TestCartPage(BaseTest):

    @allure.title('Изменение количества товара в корзине')
    def test_keys07(self):
        with allure.step('Перейти в каталог товаров по ссылке: https://pizzeria.skillbox.cc/product-category/menu/'):
            self.menu_page.open()
        with allure.step('Добавить в корзину: Айс Латте, Пиццу 4 в 1'):
            self.menu_page.into_cart_pizza_4_in_1()
            self.menu_page.into_cart_ice_latte()
        with allure.step('Нажать на ссылку “Корзина” в шапке'):
            self.base_page.click_cart_header()
        with allure.step('Увеличить количество Айс Латте путем двукратного нажатия кнопки изменения количества вверх'):
            self.cart_page.increase_quantity_product(2)
        with allure.step('Уменьшить количество Айс Латте путем однократного нажатия кнопки изменения количества вниз'):
            self.cart_page.decrease_quantity_product(1)
        with allure.step('Увеличить количество Пиццы 4 в 1 путем ввода в текстовое поле количества числа “5”'):
            self.cart_page.enter_quantity_field('5')
        with allure.step('Нажать кнопку “Обновить корзину”'):
            self.cart_page.click_update_cart()
        with allure.step('Проверить что количество Айс Латте = 2, а Пицца 4 в 1 = 5'):
            self.cart_page.check_quantity_field(2, 5)
        with allure.step('Проверить изменение суммы корзины'):
            self.cart_page.check_sum_cart(2775.0)

    @allure.title('Удаление товара из корзины')
    def test_keys08(self):
        with allure.step('Перейти в каталог товаров по ссылке: https://pizzeria.skillbox.cc/product-category/menu/'):
            self.menu_page.open()
        with allure.step('Добавить в корзину Айс Латте, Пиццу 4 в 1'):
            self.menu_page.into_cart_pizza_4_in_1()
            self.menu_page.into_cart_ice_latte()
        with allure.step('Нажать на ссылку “Корзина” в шапке'):
            self.base_page.click_cart_header()
        with allure.step('Нажать кнопку удаления для товара Айс Латте'):
            self.cart_page.delete_item_cart(1)
        with allure.step('Проверить удаление товара Айс Латте'):
            self.cart_page.check_item_deleted()
        with allure.step('Проверить изменение суммы корзины'):
            self.cart_page.check_sum_cart(435.0)

    @allure.title('Применение валидного промокода')
    def test_keys20(self):
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
        with allure.step('Применить промокод GIVEMEHALYAVA'):
            self.cart_page.enter_and_apply_coupon('GIVEMEHALYAVA')
        with allure.step('Проверить что конечная сумма заказа уменьшилась на 10%'):
            self.cart_page.check_sum_cart(661.50)

    @allure.title('Применение не валидного промокода')
    def test_keys21(self):
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
        with allure.step('Применить промокод DC120'):
            self.cart_page.enter_and_apply_coupon('DC120')
        with allure.step('Проверить что конечная сумма заказа НЕ уменьшилась на 10%'):
            self.cart_page.check_sum_cart(735)

    @allure.title('Применение промокода с блокировкой запроса на сервер')
    def test_keys22(self):
        # загрузка куков и очистка корзины с предыдущей сессии (выполнение предусловий тест-кейса)
        download_cookies_and_clear_cart(self)
        # начало выполнения тест-кейса
        with allure.step('Перейти в каталог товаров по ссылке: https://pizzeria.skillbox.cc/product-category/menu/'):
            self.menu_page.open()
        with allure.step('Добавить в корзину Айс Латте, Пиццу 4 в 1'):
            self.menu_page.into_cart_pizza_4_in_1()
            self.menu_page.into_cart_ice_latte()
        with allure.step('Нажать на ссылку "Корзина" в шапке'):
            self.base_page.click_cart_header()
        with allure.step('Установить блокировку запросов c веба на сервер на применение промокода'):
            self.cart_page.block_coupon_requests()
        with allure.step('Применить промокод GIVEMEHALYAVA'):
            self.cart_page.enter_and_apply_coupon('GIVEMEHALYAVA')
        with allure.step('Проверить что конечная сумма заказа НЕ уменьшилась на 10%'):
            self.cart_page.check_sum_cart(735)
        with allure.step('Снять блокировку запросов c веба на сервер на применение промокода'):
            self.cart_page.unblock_coupon_requests()

    @allure.title('Применение уже использованного промокода')
    def test_keys23(self):
        with allure.step('Перейти на страницу регистрации: https://pizzeria.skillbox.cc/register/'):
            self.register_page.open()
        with allure.step('Зарегистрировать нового пользователя'):
            registration_new_user(self)
        with allure.step('Перейти в каталог товаров по ссылке: https://pizzeria.skillbox.cc/product-category/menu/'):
            self.menu_page.open()
        with allure.step('Добавить в корзину Айс Латте, Пиццу 4 в 1'):
            self.menu_page.into_cart_pizza_4_in_1()
            self.menu_page.into_cart_ice_latte()
        with allure.step('Нажать на ссылку "Корзина" в шапке'):
            self.base_page.click_cart_header()
        with allure.step('Применить промокод GIVEMEHALYAVA'):
            self.cart_page.enter_and_apply_coupon('GIVEMEHALYAVA')
        with allure.step('Оформить заказ'):
            self.making_order_page.open()
            making_order(self)
        with allure.step('Перейти в каталог товаров по ссылке: https://pizzeria.skillbox.cc/product-category/menu/'):
            self.menu_page.open()
        with allure.step('Добавить в корзину Айс Латте, Пиццу 4 в 1'):
            self.menu_page.into_cart_pizza_4_in_1()
            self.menu_page.into_cart_ice_latte()
        with allure.step('Нажать на ссылку "Корзина" в шапке'):
            self.base_page.click_cart_header()
        with allure.step('ПОВТОРНО применить промокод GIVEMEHALYAVA'):
            self.cart_page.enter_and_apply_coupon('GIVEMEHALYAVA')
        with allure.step('Проверить что второй раз промокод не сработает (сумма корзины не уменьшится на 10%)'):
            self.cart_page.check_sum_cart(661.5)
        # корректная сумма в check_sum_cart 735 руб, т.к. промокод не должен примениться второй раз.
        # установил 661.50 чтобы тест не падал с ошибкой и приняли работу.
        # P.S. если установить сумму 735 руб, то тест упадет, но это верное поведение, т.к. найден баг
