from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderReceivedPage(BasePage):

    page_url = 'https://pizzeria.skillbox.cc/checkout/order-received/'

    order_amount_locator = (By.XPATH, '//strong/span[@class="woocommerce-Price-amount amount"]')
    order_number_locator = (By.XPATH, '//li[@class="woocommerce-order-overview__order order"]')
    email_field_locator = (By.XPATH, '//li[@class="woocommerce-order-overview__email email"]/strong')
    payment_method_locator = (By.XPATH, '//tr/th[contains(text(),"Payment method:")]/../td')
    comment_field_locator = (By.XPATH, '//tr/th[contains(text(),"Note:")]/../td')
    full_shipping_information_locator = (By.XPATH, '//h2[@class="woocommerce-column__title"]/../address')
    phone_locator = (By.XPATH, '//p[@class="woocommerce-customer-details--phone"]')

    def check_order_amount(self, expected_amount):
        order_amount_text = self.wait.until(EC.visibility_of_element_located(self.order_amount_locator)).text
        order_amount_normalize = order_amount_text.replace(',', '.').strip()
        assert order_amount_normalize == expected_amount, \
            f"Сумма заказа не соответствует ожидаемой. Ожидалось: {expected_amount}, получено: {order_amount_normalize}"

    def check_order_number(self):
        order_number_text = self.wait.until(EC.visibility_of_element_located(self.order_number_locator)).text
        assert order_number_text, "Номер заказа отсутствует на странице"
        assert len(order_number_text) > 0, "Номер заказа пустой"

    def check_email(self, expected_email):
        email_text = self.wait.until(EC.visibility_of_element_located(self.email_field_locator)).text
        assert email_text == expected_email, \
            f"Email не соответствует ожидаемому. Ожидалось: {expected_email}, получено: {email_text}"

    def check_payment_method(self, expected_payment_method):
        payment_method_text = self.wait.until(EC.visibility_of_element_located(self.payment_method_locator)).text
        assert expected_payment_method in payment_method_text, \
            (f"Метод оплаты не соответствует ожидаемому.  Ожидалось: {expected_payment_method}, "
             f"получено: {payment_method_text}")

    def check_comment(self, expected_comment):
        comment_text = self.wait.until(EC.visibility_of_element_located(self.comment_field_locator)).text
        assert comment_text == expected_comment, \
            f"Комментарий не соответствует ожидаемому. Ожидалось: {expected_comment}, получено: {comment_text}"

    def get_shipping_parts(self):
        """Получаем все части full_shipping_information_locator как список строк"""
        full_text = self.wait.until(EC.visibility_of_element_located(self.full_shipping_information_locator)).text
        # Разделяем весь текст на отдельные строки
        all_lines = full_text.split('\n')  # Метод split('\n') разделяет текст там где есть перенос строки
        clean_parts = []  # Создаем пустой список для хранения очищенных строк
        for line in all_lines:
            cleaned_line = line.strip()  # Убираем лишние пробелы в начале и конце строки
            if cleaned_line:  # Если строка не пустая
                clean_parts.append(cleaned_line)  # Добавляем в наш список
        return clean_parts

    def check_first_and_last_name(self, expected_first_name, expected_last_name):
        clean_parts = self.get_shipping_parts()
        full_name = clean_parts[0]  # Первая строка - имя и фамилия
        assert expected_first_name in full_name, "Имя не соответствует"
        assert expected_last_name in full_name, "Фамилия не соответствует"

    def check_address(self, expected_address):
        clean_parts = self.get_shipping_parts()
        address = clean_parts[1]  # Вторая строка - адрес
        assert expected_address in address, \
            f"Адрес не соответствует. Ожидалось: {expected_address}, получено: {address}"

    def check_city(self, expected_city):
        clean_parts = self.get_shipping_parts()
        city = clean_parts[2]  # Третья строка - город
        assert expected_city in city, f"Город не соответствует. Ожидалось: {expected_city}, получено: {city}"

    def check_region(self, expected_region):
        clean_parts = self.get_shipping_parts()
        region = clean_parts[3]  # Четвертая строка - область
        assert expected_region in region, f"Область не соответствует. Ожидалось: {expected_region}, получено: {region}"

    def check_index(self, expected_index):
        clean_parts = self.get_shipping_parts()
        index = clean_parts[4]  # Пятая строка - индекс
        assert expected_index in index, f"Индекс не соответствует. Ожидалось: {expected_index}, получено: {index}"

    def check_phone(self, expected_phone):
        phone_text = self.wait.until(EC.visibility_of_element_located(self.phone_locator)).text
        assert expected_phone in phone_text, \
            f"Телефон не соответствует ожидаемому. Ожидалось: {expected_phone}, получено: {phone_text}"
