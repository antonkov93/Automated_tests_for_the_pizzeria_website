import allure
from base.base_test import BaseTest
from helpers_function.helpers_function import download_cookies_and_filling_cart, making_order


@allure.story('Тестирование страницы "Подтверждение заказа"')
class TestOrderReceivedPage(BaseTest):



    @allure.title('Проверка данных в подтверждении заказа')
    def test_keys19(self):
        # загрузка куков и заполнение корзины (выполнение предусловий тест-кейса)
        download_cookies_and_filling_cart(self)
        # оформление заказа, а также загрузка данных для проверки (order_data) (выполнение предусловий тест-кейса)
        self.making_order_page.open()
        order_data = making_order(self)
        # начало выполнения тест-кейса
        with allure.step('Проверить соответствие общей суммы'):
            self.order_received_page.check_order_amount(order_data['order_amount'])
        with allure.step('Проверить наличие номера заказа'):
            self.order_received_page.check_order_number()
        with allure.step('Проверить соответствие e-mail'):
            self.order_received_page.check_email(order_data['email'])
        with allure.step('Проверить соответствие метода оплаты'):
            self.order_received_page.check_payment_method(order_data['payment_method'])
        with allure.step('Проверить соответствие комментария к заказу'):
            self.order_received_page.check_comment(order_data['comment'])
        with allure.step('Проверить соответствие имени и фамилии'):
            self.order_received_page.check_first_and_last_name(order_data['first_name'], order_data['last_name'])
        with allure.step('Проверить соответствие адреса'):
            self.order_received_page.check_address(order_data['address'])
        with allure.step('Проверить соответствие города / населенного пункта'):
            self.order_received_page.check_city(order_data['city'])
        with allure.step('Проверить соответствие области'):
            self.order_received_page.check_region(order_data['region'])
        with allure.step('Проверить соответствие индекса'):
            self.order_received_page.check_index(order_data['index'])
        with allure.step('Проверить соответствие телефона'):
            self.order_received_page.check_phone(order_data['phone'])
