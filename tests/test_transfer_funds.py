import time

from pages.login_page import Login_Page
from pages.transfer_funds import Transfer_Funds


def test_transfer_funds(page, config):

    login = Login_Page(page, config['base_url'])
    login.open()
    login.enter_username("QATest48")
    login.enter_password("Thesword")
    login.login_button()
    time.sleep(2)

    transfer_funds = Transfer_Funds(page,config["base_url"])
    transfer_funds.click_on_Transfer_Funds()
    time.sleep(2)
    transfer_funds.enter_amount("2")
    transfer_funds.choose_from_accounts("13677")
    transfer_funds.choose_to_accounts("13566")
    time.sleep(2)
    transfer_funds.click_on_transfer_button()
    time.sleep(3)
    transfer_funds.verify_transfer_complete_message()
    transfer_funds.verify_amount_transffered()
    transfer_funds.verify_from_account()
    transfer_funds.verify_to_account()