from selenium.webdriver.common.by import By

from pages.base_page import BasePage

FIRST_NAME_LOC = (By.CSS_SELECTOR, "input[name = 'firstname']")
LAST_NAME_LOC = (By.ID, "lastname")
EMAIL_LOC = (By.ID, "email_address")
PASSWORD_LOC = (By.ID, "password")
PASSWORD_CONFIRM_LOC = (By.ID, "password-confirmation")
CREATE_ACCOUNT_BTN_LOC = (By.CSS_SELECTOR, "[title = 'Create an Account']")
EMPTY_FIELD_ERROR_LOC = (By.XPATH, "//*[text()='This is a required field.']")
PASSWORD_CONFIRM_ERROR_LOC = (By.ID, "password-confirmation-error")


class CreateAccount(BasePage):
    page_endpoint = '/customer/account/create/'

    def fill_in_form(self, first_name, last_name, email, password, password_confirm):
        self.find(FIRST_NAME_LOC).send_keys(first_name)
        self.find(LAST_NAME_LOC).send_keys(last_name)
        self.find(EMAIL_LOC).send_keys(email)
        self.find(PASSWORD_LOC).send_keys(password)
        self.find(PASSWORD_CONFIRM_LOC).send_keys(password_confirm)
        self.find(CREATE_ACCOUNT_BTN_LOC).click()






