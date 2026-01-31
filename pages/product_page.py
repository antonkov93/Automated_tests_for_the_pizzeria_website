from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.cart_page import CartPage
from selenium.webdriver.support.select import Select


class ProductPage(BasePage):

    page_url = 'https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-4-%d0%b2-1/'

    pizza_board_dropdown_locator = (By.XPATH, '//select[@id="board_pack"]')
    cheese_board_locator = (By.XPATH, '//option[contains(text(),"Сырный")]')
    price_pizza_text_locator = (By.XPATH, "//h1[contains(text(), 'Пицца «4 в 1»')]/following-sibling::p//bdi")
    into_cart_button_locator = (By.XPATH, '//button[@name="add-to-cart"]')

    def choosing_cheese_board(self):
        pizza_board_dropdown = Select(self.wait.until(EC.element_to_be_clickable(self.pizza_board_dropdown_locator)))
        pizza_board_dropdown.select_by_index(1)

    def check_price_pizza(self, expected_pizza_price):
        pizza_price_text = self.wait.until(EC.visibility_of_element_located(self.price_pizza_text_locator)).text
        pizza_price_normalize = float(pizza_price_text.replace('₽', '').replace(',', '.').strip())
        assert pizza_price_normalize == expected_pizza_price, \
            "Цена пиццы с дополнительной опцией не соответствует ожидаемой"

    def click_into_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.into_cart_button_locator)).click()

    def check_additional_option_into_cart(self):
        cart_page = CartPage(self.driver)
        additional_option = self.wait.until(EC.visibility_of_element_located(cart_page.additional_option_locator))
        assert additional_option.is_displayed(), "Дополнительная опция не отображается в корзине"
