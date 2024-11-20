from selenium.webdriver.common.by import By
from pages.base_page import BasePage

CATEGORY_MENU_TITLES_LOC = (By.CSS_SELECTOR, "div.categories-menu>strong.title")
BLOCK_PROMO_ELEMS_LOC = (By.CSS_SELECTOR, "a.block-promo")


class SalePage(BasePage):
    page_endpoint = '/sale.html'

