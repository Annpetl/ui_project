from selenium.webdriver.common.by import By
from pages.base_page import BasePage

CATEGORY_MENU_TITLES_LOC = (By.CSS_SELECTOR, "div.categories-menu>strong.title")
BLOCK_PROMO_ELEMS_LOC = (By.CSS_SELECTOR, "a.block-promo")


class SalePage(BasePage):
    page_endpoint = '/sale.html'

    def check_category_menu_titles_are(self, title_list: list):
        categoty_title_list = [elem.text.upper() for elem in self.find_all(CATEGORY_MENU_TITLES_LOC)]
        assert categoty_title_list == title_list

    def check_block_promo_elems_count_is(self, count):
        assert len(self.find_all(BLOCK_PROMO_ELEMS_LOC)) == count
