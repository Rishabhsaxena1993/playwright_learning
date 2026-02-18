import time

from pages.login_page import Login_Page
from pages.open_new_account import Open_New_Account
from pages.register_page import RegisterPage


def test_open_basic_account(page, config):
    login = Login_Page(page, config["base_url"])
    login.open()
    login.enter_username("QATest48")
    login.enter_password("Thesword")
    login.login_button()

    open_new_account = Open_New_Account(page, config["base_url"])
    open_new_account.click_open_new_account()
    time.sleep(2)

    # if not page.locator("text=Accounts Overview").is_visible():
    #    reg = RegisterPage(page, config["base_url"])
    #    reg.register_user("QATest48", "Thesword")

    open_new_account = Open_New_Account(page, config["base_url"])
    open_new_account.click_open_new_account()
    time.sleep(2)

    # //0 is for Checking and 1 is for Savings
    open_new_account.select_account_type("1")

    open_new_account.click_open_account_button()
    time.sleep(3)
    account_number = open_new_account.get_newly_added_account_number()
    print("Account Number:", account_number)

    open_new_account.verify_congratulation_message()

    time.sleep(2)
    open_new_account.click_newly_added_account_number()
    time.sleep(3)
    #
    open_new_account.verify_printed_account_number()

    open_new_account.verify_balance()
    open_new_account.verify_available_balance()
    open_new_account.handle_month("January")
    open_new_account.transactionType("ALL")
    open_new_account.date_of_transaction()
    open_new_account.funds_transfer_received_link()
    open_new_account.transaction_id()
    open_new_account.date_of_transaction_on_transaction_page()
    open_new_account.verify_description()
    open_new_account.verify_type_of_transaction()
    open_new_account.verify_amount()
