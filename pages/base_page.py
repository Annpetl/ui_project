from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = "https://magento.softwaretestingboard.com/"
    page_endpoint = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        self.driver.get(f'{self.base_url}{self.page_endpoint}')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        return self.driver.find_element(*locator).click()

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def check_elem_text_is(self, locator, text):
        assert self.find(locator).text == text

    def check_elems_text_is(self, locator, title_list: list):
        categoty_title_list = [elem.text for elem in self.find_all(locator)]
        assert categoty_title_list == title_list

    def check_page_title_is(self, title):
        assert self.driver.title == title

    def check_page_endpoint_is_correct(self):
        assert self.driver.current_url.endswith(self.page_endpoint)

    def check_length_of_elems(self, locator, length):
        assert len(self.find_all(locator)) == length
