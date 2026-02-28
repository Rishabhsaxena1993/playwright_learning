import time

import pytest

from pages.open_new_account import Open_New_Account
from pages.register_page import RegisterPage
from pages.transfer_funds import Transfer_Funds

@pytest.mark.flaky(reruns=0)
def test_E2E_transfer_funds(page, config):

    reg = RegisterPage(page, config["base_url"])
    reg.open()
    reg.click_register()
    reg.enter_firstname("QAA")
    reg.enter_last_name("Saxena")
    reg.enter_address("Crossing")
    reg.enter_city("Noida")
    reg.enter_state("UP")
    reg.enter_zip_code("123456")
    reg.enter_phone("123456789")
    reg.enter_ssn("123756")
    reg.enter_username("rishabh")
    reg.enter_password("Thesword")
    reg.enter_confirm_password("Thesword")
    reg.click_register_button()


    open_new_account = Open_New_Account(page, config["base_url"])
    open_new_account.click_open_new_account()
    time.sleep(2)
    open_new_account.click_open_account_button()
    account_number = open_new_account.get_newly_added_account_number()
    open_new_account.click_newly_added_account_number()
    time.sleep(5)
    # open_new_account.verify_congratulation_message()
    # time.sleep(5)
    transfer_funds = Transfer_Funds(page,config["base_url"])

    transfer_funds.click_on_Transfer_Funds()
    transfer_funds.enter_amount("100")
    transfer_funds.select_first_from_account()
    transfer_funds.select_second_to_account()
    transfer_funds.click_on_transfer_button()
    # assert transfer_funds.verify_transfer_complete_message() == "Transfer Complete!"
    # assert transfer_funds