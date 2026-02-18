from pages.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, page, base_url=None):
        super().__init__(page, base_url)

    def open(self):
        self.page.goto(self.base_url)
        self.page.wait_for_load_state("networkidle")

    def click_register(self):
        self.page.click('a[href*="register.htm"]')

    def enter_firstname(self, firstname):
        self.page.fill('input[name="customer.firstName"]', firstname)

    def enter_last_name(self, lastname):
        self.page.fill('input[name="customer.lastName"]', lastname)

    def enter_address(self, address):
        self.page.fill('input[name="customer.address.street"]', address)

    def enter_city(self, city):
        self.page.fill('input[name="customer.address.city"]', city)

    def enter_state(self, state):
        self.page.fill('input[name="customer.address.state"]', state)

    def enter_zip_code(self, zip_code):
        self.page.fill('input[name="customer.address.zipCode"]', zip_code)

    def enter_phone(self, phone):
        self.page.fill('input[name="customer.phoneNumber"]', phone)

    def enter_ssn(self, ssn):
        self.page.fill('input[name="customer.ssn"]', ssn)

    def enter_username(self, username):
        self.page.fill('input[name="customer.username"]', username)

    def enter_password(self, password):
        self.page.fill('input[name="customer.password"]', password)

    def enter_confirm_password(self, confirm_password):
        self.page.fill('input[name="repeatedPassword"]', confirm_password)

    def click_register_button(self):
        self.page.click('input[value="Register"]')

    # 👉 reusable method
    def register_user(self, username, password):
        self.open()
        self.click_register()
        self.enter_firstname("QAA")
        self.enter_last_name("Saxena")
        self.enter_address("Crossing")
        self.enter_city("Noida")
        self.enter_state("UP")
        self.enter_zip_code("123456")
        self.enter_phone("123456789")
        self.enter_ssn("123756")
        self.enter_username(username)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.click_register_button()
