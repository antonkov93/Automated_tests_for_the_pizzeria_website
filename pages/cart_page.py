from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.menu_page import MenuPage


class CartPage(BasePage):

    page_url = 'https://pizzeria.skillbox.cc/cart/'

    pizza_4_in_1_text_locator = (By.XPATH, "//a[contains(text(),'4 в 1')]")
    ice_latte_text_locator = (By.XPATH, "//a[contains(text(),'Айс латте')]")
    quantity_field_item01_locator = (By.XPATH, '(//input[@type="number"])[1]')
    delete_button_item01_locator = (By.XPATH, '//a[@data-product_id="427"]')
    quantity_field_item02_locator = (By.XPATH, '(//input[@type="number"])[2]')
    delete_button_item02_locator = (By.XPATH, '//a[@data-product_id="425"]')
    update_cart_button_locator = (By.XPATH, '//button[@name="update_cart"]')
    coupon_field_locator = (By.XPATH, '//input[@id="coupon_code"]')
    apply_coupon_field_locator = (By.XPATH, '//button[@name="apply_coupon"]')
    remove_coupon_field_locator = (By.XPATH, '//a[@class="woocommerce-remove-coupon"]')
    proceed_payment_button_locator = (By.XPATH, '//a[contains(text(),"ПЕРЕЙТИ К ОПЛАТЕ")]')
    additional_option_locator = (By.XPATH, "//p[contains(text(), 'борт')]")
    sum_cart_locator = (By.XPATH, '//tr[@class="order-total"]/td/strong/span')
    delete_button_locators = (By.XPATH, '//a[@class="remove"]')  # локаторы кнопки удаления ВСЕХ товаров в корзине

    def increase_quantity_product(self, quantity_clicks):
        for i in range(quantity_clicks):
            self.wait.until(EC.element_to_be_clickable(self.quantity_field_item01_locator)).send_keys(Keys.ARROW_UP)

    def decrease_quantity_product(self, quantity_clicks):
        for i in range(quantity_clicks):
            self.wait.until(EC.element_to_be_clickable(self.quantity_field_item01_locator)).send_keys(Keys.ARROW_DOWN)

    def enter_quantity_field(self, quantity):
        quantity_field_item02 = self.wait.until(EC.element_to_be_clickable(self.quantity_field_item02_locator))
        quantity_field_item02.clear()
        quantity_field_item02.send_keys(quantity)

    def click_update_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.update_cart_button_locator)).click()

    def check_quantity_field(self, expected_quantity_item01, expected_quantity_item02):
        pizza_4_in_1 = self.wait.until(EC.visibility_of_element_located(self.quantity_field_item01_locator))
        ice_latte = self.wait.until(EC.visibility_of_element_located(self.quantity_field_item02_locator))
        pizza_4_in_1_quantity = int(pizza_4_in_1.get_attribute('value'))
        ice_latte_quantity = int(ice_latte.get_attribute('value'))
        assert pizza_4_in_1_quantity == expected_quantity_item01, 'Количество Пиццы 4 в 1 не соответствует ожидаемому'
        assert ice_latte_quantity == expected_quantity_item02, 'Количество Айс Латте не соответствует ожидаемому'

    def check_sum_cart(self, expected_sum):
        # ожидаем окончание анимации обновления корзины
        self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        sum_cart_text = self.wait.until(EC.visibility_of_element_located(self.sum_cart_locator)).text
        sum_cart_normalize = float(sum_cart_text.replace('₽', '').replace(',', '.').strip())
        assert sum_cart_normalize == expected_sum, f"Сумма корзины = {sum_cart_normalize}, а ожидается {expected_sum}"

    def delete_item_cart(self, item_number):
        locators = {
            1: self.delete_button_item01_locator,
            2: self.delete_button_item02_locator
        }
        assert item_number in locators, (f"Данный номер товара недоступен. "
                                         f"Нужно использовать доступные номера или добавить новый локатор вручную."
                                         f" Доступные номера: {list(locators.keys())}")
        self.wait.until(EC.element_to_be_clickable(locators[item_number])).click()
        self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))

    def check_item_deleted(self):
        self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        try:
            self.wait.until(EC.presence_of_element_located(self.ice_latte_text_locator))
            assert False, 'Товар не удалился из корзины'
        except TimeoutException:
            print('Товар успешно удален из корзины')

    def click_proceed_payment(self):
        self.wait.until(EC.element_to_be_clickable(self.proceed_payment_button_locator)).click()

    def clear_cart_and_remove_coupon(self):
        # Проверяем наличие примененного промокода
        remove_coupon_buttons = self.driver.find_elements(*self.remove_coupon_field_locator)
        # если использовать find_element и промокода не будет, то выведется ошибка NoSuchElementException
        # если использовании find_elements и промокода не будет, то вернется просто пустой список
        if len(remove_coupon_buttons) > 0:
            remove_coupon_buttons[0].click()
            self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        # Считаем сколько товаров в корзине в данный момент
        delete_buttons = self.driver.find_elements(*self.delete_button_locators)
        count = len(delete_buttons)
        # Удаляем каждый товар по одному
        for i in range(count):
            self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
            self.wait.until(EC.element_to_be_clickable(self.delete_button_locators)).click()

    def filling_cart(self):
        menu_page = MenuPage(self.driver)
        self.wait.until(EC.element_to_be_clickable(menu_page.pizza_4_in_1_into_cart_locator)).click()
        self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        self.wait.until(EC.element_to_be_clickable(menu_page.ice_latte_into_cart_locator)).click()

    def enter_and_apply_coupon(self, coupon):
        coupon_field = self.wait.until(EC.element_to_be_clickable(self.coupon_field_locator))
        coupon_field.clear()
        coupon_field.send_keys(coupon)
        self.wait.until(EC.element_to_be_clickable(self.apply_coupon_field_locator)).click()

    def block_coupon_requests(self):
        """Блокирует запрос на применение промокода через Chrome DevTools Protocol"""
        self.driver.execute_cdp_cmd('Network.enable', {})
        self.driver.execute_cdp_cmd('Network.setBlockedURLs', {
            'urls': ['*wc-ajax=apply_coupon*']
        })  # со значением '*apply_coupon*' тоже работает, т.к. блокирует любой URL, содержащий "apply_coupon"

    def unblock_coupon_requests(self):
        """Снимает блокировку запроса на применение промокода"""
        self.driver.execute_cdp_cmd('Network.setBlockedURLs', {'urls': []})
        self.driver.execute_cdp_cmd('Network.disable', {})
