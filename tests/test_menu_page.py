import allure
from base.base_test import BaseTest


@allure.story('Тестирование страницы "Меню"')
class TestMenuPage(BaseTest):

    @allure.title('Проверка перехода на страницу “Меню”')
    def test_keys09(self):
        with allure.step('Перейти на главную страницу по ссылке: https://pizzeria.skillbox.cc/'):
            self.main_page.open()
        with allure.step('Нажать на ссылку “Меню” в шапке'):
            self.base_page.click_menu_header()
        with allure.step('Проверить загрузку страницы “Меню”'):
            self.menu_page.check_menu_page_loaded()

    @allure.title('Переход в определенную категорию меню через выпадающий список')
    def test_keys10(self):
        with allure.step('Перейти на главную страницу по ссылке: https://pizzeria.skillbox.cc/'):
            self.main_page.open()
        with allure.step('Навести мышь на ссылку “Меню” в шапке'):
            self.menu_page.hover_cursor_menu_header()
        with allure.step('В выпадающем меню нажать на категорию “Десерты”'):
            self.menu_page.click_menu_header_deserts()
        with allure.step('Проверить загрузку страницы с десертами (“Меню/Десерты”)'):
            self.menu_page.check_menu_page_deserts_loaded()

    @allure.title('Выбор категории товаров со страницы “Меню”')
    def test_keys11(self):
        with allure.step('Перейти на страницу меню: https://pizzeria.skillbox.cc/product-category/menu/'):
            self.menu_page.open()
        with allure.step('Нажать на категорию "Десерты" в фильтре'):
            self.menu_page.click_deserts_category()
        with allure.step('Проверить загрузку страницы с десертами (“Меню/Десерты”)'):
            self.menu_page.check_menu_page_deserts_loaded()

    @allure.title('Фильтрация товаров по цене и добавление в корзину')
    def test_keys12(self):
        with allure.step('Перейти на страницу меню: https://pizzeria.skillbox.cc/product-category/menu/'):
            self.menu_page.open()
        with allure.step('Установить в фильтре максимальную цену 140 рублей'):
            self.menu_page.change_maximum_price_filter()
        with allure.step('Нажать кнопку "Применить"'):
            self.menu_page.click_apply_button()
        with allure.step('Проверить стоимость отображаемых товаров'):
            self.menu_page.check_filter_cost_of_product()
        with allure.step('Добавить Десерт «Булочка с корицей» в корзину'):
            self.menu_page.into_cart_cinnamon_bun()
