from pages.eco_friendly_page import SORTER_LOC


def test_sale_page_is_open(eco_friendly_page):
    eco_friendly_page.check_page_endpoint_is_correct()
    eco_friendly_page.check_page_title_is('Eco Friendly')


def test_sort_by_price(eco_friendly_page):
    eco_friendly_page.click(SORTER_LOC)
    eco_friendly_page.select_by_value('price')
    eco_friendly_page.check_sort_by_price()


def test_sort_by_name(eco_friendly_page):
    eco_friendly_page.click(SORTER_LOC)
    eco_friendly_page.select_by_value('name')
    eco_friendly_page.check_sort_by_product_name()
