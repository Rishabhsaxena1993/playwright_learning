import time

from pages.login_page import Login_Page
from pages.register_page import RegisterPage
from pages.transfer_funds import Transfer_Funds


def login_or_register(self, username, password):
    self.open()
    self.enter_username(username)
    self.enter_password(password)
    self.login_button()

    try:
        self.page.wait_for_selector("text=Accounts Overview", timeout=3000)
    except:
        RegisterPage(self.page, self.base_url).register_new_user(username, password)
