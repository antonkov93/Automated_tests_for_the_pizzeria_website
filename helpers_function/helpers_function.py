import allure


def download_cookies_and_clear_cart(test_instance):
    """Загружает cookies и очищает корзину"""
    test_instance.my_account_page.download_cookies()
    test_instance.cart_page.open()
    test_instance.cart_page.clear_cart_and_remove_coupon()


def download_cookies_and_filling_cart(test_instance):
    """Загружает cookies и заполняет корзину товарами"""
    test_instance.my_account_page.download_cookies()
    test_instance.menu_page.open()
    test_instance.cart_page.filling_cart()


def making_order(test_instance):
    """Заполняет все поля для доставки и оформляет заказ"""
    with allure.step('Заполнить поля: Имя, Фамилия, Адрес, Город/Населенный пункт, '
                     'Область, Почтовый индекс, Телефон, Комментарий'):
        # Заполнение полей, а также сохранение данные для последующего сравнения в тест-кейсе №19
        order_data = {
            'first_name': test_instance.making_order_page.enter_first_name(15),
            'last_name': test_instance.making_order_page.enter_last_name(15),
            'address': test_instance.making_order_page.enter_address(35),
            'city': test_instance.making_order_page.enter_city(15),
            'region': test_instance.making_order_page.enter_region(15),
            'index': test_instance.making_order_page.enter_index(6),
            'phone': test_instance.making_order_page.enter_phone(11),
            'email': test_instance.making_order_page.get_email(),
            'comment': test_instance.making_order_page.enter_comment(40),
            'order_amount': test_instance.making_order_page.get_order_amount(),
            'payment_method': test_instance.making_order_page.get_payment_method()
        }
    with allure.step('Ввести/выбрать в поле календаря дату следующего дня'):
        test_instance.making_order_page.enter_calendar(1)
    with allure.step('Установить радио-баттон “Оплата при доставке”'):
        test_instance.making_order_page.click_payment_delivery_radiobutton()
    with allure.step('Установить чекбокс напротив строки “I have read and agree to the website terms and conditions”'):
        test_instance.making_order_page.click_terms_of_use_checkbox()
    with allure.step('Нажать кнопку "Оформить заказ"'):
        test_instance.making_order_page.click_place_order_button()
    return order_data


def registration_new_user(test_instance):
    """Заполняет все поля пользовательских данных и проводит регистрацию нового пользователя"""
    with allure.step('Заполнить поле "Имя пользователя"'):
        username = test_instance.register_page.enter_username(8, 4)
    with allure.step('Заполнить поле "Адрес почты"'):
        test_instance.register_page.enter_email(10)
    with allure.step('Заполнить поле "Пароль"'):
        test_instance.register_page.enter_password(5)
    with allure.step('Нажать кнопку "Зарегистрироваться"'):
        test_instance.register_page.click_registration_button()
    return username
