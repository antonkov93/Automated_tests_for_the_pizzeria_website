from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from pages.my_account_page import MyAccountPage
from selenium.webdriver.common.by import By
from faker import Faker


class RegisterPage(BasePage):

    page_url = 'https://pizzeria.skillbox.cc/register/'

    username_field_locator = (By.XPATH, '//input[@id="reg_username"]')
    email_field_locator = (By.XPATH, '//input[@id="reg_email"]')
    password_field_locator = (By.XPATH, '//input[@id="reg_password"]')
    register_button_locator = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')

    fake = Faker('ru_RU')  # Просто создаем на уровне класса

    def enter_username(self, username_max_length, number_length):
        username = self.fake.user_name()[:username_max_length] + str(self.fake.random_number(digits=number_length))
        self.wait.until(EC.element_to_be_clickable(self.username_field_locator)).send_keys(username)
        return username

    def enter_email(self, name_email_max_length):
        name_email = self.fake.user_name()[:name_email_max_length]  # Максимум 10 символов для имени
        domain = "mail.ru"
        email = f"{name_email}@{domain}"
        self.wait.until(EC.element_to_be_clickable(self.email_field_locator)).send_keys(email)

    def enter_password(self, password_length):
        password = self.fake.password(length=password_length, special_chars=False)
        self.wait.until(EC.element_to_be_clickable(self.password_field_locator)).send_keys(password)

    def click_registration_button(self):
        self.wait.until(EC.element_to_be_clickable(self.register_button_locator)).click()
        self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))

    def check_greeting_user_name(self, expected_username):
        my_account_page = MyAccountPage(self.driver)
        authorized_username_text = self.wait.until(EC.visibility_of_element_located(
            my_account_page.authorized_username_locator)).text
        assert expected_username in authorized_username_text, \
            "Имя пользователя в ЛК не совпадает с именем пользователя при регистрации"

    def check_registration_page_loaded(self):
        self.wait.until(EC.url_contains(self.page_url))
        current_url = self.driver.current_url
        expected_url = self.page_url
        assert expected_url in current_url, "Текущий URL не соответствует ожидаемому"
