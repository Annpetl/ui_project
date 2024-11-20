from pages.create_account_page import CREATE_ACCOUNT_BTN_LOC, PASSWORD_CONFIRM_ERROR_LOC, EMPTY_FIELD_ERROR_LOC
from pages.customer_account_page import SUCCESS_CREATE_MSG_LOC


def test_valid_body(create_account_page, customer_account, create_test_data):
    create_account_page.fill_in_form(create_test_data['name'], create_test_data['last_name'], create_test_data['email'],
                                     create_test_data['password'], create_test_data['password_confirm'])
    customer_account.check_page_title_is('My Account')
    customer_account.check_page_endpoint_is_correct()
    customer_account.check_elem_text_is(SUCCESS_CREATE_MSG_LOC,
                                        "Thank you for registering with Main Website Store.")


def test_empty_body(create_account_page):
    create_account_page.open_page()
    create_account_page.find(CREATE_ACCOUNT_BTN_LOC).click()
    create_account_page.check_length_of_elems(EMPTY_FIELD_ERROR_LOC, 5)
    create_account_page.check_page_endpoint_is_correct()


def test_incorrect_confirm_password(create_account_page, create_test_data):
    create_account_page.fill_in_form(create_test_data['name'], create_test_data['last_name'], create_test_data['email'],
                                     create_test_data['password'], password_confirm='111111')
    create_account_page.check_elem_text_is(PASSWORD_CONFIRM_ERROR_LOC, "Please enter the same value again.")
    create_account_page.check_page_endpoint_is_correct()
