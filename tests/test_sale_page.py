from pages.sale_page import CATEGORY_MENU_TITLES_LOC,BLOCK_PROMO_ELEMS_LOC


def test_sale_page_is_open(sale_page):
    sale_page.check_page_endpoint_is_correct()
    sale_page.check_page_title_is('Sale')


def test_category_menu_titles(sale_page):
    sale_page.check_elems_text_is(CATEGORY_MENU_TITLES_LOC, title_list=["WOMEN'S DEALS", "MENS'S DEALS", 'GEAR DEALS'])


def test_block_promo_elems_length(sale_page):
    sale_page.check_length_of_elems(BLOCK_PROMO_ELEMS_LOC, length=6)
