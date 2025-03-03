from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from faker import Faker
from random import randint

from pages.create_account_page import CreateAccount
from pages.customer_account_page import CustomerAccount
from pages.sale_page import SalePage
from pages.eco_friendly_page import EcoFriendly


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--force-device-scale-factor=0.75')
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.set_window_size(900, 1250)
    return chrome_driver


@pytest.fixture()
def sale(driver):
    return SalePage(driver)


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def create_account(driver):
    return CreateAccount(driver)


@pytest.fixture()
def customer_account(driver):
    return CustomerAccount(driver)


@pytest.fixture()
def create_test_data():
    faker_data = Faker()
    password = faker_data.password(length=randint(8, 15), digits=True, upper_case=True, lower_case=True,
                                   special_chars=True)
    return {
        'name': faker_data.name(),
        'last_name': faker_data.last_name(),
        'email': faker_data.email(),
        'password': password,
        'password_confirm': password
    }
