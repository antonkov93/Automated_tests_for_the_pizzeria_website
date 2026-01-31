import allure
from base.base_test import BaseTest


@allure.story('Тестирование страницы "Главная"')
class TestMainPage(BaseTest):

    @allure.title('Проверка отображения основных элементов главной страницы')
    def test_keys01(self):
        with allure.step('Перейти на главную страницу по ссылке: https://pizzeria.skillbox.cc/'):
            self.main_page.open()
        with allure.step('Проверить наличие заголовка страницы "Pizzeria"'):
            self.main_page.check_title()
        with allure.step('Проверить наличие навигационного меню'):
            self.main_page.check_visible_navigation_menu()
        with allure.step('Проверить отображение блоков с товарами'):
            self.main_page.check_visible_slider()

    @allure.title('Проверка появления кнопки "В корзину" при наведении на картинку')
    def test_keys02(self):
        with allure.step('Перейти на главную страницу по ссылке: https://pizzeria.skillbox.cc/'):
            self.main_page.open()
        with allure.step('Навести курсор на изображение (карточку) товара в слайдере'):
            self.main_page.hover_cursor_pizza_4_in_1()
        with allure.step('Проверить появление кнопки "В корзину"'):
            self.main_page.check_into_cart()
        with allure.step('Нажать кнопку “В корзину”'):
            self.main_page.click_into_cart_pizza()

    @allure.title('Проверка функциональности слайдера')
    def test_keys03(self):
        with allure.step('Перейти на главную страницу по ссылке: https://pizzeria.skillbox.cc/'):
            self.main_page.open()
        with allure.step('Нажать кнопку переключения слайдера вправо два раза'):
            self.main_page.hover_cursor_pizza_4_in_1()
            self.main_page.click_slider_right(2)
        with allure.step('Нажать кнопку переключения слайдера влево один раз'):
            self.main_page.hover_cursor_pizza_pepperoni()
            self.main_page.click_slider_left(1)
        with allure.step('Проверить появление картинки пиццы “Пепперони”'):
            self.main_page.check_work_slider()

    @allure.title('Добавление товара в корзину с главной страницы')
    def test_keys04(self):
        with allure.step('Перейти на главную страницу по ссылке: https://pizzeria.skillbox.cc/'):
            self.main_page.open()
            # Получаем названия товаров с главной страницы ДО перехода в корзину
            pizza_4_in_1_main, ice_latte_main = self.main_page.get_product_titles_from_main_page()
        with allure.step('Навести курсор на любой товар в слайдере “Пицца”'):
            self.main_page.hover_cursor_pizza_4_in_1()
        with allure.step('Нажать кнопку "В корзину"'):
            self.main_page.click_into_cart_pizza()
        with allure.step('Навести курсор на любой товар в блоке “Напитки”'):
            self.main_page.hover_cursor_drink()
        with allure.step('Нажать кнопку “В корзину”'):
            self.main_page.click_into_cart_drink()
        with allure.step('Проверить изменение счетчика корзины в шапке и соответствие суммы выбранных товаров'):
            self.main_page.check_total_amount_cart_header(735)
        with allure.step('Нажать на ссылку “Корзина” в шапке'):
            self.base_page.click_cart_header()
        with allure.step('Проверить наличие выбранных товаров в корзине'):
            self.main_page.check_title_product_cart(pizza_4_in_1_main, ice_latte_main)

    @allure.title('Переход к странице описания товара из слайдера')
    def test_keys05(self):
        with allure.step('Перейти на главную страницу по ссылке: https://pizzeria.skillbox.cc/'):
            self.main_page.open()
        with allure.step('Нажать на изображение товара в слайдере'):
            self.main_page.click_image_pizza_4_in_1()
        with allure.step('Проверить загрузку страницы с описанием товара'):
            self.main_page.check_product_page_loaded()
