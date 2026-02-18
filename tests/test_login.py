import time

from pages.login_page import Login_Page


def test_login(page, config):
    login = Login_Page(page, config["base_url"])
    login.open()
    login.enter_username("QATest30")
    login.enter_password("Thesword")
    login.login_button()
    time.sleep(4)
