from pages.base_page import BasePage
from selenium.webdriver.common.by import By

SUCCESS_CREATE_MSG_LOC = (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')


class CustomerAccount(BasePage):
    page_endpoint = '/customer/account/'

    def check_success_create_msg_is(self, text):
        assert self.get_text(SUCCESS_CREATE_MSG_LOC) == text
