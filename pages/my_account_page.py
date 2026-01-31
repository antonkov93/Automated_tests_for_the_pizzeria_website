import os
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from selenium.webdriver.common.by import By
import pickle


class MyAccountPage(BasePage):

    page_url = 'https://pizzeria.skillbox.cc/my-account/'

    # без авторизации
    username_field_locator = (By.XPATH, '//input[@id="username"]')
    password_field_locator = (By.XPATH, '//input[@id="password"]')
    login_button_locator = (By.XPATH, '//button[contains(text(),"Войти")]')
    remember_me_checkbox_locator = (By.XPATH, '//input[@id="rememberme"]')
    forgot_password_locator = (By.XPATH, '//a[contains(text(),"Забыли пароль?")]')
    register_button_locator = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')

    # с авторизацией
    log_out_button_locator = (By.XPATH, '//p/a[contains(text(),"Выйти")]')
    authorized_username_locator = (By.XPATH, '//p[contains(text(), "Привет")]/strong')

    def enter_username(self, username):
        self.wait.until(EC.element_to_be_clickable(self.username_field_locator)).send_keys(username)
        return username

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.password_field_locator)).send_keys(password)

    def click_remember_me_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.remember_me_checkbox_locator)).click()

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button_locator)).click()

    def click_registration_button(self):
        self.wait.until(EC.element_to_be_clickable(self.register_button_locator)).click()

    def save_cookies(self):
        self.driver.get(self.page_url)
        self.wait.until(EC.element_to_be_clickable(self.username_field_locator)).send_keys('hiddify')
        self.wait.until(EC.element_to_be_clickable(self.password_field_locator)).send_keys('1234')
        self.wait.until(EC.element_to_be_clickable(self.remember_me_checkbox_locator)).click()
        self.wait.until(EC.element_to_be_clickable(self.login_button_locator)).click()
        cookies_path = os.path.dirname(__file__) + "/../cookies/cookies.pkl"
        os.makedirs(os.path.dirname(cookies_path), exist_ok=True)
        pickle.dump(self.driver.get_cookies(), open(cookies_path, "wb"))

    def download_cookies(self):
        self.driver.delete_all_cookies()
        cookies_path = os.path.dirname(__file__) + "/../cookies/cookies.pkl"
        cookies = pickle.load(open(cookies_path, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
