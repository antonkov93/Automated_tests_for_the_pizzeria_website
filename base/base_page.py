from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    log_in_header_locator = (By.XPATH, '//a[@class="account"]')
    log_out_header_locator = (By.XPATH, '//a[@class="logout"]')
    menu_header_locator = (By.XPATH, '//a[contains(text(),"Меню")]')
    menu_header_deserts_locator = (By.XPATH, '//li[@id="menu-item-391"]')
    main_header_locator = (By.XPATH, '(//a[@aria-current="page"])[1]')
    cart_header_locator = (By.XPATH, '//li[@id="menu-item-29"]')
    total_amount_cart_header_price_locator = (By.XPATH, "//a[@class='cart-contents wcmenucart-contents']")
    my_account_header_locator = (By.XPATH, '(//a[contains(text(),"Мой аккаунт")])[1]')
    making_order_header_locator = (By.XPATH, '(//a[contains(text(),"Оформление заказа")])[1]')

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def open(self):
        self.driver.get(self.page_url)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.page_url))

    def click_log_in_header(self):
        self.wait.until(EC.element_to_be_clickable(self.log_in_header_locator)).click()

    def click_log_out_header(self):
        self.wait.until(EC.element_to_be_clickable(self.log_out_header_locator)).click()

    def click_menu_header(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_header_locator)).click()

    def click_main_header(self):
        self.wait.until(EC.element_to_be_clickable(self.main_header_locator)).click()

    def click_cart_header(self):
        self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        self.wait.until(EC.element_to_be_clickable(self.cart_header_locator)).click()

    def click_my_account_header(self):
        self.wait.until(EC.element_to_be_clickable(self.my_account_header_locator)).click()

    def click_making_order_header(self):
        self.wait.until(EC.element_to_be_clickable(self.making_order_header_locator)).click()
