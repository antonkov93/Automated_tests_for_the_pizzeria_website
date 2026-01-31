from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BonusPage(BasePage):

    page_url = 'https://pizzeria.skillbox.cc/bonus/'

    name_field_locator = (By.XPATH, '//input[@id="bonus_username"]')
    phone_field_locator = (By.XPATH, '//input[@id="bonus_phone"]')
    apply_for_card_locator = (By.XPATH, '//button[@name="bonus"]')
    validation_message_locator = (By.XPATH, '//div[@id="bonus_content"]')
    confirmation_message_locator = (By.XPATH, '//div[@id="bonus_main"]')
    loading_animation_locator = (By.XPATH, '//div[@class="loaderPoint"]')

    def click_apply_for_card(self):
        self.wait.until(EC.element_to_be_clickable(self.apply_for_card_locator)).click()

    def check_validation_message(self):
        validation_message_text = self.wait.until(
            EC.visibility_of_element_located(self.validation_message_locator)).text
        assert validation_message_text.strip() != "", "Сообщение о валидации не содержит текста"

    def enter_name(self, name):
        self.wait.until(EC.element_to_be_clickable(self.name_field_locator)).clear()
        self.wait.until(EC.element_to_be_clickable(self.name_field_locator)).send_keys(name)

    def enter_phone(self, phone):
        self.wait.until(EC.element_to_be_clickable(self.phone_field_locator)).clear()
        self.wait.until(EC.element_to_be_clickable(self.phone_field_locator)).send_keys(phone)

    def waiting_activation_bonus_program(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        loading_element = self.driver.find_element(*self.loading_animation_locator)
        self.wait.until(EC.staleness_of(loading_element))
        # self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))

    def check_confirmation_message(self, expected_confirmation_message):
        confirmation_message_text = self.wait.until(
            EC.visibility_of_element_located(self.confirmation_message_locator)).text
        assert expected_confirmation_message in confirmation_message_text, \
            "Сообщение об успешной активации не соответствует ожидаемому"
