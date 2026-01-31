import pytest
from base.base_page import BasePage
from pages.my_account_page import MyAccountPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.menu_page import MenuPage
from pages.cart_page import CartPage
from pages.making_order_page import MakingOrderPage
from pages.product_page import ProductPage
from pages.order_received_page import OrderReceivedPage
from pages.bonus_page import BonusPage


class BaseTest:

    base_page: BasePage
    my_account_page: MyAccountPage
    main_page: MainPage
    register_page: RegisterPage
    menu_page: MenuPage
    cart_page: CartPage
    making_order_page: MakingOrderPage
    product_page: ProductPage
    order_received_page: OrderReceivedPage
    bonus_page: BonusPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.base_page = BasePage(driver)
        request.cls.my_account_page = MyAccountPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.register_page = RegisterPage(driver)
        request.cls.menu_page = MenuPage(driver)
        request.cls.cart_page = CartPage(driver)
        request.cls.making_order_page = MakingOrderPage(driver)
        request.cls.product_page = ProductPage(driver)
        request.cls.order_received_page = OrderReceivedPage(driver)
        request.cls.bonus_page = BonusPage(driver)
