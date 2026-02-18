import logging
import time

from conftest import page, config
from pages.Dashboard import DashboardPage
from pages.login_page import Login_Page

def test_homepage(page, config):
    login = Login_Page(page, config["base_url"])
    login.open()
    login.enter_username("QATest6")
    time.sleep(2)
    login.enter_password("Thesword")
    login.login_button()
    time.sleep(3)

    dashboard = DashboardPage(page, config["base_url"])
    account_no = dashboard.open_account_and_get_number()
    assert account_no is not None
    assert "activity.htm" in page.url

    details_account_no = dashboard.get_account_number_from_details()
    logging.info(f"Account number: {details_account_no}")
    time.sleep(4)
    # assert account_no == details_account_no
