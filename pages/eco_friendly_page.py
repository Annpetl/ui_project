from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

SORTER_LOC = (By.CSS_SELECTOR, "#sorter")
PRICE_LIST_LOC = (By.CLASS_NAME, "price-wrapper")
PRODUCT_LIST_LOC = (By.CSS_SELECTOR, "a.product-item-link")


class EcoFriendly(BasePage):
    page_endpoint = '/collections/eco-friendly.html'

    def select_by_value(self, value):
        Select(self.find(SORTER_LOC)).select_by_value(value)

    def check_sort_by_price(self):
        self.click(SORTER_LOC)
        price_list = [float(price.text[1:]) for price in self.find_all(PRICE_LIST_LOC)]
        assert price_list == sorted(price_list)

    def check_sort_by_product_name(self):
        self.click(SORTER_LOC)
        product_title_list = [product.text for product in self.find_all(PRODUCT_LIST_LOC)]
        assert product_title_list == sorted(product_title_list)
