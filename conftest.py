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
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.set_window_size(900, 1250)
    return chrome_driver


@pytest.fixture()
def sale_page(driver):
    sale_page = SalePage(driver)
    sale_page.open_page()
    return sale_page


@pytest.fixture()
def eco_friendly_page(driver):
    eco_friendly_page = EcoFriendly(driver)
    eco_friendly_page.open_page()
    return eco_friendly_page


@pytest.fixture()
def create_account_page(driver):
    create_account_page = CreateAccount(driver)
    create_account_page.open_page()
    return create_account_page


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
