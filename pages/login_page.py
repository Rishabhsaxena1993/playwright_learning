from pages.base_page import BasePage


class Login_Page(BasePage):
    def __init__(self, page, base_url=None):
        super().__init__(page, base_url)

    # def navigate(self):
        # self.page.goto(self.base_url)

    def open(self):
        self.page.goto(self.base_url)
        self.page.wait_for_load_state("networkidle")

    def enter_username(self, username):
        self.page.fill('input[name="username"]', username)

    def enter_password(self, password):
        self.page.fill('input[name="password"]', password)

    def login_button(self):
        self.page.click('input[value="Log In"]')
