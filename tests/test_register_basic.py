import time

from pages.register_page import RegisterPage


def test_basic_register(page, config):
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
    reg.enter_username("QATest48")
    reg.enter_password("Thesword")
    reg.enter_confirm_password("Thesword")
    reg.click_register_button()
    time.sleep(3)
