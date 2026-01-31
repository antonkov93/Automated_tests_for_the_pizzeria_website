import time

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from faker import Faker


class MakingOrderPage(BasePage):

    page_url = 'https://pizzeria.skillbox.cc/checkout/'

    # без авторизации
    authorization_requirements_locator = (By.XPATH, '//div[@class="woocommerce"]')

    # с авторизацией
    first_name_field_locator = (By.XPATH, '//*[@id="billing_first_name"]')
    last_name_field_locator = (By.XPATH, '//*[@id="billing_last_name"]')
    address_field_locator = (By.XPATH, '//*[@id="billing_address_1"]')
    city_field_locator = (By.XPATH, '//*[@id="billing_city"]')
    region_field_locator = (By.XPATH, '//*[@id="billing_state"]')
    index_field_locator = (By.XPATH, '//*[@id="billing_postcode"]')
    phone_field_locator = (By.XPATH, '//*[@id="billing_phone"]')
    email_field_locator = (By.XPATH, '//*[@id="billing_email"]')
    calendar_field_locator = (By.XPATH, '//*[@id="order_date"]')
    comment_field_locator = (By.XPATH, '//*[@id="order_comments"]')
    payment_delivery_radiobutton_locator = (By.XPATH, '//label[@for="payment_method_cod"]')
    terms_of_use_checkbox_locator = (By.XPATH, '//*[@id="terms"]')
    place_order_button_locator = (By.XPATH, '//*[@id="place_order"]')
    order_amount_locator = (By.XPATH, '//tr/td/strong/span[@class="woocommerce-Price-amount amount"]')

    fake = Faker('ru_RU')

    def check_text_authorization_requirements(self):
        authorization_requirements_text = self.wait.until(EC.visibility_of_element_located(
            self.authorization_requirements_locator)).text
        assert 'Для оформления заказа необходимо авторизоваться.' in authorization_requirements_text, \
            'На странице не содержится сообщения с требованием об авторизации'

    def check_delivery_all_fields(self):
        field_locators = [
            self.first_name_field_locator,
            self.last_name_field_locator,
            self.address_field_locator,
            self.city_field_locator,
            self.region_field_locator,
            self.index_field_locator,
            self.phone_field_locator,
            self.email_field_locator,
            self.calendar_field_locator,
            self.comment_field_locator
        ]
        for locator in field_locators:
            assert self.wait.until(EC.visibility_of_element_located(locator)), \
                f'Поле "{locator}" не найдено на странице'

    def enter_first_name(self, max_length_first_name):
        first_name = self.fake.first_name()[:max_length_first_name]
        self.wait.until(EC.element_to_be_clickable(self.first_name_field_locator)).clear()
        self.wait.until(EC.element_to_be_clickable(self.first_name_field_locator)).send_keys(first_name)
        return first_name

    def enter_last_name(self, max_length_last_name):
        last_name = self.fake.last_name()[:max_length_last_name]
        self.wait.until(EC.element_to_be_clickable(self.last_name_field_locator)).clear()
        self.wait.until(EC.element_to_be_clickable(self.last_name_field_locator)).send_keys(last_name)
        return last_name

    def enter_address(self, max_length_address):
        address = self.fake.street_address()[:max_length_address]
        self.wait.until(EC.element_to_be_clickable(self.address_field_locator)).clear()
        self.wait.until(EC.element_to_be_clickable(self.address_field_locator)).send_keys(address)
        return address

    def enter_city(self, max_length_city):
        city = self.fake.city()[:max_length_city]
        self.wait.until(EC.element_to_be_clickable(self.city_field_locator)).clear()
        self.wait.until(EC.element_to_be_clickable(self.city_field_locator)).send_keys(city)
        return city

    def enter_region(self, max_length_region):
        region = self.fake.region()[:max_length_region]
        self.wait.until(EC.element_to_be_clickable(self.region_field_locator)).clear()
        self.wait.until(EC.element_to_be_clickable(self.region_field_locator)).send_keys(region)
        return region

    def enter_index(self, length_index):
        index = str(self.fake.random_number(digits=length_index))
        self.wait.until(EC.element_to_be_clickable(self.index_field_locator)).clear()
        self.wait.until(EC.element_to_be_clickable(self.index_field_locator)).send_keys(index)
        return index

    def enter_phone(self, length_phone):
        phone = '7' + str(self.fake.random_number(digits=length_phone - 1)).zfill(length_phone - 1)
        self.wait.until(EC.element_to_be_clickable(self.phone_field_locator)).clear()
        self.wait.until(EC.element_to_be_clickable(self.phone_field_locator)).send_keys(phone)
        return phone

    def enter_calendar(self, days_from_now):
        # Генерируем дату через N дней от сегодня
        future_date = self.fake.future_date(end_date=f'+{days_from_now}d')
        date_string = future_date.strftime('%d-%m-%Y')
        self.wait.until(EC.element_to_be_clickable(self.calendar_field_locator)).clear()
        self.wait.until(EC.element_to_be_clickable(self.calendar_field_locator)).send_keys(date_string)

    def enter_comment(self, max_length_comment):
        comment = self.fake.text(max_nb_chars=max_length_comment)
        self.wait.until(EC.element_to_be_clickable(self.comment_field_locator)).clear()
        self.wait.until(EC.element_to_be_clickable(self.comment_field_locator)).send_keys(comment)
        return comment

    def check_email(self):
        email_field = self.wait.until(EC.visibility_of_element_located(self.email_field_locator))
        email_value = email_field.get_attribute('value')
        assert 'hiddify@mail.ru' in email_value

    def click_payment_delivery_radiobutton(self):
        self.wait.until(EC.element_to_be_clickable(self.payment_delivery_radiobutton_locator)).click()
        self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))

    def click_terms_of_use_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.terms_of_use_checkbox_locator)).click()

    def click_place_order_button(self):
        self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        self.wait.until(EC.element_to_be_clickable(self.place_order_button_locator)).click()
        time.sleep(1)

    def check_order_received_page(self):
        self.wait.until(EC.url_contains('https://pizzeria.skillbox.cc/checkout/order-received'))
        current_url = self.driver.current_url
        expected_url = 'https://pizzeria.skillbox.cc/checkout/order-received'
        assert expected_url in current_url, "Текущий URL не соответствует ожидаемому"

    def get_email(self):
        email_field = self.wait.until(EC.visibility_of_element_located(self.email_field_locator))
        return email_field.get_attribute('value')

    def get_order_amount(self):
        amount_text = self.wait.until(EC.visibility_of_element_located(self.order_amount_locator)).text
        return amount_text.replace(',', '.').strip()

    def get_payment_method(self):
        payment_method = self.wait.until(EC.visibility_of_element_located(
            self.payment_delivery_radiobutton_locator)).text
        return payment_method
