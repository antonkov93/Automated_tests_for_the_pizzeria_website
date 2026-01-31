import time
from urllib.parse import unquote
from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage


class MainPage(BasePage):

    page_url = 'https://pizzeria.skillbox.cc/'

    arrow_left_locator = (By.XPATH, '//a[@aria-label="previous"]')
    arrow_right_locator = (By.XPATH, '//a[@aria-label="next"]')
    pizza_4_in_1_image_locator = (By.XPATH, '(//a[@title="Пицца «4 в 1»"])[1]')
    pizza_4_in_1_into_cart_locator = (By.XPATH, '(//a[@data-product_id="425"])[1]')
    pizza_4_in_1_price_locator = (By.XPATH,
                                  "//a[@title='Пицца «4 в 1»']//span[@class='woocommerce-Price-amount amount']")
    pizza_pepperoni_image_locator = (By.XPATH, '(//a[@title="Пицца «Пепперони»"])[3]')
    ice_latte_locator = (By.XPATH, '(//a[@title="Айс латте"])[1]')
    ice_latte_into_cart_locator = (By.XPATH, '//a[@data-product_id="427"]')
    ice_latte_price_locator = (By.XPATH, "//a[@title='Айс латте']//span[@class='woocommerce-Price-amount amount']")
    navigation_menu_locator = (By.XPATH, '//div[@id="menu"]')
    pizza_slider_locator = (By.XPATH, '(//div[@aria-live="polite"])[2]')
    desserts_slider_locator = (By.XPATH, '(//div[@aria-live="polite"])[3]')
    drinks_slider_locator = (By.XPATH, '(//div[@aria-live="polite"])[4]')

    def check_title(self):
        assert "Pizzeria — Пиццерия" in self.driver.title, "Заголовок страницы не содержит 'Pizzeria - Пиццерия'"

    def check_visible_navigation_menu(self):
        navigation_menu = self.wait.until(EC.element_to_be_clickable(self.navigation_menu_locator))
        assert navigation_menu.is_displayed(), "Навигационное меню не отображается на главной странице"

    def check_visible_slider(self):
        pizza_slider = self.wait.until(EC.element_to_be_clickable(self.pizza_slider_locator))
        desserts_slider = self.wait.until(EC.element_to_be_clickable(self.desserts_slider_locator))
        drinks_slider = self.wait.until(EC.element_to_be_clickable(self.drinks_slider_locator))
        assert pizza_slider.is_displayed(), "Слайдер с пиццами не отображается на главной странице"
        assert desserts_slider.is_displayed(), "Слайдер с десертами не отображается на главной странице"
        assert drinks_slider.is_displayed(), "Слайдер с напитками не отображается на главной странице"

    def hover_cursor_pizza_4_in_1(self):
        pizza_4_in_1_image = self.wait.until(EC.element_to_be_clickable(self.pizza_4_in_1_image_locator))
        self.actions.move_to_element(pizza_4_in_1_image).perform()

    def hover_cursor_pizza_pepperoni(self):
        pizza_pepperoni = self.wait.until(EC.element_to_be_clickable(self.pizza_pepperoni_image_locator))
        self.actions.move_to_element(pizza_pepperoni).perform()

    def check_into_cart(self):
        pizza_4_in_1_into_cart = self.wait.until(EC.element_to_be_clickable(self.pizza_4_in_1_into_cart_locator))
        assert pizza_4_in_1_into_cart.is_displayed(), "Кнопка 'В корзину' не отображается в слайдере пицц"

    def click_slider_right(self, quantity_clicks):
        for i in range(quantity_clicks):
            self.wait.until(EC.element_to_be_clickable(self.arrow_right_locator)).click()
            time.sleep(0.5)

    def click_slider_left(self, quantity_clicks):
        for i in range(quantity_clicks):
            self.wait.until(EC.element_to_be_clickable(self.arrow_left_locator)).click()
            time.sleep(0.5)

    def check_work_slider(self):
        pizza_pepperoni_image = self.wait.until(EC.element_to_be_clickable(self.pizza_pepperoni_image_locator))
        assert pizza_pepperoni_image.is_displayed(), "Картинка пиццы 'Пепперони' не отображается при скроле слайдера"

    def click_into_cart_pizza(self):
        self.wait.until(EC.element_to_be_clickable(self.pizza_4_in_1_into_cart_locator)).click()

    def hover_cursor_drink(self):
        ice_latte_image = self.wait.until(EC.presence_of_element_located(self.ice_latte_locator))
        self.actions.scroll_to_element(ice_latte_image)
        self.actions.move_to_element(ice_latte_image).perform()
        self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))

    def click_into_cart_drink(self):
        self.wait.until(EC.element_to_be_clickable(self.ice_latte_into_cart_locator)).click()

    def check_total_amount_cart_header(self, expected_total):
        # Ждем, пока в корзине появится сумма больше 700₽ (пицца + напиток)
        self.wait.until(lambda driver: str(expected_total) in driver.find_element(
            *self.total_amount_cart_header_price_locator)
                        .text)
        pizza_price_text = self.wait.until(EC.visibility_of_element_located(self.pizza_4_in_1_price_locator)).text
        drink_price_text = self.wait.until(EC.visibility_of_element_located(self.ice_latte_price_locator)).text
        total_amount_cart_header_price_text = self.wait.until(
            EC.visibility_of_element_located(
                self.total_amount_cart_header_price_locator
            )
        ).text
        # Извлекаем числовые значения убирая/меняя символы
        pizza_price_normalized = float(pizza_price_text.replace('₽', '').replace(',', '.').strip())
        drink_price_normalized = float(drink_price_text.replace('₽', '').replace(',', '.').strip())
        total_amount_cart_header_price_normalized = float(
            total_amount_cart_header_price_text
            .replace('₽', '')
            .replace(',', '.')
            .replace('[', '')
            .replace(']', '')
            .strip()
        )
        sum_product = pizza_price_normalized + drink_price_normalized
        assert sum_product == total_amount_cart_header_price_normalized, \
            "Сумма корзины в хэдере не соответствует сумме добавленных товаров"

    def get_product_titles_from_main_page(self):
        """Получает названия товаров с главной страницы"""
        pizza_4_in_1_main = self.wait.until(EC.presence_of_element_located(
            self.pizza_4_in_1_image_locator)).get_attribute("title")
        ice_latte_main = self.wait.until(EC.presence_of_element_located(self.ice_latte_locator)).get_attribute("title")
        return pizza_4_in_1_main, ice_latte_main

    def check_title_product_cart(self, pizza_4_in_1_main, ice_latte_main):
        cart_page = CartPage(self.driver)
        # Меняем кавычки « на "
        pizza_4_in_1_main_normalized = pizza_4_in_1_main.replace('«', '"').replace('»', '"')
        pizza_4_in_1_cart = self.wait.until(EC.visibility_of_element_located(cart_page.pizza_4_in_1_text_locator)).text
        ice_latte_cart = self.wait.until(EC.visibility_of_element_located(cart_page.ice_latte_text_locator)).text
        assert pizza_4_in_1_main_normalized in pizza_4_in_1_cart, "Название пиццы в корзине не соответствует ожидаемому"
        assert ice_latte_main in ice_latte_cart, "Название напитка в корзине не соответствует ожидаемому"

    def click_image_pizza_4_in_1(self):
        self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        self.wait.until(EC.element_to_be_clickable(self.pizza_4_in_1_image_locator)).click()

    def check_product_page_loaded(self):
        self.wait.until(EC.url_contains(
            'https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-4-%d0%b2-1/'))
        # декодируем текущий url (т.к. в читабельном виде он содержит кириллицу)
        decoded_current_url = unquote(self.driver.current_url)
        expected_url = 'https://pizzeria.skillbox.cc/product/пицца-4-в-1/'
        assert expected_url in decoded_current_url, "Текущий URL не соответствует ожидаемому"
