from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MenuPage(BasePage):

    page_url = 'https://pizzeria.skillbox.cc/product-category/menu/'

    category_deserts_dropdown_locator = (By.XPATH, '(//a[contains(text(),"Десерты")])[1]')
    category_deserts_locator = (By.XPATH, '(//a[contains(text(),"Десерты")])[2]')
    right_slider_locator = (By.XPATH, '//span[@style="left: 100%;"]')
    min_price_filter_locator = (By.XPATH, '//span[@class="from"]')
    max_price_filter_locator = (By.XPATH, '//span[@class="to"]')
    filter_items_on_page_locator = (By.XPATH, '//span/span[@class="woocommerce-Price-amount amount"]')
    apply_button_locator = (By.XPATH, '//button[contains(text(),"Применить")]')
    cinnamon_bun_into_cart_locator = (By.XPATH, '//a[@data-product_id="437"]')
    pizza_4_in_1_into_cart_locator = (By.XPATH, '//a[@data-product_id="427"]')
    ice_latte_into_cart_locator = (By.XPATH, '//a[@data-product_id="425"]')

    def into_cart_pizza_4_in_1(self):
        self.wait.until(EC.element_to_be_clickable(self.pizza_4_in_1_into_cart_locator)).click()
        self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))

    def into_cart_ice_latte(self):
        self.wait.until(EC.element_to_be_clickable(self.ice_latte_into_cart_locator)).click()
        self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))

    def check_menu_page_loaded(self):
        self.wait.until(EC.url_contains('https://pizzeria.skillbox.cc/product-category/menu/'))
        current_url = self.driver.current_url
        expected_url = 'https://pizzeria.skillbox.cc/product-category/menu/'
        assert expected_url in current_url, "Текущий URL не соответствует ожидаемому"

    def hover_cursor_menu_header(self):
        menu_header = self.wait.until(EC.element_to_be_clickable(self.menu_header_locator))
        self.actions.move_to_element(menu_header).perform()

    def click_menu_header_deserts(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_header_deserts_locator)).click()

    def check_menu_page_deserts_loaded(self):
        self.wait.until(EC.url_contains('https://pizzeria.skillbox.cc/product-category/menu/deserts/'))
        current_url = self.driver.current_url
        expected_url = 'https://pizzeria.skillbox.cc/product-category/menu/deserts/'
        assert expected_url in current_url, "Текущий URL не соответствует ожидаемому"

    def click_deserts_category(self):
        self.wait.until(EC.element_to_be_clickable(self.category_deserts_locator)).click()

    def change_maximum_price_filter(self):
        right_slider = self.wait.until(EC.element_to_be_clickable(self.right_slider_locator))
        self.actions.click_and_hold(right_slider).move_by_offset(xoffset=-300, yoffset=0).perform()
        self.actions.release().perform()

    def click_apply_button(self):
        self.wait.until(EC.element_to_be_clickable(self.apply_button_locator)).click()

    def check_filter_cost_of_product(self):
        min_price_filter_text = self.wait.until(EC.visibility_of_element_located(self.min_price_filter_locator)).text
        max_price_filter_text = self.wait.until(EC.visibility_of_element_located(self.max_price_filter_locator)).text
        min_price_filter_normalize = float(min_price_filter_text.replace('₽', '').strip())
        max_price_filter_normalize = float(max_price_filter_text.replace('₽', '').strip())
        filter_items_on_page = self.wait.until(EC.visibility_of_all_elements_located(self.filter_items_on_page_locator))
        for filter_item_on_page in filter_items_on_page:
            filter_item_on_page_text = filter_item_on_page.text
            filter_item_on_page_normalize = float(filter_item_on_page_text.replace('₽', '').replace(',', '.').strip())
            assert min_price_filter_normalize <= filter_item_on_page_normalize <= max_price_filter_normalize, \
                "Цена товаров на странице не соответствует выбранному диапазону фильтра"

    def into_cart_cinnamon_bun(self):
        self.wait.until(EC.element_to_be_clickable(self.cinnamon_bun_into_cart_locator)).click()
