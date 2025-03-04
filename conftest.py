import random

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
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    prefs = {
        "profile.default_content_setting_values.cookies": 2,
        "profile.default_content_setting_values.popups": 2,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.automatic_downloads": 1
    }
    options.add_experimental_option("prefs", prefs)
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.save_screenshot(f'{str(random.randint(100,1000))}.png')



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
