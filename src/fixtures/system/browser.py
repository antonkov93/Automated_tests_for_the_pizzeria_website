import pytest
import logging
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    logging.info('Preparing the Chrome Browser...')
    # # Получаем абсолютный путь к драйверу
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # driver_path = os.path.join(current_dir, '../../../drivers/chromedriver.exe')
    # service = Service(driver_path)
    driver = webdriver.Chrome(options=options)
    # Присваиваем драйвер классу теста
    # request.cls.driver = driver
    logging.info('Browser has been started...')

    yield driver

    driver.quit()
